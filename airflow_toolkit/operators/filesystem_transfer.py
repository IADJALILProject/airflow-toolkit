from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

from airflow.models import BaseOperator
from airflow.utils.context import Context

from airflow_toolkit.utils.logging_utils import get_logger


class FilesystemTransferOperator(BaseOperator):
    """
    Operator pour copier un fichier local d'un chemin source vers un chemin cible.

    Idéal pour :
    - démos
    - pré-ingestion simple
    - tests unitaires

    Cette version implémente :
    - vérifications d'existence
    - création des dossiers cibles
    - option d'overwrite
    """

    def __init__(
        self,
        source_path: str,
        target_path: str,
        overwrite: bool = True,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.source_path = Path(source_path)
        self.target_path = Path(target_path)
        self.overwrite = overwrite
        self.logger = get_logger(self.__class__.__name__)

    def execute(self, context: Context) -> str:
        self.logger.info("Copie de %s vers %s", self.source_path, self.target_path)

        if not self.source_path.exists():
            raise FileNotFoundError(f"Source file not found: {self.source_path}")

        if self.target_path.exists() and not self.overwrite:
            raise FileExistsError(f"Target already exists: {self.target_path}")

        self.target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(self.source_path, self.target_path)

        self.logger.info("Copie terminée avec succès.")
        return str(self.target_path)
