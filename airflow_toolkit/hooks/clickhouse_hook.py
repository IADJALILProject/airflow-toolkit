from __future__ import annotations

from typing import Any, Iterable, List, Optional

from airflow.hooks.base import BaseHook
from clickhouse_driver import Client


class ClickHouseHook(BaseHook):
    """
    Hook ClickHouse basé sur clickhouse-driver.

    Utilise une connexion Airflow de type 'clickhouse' ou générique avec :
      - host
      - port
      - login
      - password
      - schema (database)
    """

    conn_name_attr = "clickhouse_conn_id"
    default_conn_name = "clickhouse_default"
    conn_type = "clickhouse"
    hook_name = "ClickHouse"

    def __init__(self, clickhouse_conn_id: str = default_conn_name) -> None:
        super().__init__()
        self.clickhouse_conn_id = clickhouse_conn_id
        self._client: Optional[Client] = None

    def get_conn(self) -> Client:
        if self._client:
            return self._client

        conn = self.get_connection(self.clickhouse_conn_id)
        extras = conn.extra_dejson or {}

        self._client = Client(
            host=conn.host,
            port=conn.port or 9000,
            user=conn.login or "default",
            password=conn.password or "",
            database=conn.schema or extras.get("database", "default"),
            settings=extras.get("settings", {}),
        )
        return self._client

    def run(
        self, sql: str, params: Optional[dict[str, Any]] = None
    ) -> List[Iterable[Any]]:
        """
        Exécute une requête SQL et retourne un itérable de lignes.
        """
        client = self.get_conn()
        self.log.info("Exécution SQL ClickHouse : %s", sql)
        return list(client.execute_iter(sql, params=params))
