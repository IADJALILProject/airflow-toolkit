from pathlib import Path

from airflow_toolkit.utils.env_utils import load_env_config


def test_load_env_config_from_yaml(tmp_path):
    config_dir: Path = tmp_path
    config_file = config_dir / "env_dev.yaml"

    config_file.write_text(
        "TEST_KEY: 42\nOTHER_KEY: 'foo'\n",
        encoding="utf-8",
    )

    cfg = load_env_config(env="dev", base_dir=config_dir)

    assert cfg["TEST_KEY"] == 42
    assert cfg["OTHER_KEY"] == "foo"
