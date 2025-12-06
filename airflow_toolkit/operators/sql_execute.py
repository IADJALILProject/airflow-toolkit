from __future__ import annotations

from typing import Any, Optional

from airflow.hooks.base import BaseHook
from airflow.models import BaseOperator
from airflow.utils.context import Context

from airflow_toolkit.utils.logging_utils import get_logger


class SqlExecuteOperator(BaseOperator):
    """
    Operator générique pour exécuter une requête SQL sur n'importe quelle connexion
    supportée par DbApiHook (Postgres, MySQL, etc.).

    Il utilise la connexion Airflow fournie (conn_id) et supporte :
    - exécution simple (sans retour)
    - `autocommit` configurable
    """

    def __init__(
        self,
        sql: str,
        conn_id: str,
        autocommit: bool = True,
        parameters: Optional[dict[str, Any]] = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.sql = sql
        self.conn_id = conn_id
        self.autocommit = autocommit
        self.parameters = parameters or {}
        self.logger = get_logger(self.__class__.__name__)

    def execute(self, context: Context) -> None:
        self.logger.info("Exécution SQL via connexion '%s'", self.conn_id)
        hook = BaseHook.get_connection(self.conn_id).get_hook()

        # hook peut être un DbApiHook ou dérivé
        hook.run(self.sql, parameters=self.parameters, autocommit=self.autocommit)
        self.logger.info("Requête exécutée avec succès.")
