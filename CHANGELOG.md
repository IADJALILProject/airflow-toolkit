# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Ce projet suit un versioning sémantique de type `MAJOR.MINOR.PATCH`.

---

## [1.0.0] - 2025-12-07

### Ajouté

- Première version stable de la librairie interne **`airflow-toolkit`**.
- **Operators génériques** :
  - `FilesystemTransferOperator` : copie de fichiers / répertoires entre systèmes de fichiers.
  - `HttpToFilesystemOperator` : téléchargement HTTP(s) vers le filesystem.
  - `DbtRunnerOperator` : exécution de commandes `dbt` (run / test / seed / deps…).
  - `SqlExecuteOperator` : exécution de requêtes SQL génériques (administration, maintenance, dataops).
- **Hooks** :
  - `ClickHouseHook` : connexion et exécution de requêtes sur ClickHouse.
- **Utils** :
  - `logging_utils.get_logger` : logger standardisé pour tous les operators / hooks.
  - `date_utils` : helpers temporels (`utc_now`, `days_ago`).
  - `env_utils.load_env_config` : chargement de fichiers YAML d’environnement (`env_dev.yaml`, etc.).
  - `alerts.slack_failure_alert` : callback générique de notification Slack en cas d’échec de tâche.
- **Configuration qualité** :
  - `pyproject.toml` avec configuration de `ruff`, `black`, `pytest`.
  - Tests unitaires sur les utils (`date_utils`, `logging_utils`, `env_utils`).
  - Tests d’intégration Airflow désactivés par défaut (skipés sur Python 3.12).
- **CI GitHub Actions** :
  - Workflow `.github/workflows/ci.yml` exécutant :
    - `ruff check .`
    - `black --check .`
    - `pytest`

---
