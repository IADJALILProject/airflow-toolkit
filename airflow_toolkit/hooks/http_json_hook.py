from __future__ import annotations

from typing import Any, Dict, Optional, Union

import requests
from airflow.hooks.base import BaseHook


class HttpJsonHook(BaseHook):
    """
    Hook simple pour appeler des APIs HTTP/HTTPS en s'appuyant sur la connexion Airflow.

    Connexion Airflow de type HTTP :
      - host
      - schema (http/https)
      - login/password (optionnel)
      - extra: headers par défaut, timeout, etc.
    """

    conn_name_attr = "http_conn_id"
    default_conn_name = "http_default"
    conn_type = "http"
    hook_name = "HTTP JSON"

    def __init__(self, http_conn_id: str = default_conn_name) -> None:
        super().__init__()
        self.http_conn_id = http_conn_id

    def _build_url(self, endpoint: str) -> str:
        conn = self.get_connection(self.http_conn_id)
        base = conn.get_uri().replace("://:@", "://")  # clean si pas de login/pwd
        if base.endswith("/"):
            base = base[:-1]
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        return base + endpoint

    def run(
        self,
        endpoint: str,
        method: str = "GET",
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None,
        return_json: bool = True,
        timeout: int = 30,
    ) -> Union[Dict[str, Any], bytes]:
        url = self._build_url(endpoint)
        conn = self.get_connection(self.http_conn_id)
        extras = conn.extra_dejson or {}

        default_headers = extras.get("headers", {})
        merged_headers: Dict[str, str] = {**default_headers, **(headers or {})}

        auth = None
        if conn.login:
            auth = (conn.login, conn.password or "")

        self.log.info("HTTP %s %s", method, url)
        resp = requests.request(
            method=method,
            url=url,
            params=params,
            headers=merged_headers,
            json=json,
            timeout=timeout,
            auth=auth,
        )
        resp.raise_for_status()

        if return_json:
            return resp.json()
        return resp.content
