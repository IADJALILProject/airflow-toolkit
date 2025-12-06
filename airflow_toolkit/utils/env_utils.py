from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict

import yaml


def load_env_config(
    env: str | None = None,
    base_dir: str | Path | None = None,
) -> Dict[str, Any]:
    """
    Charge un fichier de configuration YAML en fonction de l'environnement demandé.

    - `env` : dev / preprod / prod / etc.
      Si None, on lit la variable d'env `AIRFLOW_TOOLKIT_ENV` (par défaut: "dev").

    - `base_dir` : dossier contenant les fichiers YAML.
      Si None, on prend `airflow_toolkit/config`.

    Exemple de fichier attendu : `env_dev.yaml`, `env_preprod.yaml`, etc.
    """
    resolved_env = env or os.getenv("AIRFLOW_TOOLKIT_ENV", "dev")
    if base_dir is None:
        base_dir = Path(__file__).resolve().parent.parent / "config"
    else:
        base_dir = Path(base_dir)

    filename = base_dir / f"env_{resolved_env}.yaml"
    if not filename.exists():
        raise FileNotFoundError(f"Config file not found for env '{resolved_env}': {filename}")

    with filename.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}
