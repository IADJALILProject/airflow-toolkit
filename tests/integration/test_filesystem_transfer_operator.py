from pathlib import Path

import pytest

try:
    from airflow_toolkit.operators.filesystem_transfer import (
        FilesystemTransferOperator,
    )
except Exception:
    pytest.skip(
        "Tests d’intégration FilesystemTransferOperator désactivés (Airflow non disponible).",
        allow_module_level=True,
    )


def test_filesystem_transfer_operator_has_basic_attrs(tmp_path: Path) -> None:
    src = tmp_path / "src"
    dst = tmp_path / "dst"
    src.mkdir()
    dst.mkdir()

    op = FilesystemTransferOperator(
        task_id="test_filesystem_transfer",
        source=str(src),
        destination=str(dst),
    )

    assert op.task_id == "test_filesystem_transfer"
