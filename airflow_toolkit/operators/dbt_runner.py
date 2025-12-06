from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional

from airflow.models import BaseOperator
from airflow.utils.context import Context

from airflow_toolkit.utils.logging_utils import get_logger


class DbtRunnerOperator(BaseOperator):
    """
    Operator générique pour exécuter des commandes dbt via la CLI.

    Il ne dépend pas de la lib Python dbt :
    - il exécute simplement `dbt` comme un binaire (subprocess)
    - idéal pour les projets où dbt est installé dans l'image Docker Airflow.

    Exemple :
    DbtRunnerOperator(
        task_id="dbt_run",
        project_dir="/opt/dbt/project",
        command="run",
        select=["tag:daily"],
    )
    """

    def __init__(
        self,
        project_dir: str,
        command: str = "run",
        profiles_dir: Optional[str] = None,
        select: Optional[List[str]] = None,
        exclude: Optional[List[str]] = None,
        vars: Optional[Dict[str, Any]] = None,
        full_refresh: bool = False,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.project_dir = Path(project_dir)
        self.command = command
        self.profiles_dir = Path(profiles_dir) if profiles_dir else None
        self.select = select or []
        self.exclude = exclude or []
        self.vars = vars or {}
        self.full_refresh = full_refresh
        self.logger = get_logger(self.__class__.__name__)

    def build_command(self) -> List[str]:
        cmd: List[str] = ["dbt", self.command, "--project-dir", str(self.project_dir)]

        if self.profiles_dir:
            cmd += ["--profiles-dir", str(self.profiles_dir)]

        if self.select:
            cmd += ["--select", " ".join(self.select)]

        if self.exclude:
            cmd += ["--exclude", " ".join(self.exclude)]

        if self.vars:
            import json

            cmd += ["--vars", json.dumps(self.vars)]

        if self.full_refresh and self.command in {"run", "seed"}:
            cmd.append("--full-refresh")

        return cmd

    def execute(self, context: Context) -> None:
        if not self.project_dir.exists():
            raise FileNotFoundError(f"dbt project_dir does not exist: {self.project_dir}")

        cmd = self.build_command()
        self.logger.info("Exécution de la commande dbt : %s", " ".join(cmd))

        completed = subprocess.run(
            cmd,
            cwd=str(self.project_dir),
            check=False,
            capture_output=True,
            text=True,
        )

        self.logger.info("dbt stdout:\n%s", completed.stdout)
        if completed.stderr:
            self.logger.warning("dbt stderr:\n%s", completed.stderr)

        if completed.returncode != 0:
            raise RuntimeError(f"dbt command failed with code {completed.returncode}")
