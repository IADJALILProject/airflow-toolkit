# ruff: noqa: E402

import pytest

pytest.skip(
    "Tests d’intégration Airflow (HttpToFilesystemOperator) désactivés par défaut sur "
    "l’environnement local / CI sans stack Airflow complète.",
    allow_module_level=True,
)

from pathlib import Path

from airflow_toolkit.operators.http_to_filesystem import HttpToFilesystemOperator


def test_http_to_filesystem_operator_has_basic_attrs(tmp_path: Path) -> None:
    """Vérifie que l'opérateur HTTP->FS accepte les paramètres de base."""
    dst = tmp_path / "dst"
    dst.mkdir()

    op = HttpToFilesystemOperator(
        task_id="test_http_to_filesystem",
        endpoint="/test",
        destination=str(dst),
    )

    assert op.task_id == "test_http_to_filesystem"
