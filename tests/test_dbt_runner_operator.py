import pytest

pytest.skip(
    "Tests d’intégration Airflow (operators) désactivés par défaut sur l’environnement local Python 3.12.",
    allow_module_level=True,
)

from pathlib import Path

from airflow_toolkit.operators.dbt_runner import DbtRunnerOperator


def test_dbt_runner_builds_command(tmp_path: Path):
    project_dir = tmp_path / "dbt_project"
    project_dir.mkdir()

    op = DbtRunnerOperator(
        task_id="test_dbt",
        project_dir=str(project_dir),
        command="run",
        select=["tag:daily"],
        full_refresh=True,
    )

    cmd = op.build_command()
    assert cmd[0] == "dbt"
    assert "run" in cmd
    assert "--select" in cmd
    assert "--full-refresh" in cmd
