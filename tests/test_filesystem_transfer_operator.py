import pytest

pytest.skip(
    "Tests d’intégration Airflow (operators) désactivés par défaut sur l’environnement local Python 3.12.",
    allow_module_level=True,
)


from pathlib import Path

from airflow_toolkit.operators.filesystem_transfer import FilesystemTransferOperator


def test_filesystem_transfer_operator_copies_file(tmp_path):
    source = tmp_path / "source.txt"
    target = tmp_path / "dest" / "copied.txt"
    source.write_text("hello", encoding="utf-8")

    op = FilesystemTransferOperator(
        task_id="test_copy",
        source_path=str(source),
        target_path=str(target),
        overwrite=True,
    )

    result_path = op.execute(context={})
    assert Path(result_path).exists()
    assert target.read_text(encoding="utf-8") == "hello"
