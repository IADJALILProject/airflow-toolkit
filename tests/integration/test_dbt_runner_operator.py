from pathlib import Path

import pytest

try:
    from airflow_toolkit.operators.dbt_runner import DbtRunnerOperator
except Exception:
    pytest.skip(
        "Tests d’intégration DbtRunnerOperator désactivés (Airflow non disponible).",
        allow_module_level=True,
    )


def test_dbt_runner_builds_command(tmp_path: Path) -> None:
    project_dir = tmp_path / "dbt_project"
    project_dir.mkdir()

    op = DbtRunnerOperator(
        task_id="test_dbt",
        project_dir=str(project_dir),
        command="run",
    )

    cmd = op.build_command()

    assert isinstance(cmd, list)
    assert "run" in cmd
