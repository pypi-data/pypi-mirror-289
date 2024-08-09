import datetime
from abc import ABC
from typing import Any, Dict, List, NamedTuple

import requests
from dagster import AssetKey
from dagster._core.errors import DagsterError
from pydantic import BaseModel


class AirflowInstance(NamedTuple):
    auth_backend: "AirflowAuthBackend"
    name: str

    @property
    def normalized_name(self) -> str:
        return self.name.replace(" ", "_").replace("-", "_")

    def get_api_url(self) -> str:
        return f"{self.auth_backend.get_webserver_url()}/api/v1"

    def list_dags(self) -> List["DagInfo"]:
        response = self.auth_backend.get_session().get(f"{self.get_api_url()}/dags")
        if response.status_code == 200:
            dags = response.json()
            return [
                DagInfo(
                    dag_id=dag["dag_id"],
                    metadata=dag,
                )
                for dag in dags["dags"]
            ]
        else:
            raise DagsterError(
                f"Failed to fetch DAGs. Status code: {response.status_code}, Message: {response.text}"
            )

    def get_task_info(self, dag_id: str, task_id: str) -> "TaskInfo":
        response = self.auth_backend.get_session().get(
            f"{self.get_api_url()}/dags/{dag_id}/tasks/{task_id}"
        )
        if response.status_code == 200:
            return TaskInfo(
                dag_id=dag_id,
                task_id=task_id,
                metadata=response.json(),
            )
        else:
            raise DagsterError(
                f"Failed to fetch task info for {dag_id}/{task_id}. Status code: {response.status_code}, Message: {response.text}"
            )

    def get_dag_url(self, dag_id: str) -> str:
        return f"{self.auth_backend.get_webserver_url()}/dags/{dag_id}"

    def get_dag_run_url(self, dag_id: str, run_id: str) -> str:
        return f"{self.auth_backend.get_webserver_url()}/dags/{dag_id}/grid?dag_run_id={run_id}&tab=details"

    def get_task_instance_url(self, dag_id: str, task_id: str, run_id: str) -> str:
        # http://localhost:8080/dags/print_dag/grid?dag_run_id=manual__2024-08-08T17%3A21%3A22.427241%2B00%3A00&task_id=print_task
        return f"{self.auth_backend.get_webserver_url()}/dags/{dag_id}/grid?dag_run_id={run_id}&task_id={task_id}"

    def get_task_instance_log_url(self, dag_id: str, task_id: str, run_id: str) -> str:
        # http://localhost:8080/dags/print_dag/grid?dag_run_id=manual__2024-08-08T17%3A21%3A22.427241%2B00%3A00&task_id=print_task&tab=logs
        return f"{self.get_task_instance_url(dag_id, task_id, run_id)}&tab=logs"

    def get_dag_run_asset_key(self, dag_id: str) -> AssetKey:
        return AssetKey([self.normalized_name, "dag", dag_id])

    def get_dag_source_code(self, file_token: str) -> str:
        response = self.auth_backend.get_session().get(
            f"{self.get_api_url()}/dagSources/{file_token}"
        )
        if response.status_code == 200:
            return response.text
        else:
            raise DagsterError(
                f"Failed to fetch source code. Status code: {response.status_code}, Message: {response.text}"
            )

    @staticmethod
    def airflow_str_from_datetime(dt: datetime.datetime) -> str:
        return dt.strftime("%Y-%m-%dT%H:%M:%S+00:00")

    def get_dag_runs(
        self, dag_id: str, start_date: datetime.datetime, end_date: datetime.datetime
    ) -> List[Dict[str, Any]]:
        response = self.auth_backend.get_session().get(
            f"{self.get_api_url()}/dags/{dag_id}/dagRuns",
            params={
                "updated_at_gte": self.airflow_str_from_datetime(start_date),
                "updated_at_lte": self.airflow_str_from_datetime(end_date),
                "state": ["success"],
            },
        )
        if response.status_code == 200:
            return response.json()["dag_runs"]
        else:
            raise DagsterError(
                f"Failed to fetch dag runs for {dag_id}. Status code: {response.status_code}, Message: {response.text}"
            )

    @staticmethod
    def timestamp_from_airflow_date(airflow_date: str) -> float:
        try:
            return datetime.datetime.strptime(airflow_date, "%Y-%m-%dT%H:%M:%S+00:00").timestamp()
        except ValueError:
            return datetime.datetime.strptime(
                airflow_date, "%Y-%m-%dT%H:%M:%S.%f+00:00"
            ).timestamp()


class DagInfo(BaseModel):
    dag_id: str
    metadata: Dict[str, Any]


class TaskInfo(BaseModel):
    dag_id: str
    task_id: str
    metadata: Dict[str, Any]


class DagRun(BaseModel):
    dag_id: str
    note: str
    state: str
    airflow_run_id: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    run_type: str
    airflow_run_config: Dict[str, Any]
    raw_metadata: Dict[str, Any]

    @property
    def success(self) -> bool:
        return self.state == "success"


class AirflowAuthBackend(ABC):
    def get_session(self) -> requests.Session:
        raise NotImplementedError("This method must be implemented by subclasses.")

    def get_webserver_url(self) -> str:
        raise NotImplementedError("This method must be implemented by subclasses.")
