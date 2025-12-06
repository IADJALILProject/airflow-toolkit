from pathlib import Path

from airflow_toolkit.utils.env_utils import load_env_config


def test_load_env_config_reads_yaml(tmp_path: Path):
    cfg = tmp_path / "env_dev.yaml"
    cfg.write_text("answer: 42\n", encoding="utf-8")

    result = load_env_config(env="dev", base_dir=tmp_path)
    assert result["answer"] == 42
