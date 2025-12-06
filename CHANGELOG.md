# Changelog – Airflow Toolkit

Ce document suit le format **Semantic Versioning (SemVer)** : MAJOR.MINOR.PATCH.

---

## [1.0.0] – 2025-12-06
### 🎉 Version stable initiale

#### 🚀 Added
- `HttpToFilesystemOperator` : téléchargement HTTP → fichier local.
- `FilesystemTransferOperator` : copie/gestion de fichiers locaux.
- `DbtRunnerOperator` : exécution de commandes dbt (run/test/seed).
- `SqlExecuteOperator` : exécution SQL générique via Airflow `BaseHook`.
- `ClickHouseHook` : connexion et exécution de requêtes ClickHouse.
- Module `utils/` :
  - `date_utils` : helpers datetime (`utc_now`, `days_ago`).
  - `logging_utils` : logger structuré Airflow.
  - `env_utils` : chargement automatisé des fichiers de configuration YAML.
  - `alerts` : alerting Slack en cas d'échec de tâche.
- Support Airflow ≥ 2.9.0 & Python 3.10–3.12.
- Structure complète de tests :
  - Tests unitaires (utils)
  - Tests opérateurs (basique)
  - Tests d’intégration (skip si environnement Airflow absent)
- CI GitHub Actions :
  - Ruff (lint)
  - Black (format)
  - Pytest (tests)
  - Check packaging

---

## Historique
→ Première version stable publiée.  
→ Compatible production.

