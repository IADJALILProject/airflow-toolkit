# ruff: noqa: E402

import pytest

pytest.skip(
    "Tests d’intégration Airflow (FilesystemTransferOperator) désactivés par défaut sur "
    "l’environnement local / CI sans stack Airflow complète.",
    allow_module_level=True,
)

from pathlib import Path

from airflow_toolkit.operators.filesystem_transfer import FilesystemTransferOperator


def test_filesystem_transfer_operator_has_basic_attrs(tmp_path: Path) -> None:
    """Vérifie que l'opérateur accepte les paramètres de base."""
    src = tmp_path / "src"
    dst = tmp_path / "dst"
    src.mkdir()
    dst.mkdir()

    op = FilesystemTransferOperator(
        task_id="test_filesystem_transfer",
        source_path=str(src),
        target_path=str(dst),
    )

    assert op.task_id == "test_filesystem_transfer"
