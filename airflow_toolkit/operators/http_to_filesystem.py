from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional

from airflow.models import BaseOperator
from airflow.utils.context import Context

from airflow_toolkit.hooks.http_json_hook import HttpJsonHook
from airflow_toolkit.utils.logging_utils import get_logger


class HttpToFilesystemOperator(BaseOperator):
    """
    Operator pour faire un GET HTTP/HTTPS et sauvegarder la réponse dans un fichier.

    Cas d'usage :
    - ingestion d'API REST (JSON) dans un fichier brut
    - récupération d'un fichier distant (CSV, JSON, etc.)
    """

    def __init__(
        self,
        endpoint: str,
        target_path: str,
        http_conn_id: str = "http_default",
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        method: str = "GET",
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.endpoint = endpoint
        self.target_path = Path(target_path)
        self.http_conn_id = http_conn_id
        self.params = params or {}
        self.headers = headers or {}
        self.method = method
        self.logger = get_logger(self.__class__.__name__)

    def execute(self, context: Context) -> str:
        self.logger.info("Appel HTTP %s sur %s", self.method, self.endpoint)

        hook = HttpJsonHook(http_conn_id=self.http_conn_id)
        content = hook.run(
            endpoint=self.endpoint,
            method=self.method,
            params=self.params,
            headers=self.headers,
            return_json=False,
        )

        self.target_path.parent.mkdir(parents=True, exist_ok=True)
        self.target_path.write_bytes(content)

        self.logger.info("Réponse sauvegardée dans %s", self.target_path)
        return str(self.target_path)
