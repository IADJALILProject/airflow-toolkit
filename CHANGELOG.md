# Changelog – airflow-toolkit

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

---

## [1.0.0] – 2025-12-06
### 🎉 Première release stable (v1.0.0)

Cette version introduit la base solide de la librairie interne Airflow utilisée pour écrire des DAGs industriels, reproductibles et maintenables.

#### 🚀 Nouveaux Operators
- **FilesystemTransferOperator**
  - Copie de fichiers source → destination avec validations.
  - Utilisé pour l’ingestion batch (zone raw → staging).

- **HttpToFilesystemOperator**
  - Téléchargement HTTP/API vers le système de fichiers.
  - Support idéal pour ingestion API simple.

- **DbtRunnerOperator**
  - Exécution de commandes `dbt` (run/test/seed/snapshot).
  - Logging enrichi et gestion d’erreurs.

- **SqlExecuteOperator**
  - Exécution SQL générique pour l’admin / maintenance SGBD.
  - Utile pour VACUUM, ANALYZE, indexation, jobs DataOps.

#### 🔌 Nouveaux Hooks
- **ClickHouseHook**
  - Connexion simplifiée à ClickHouse.
  - Méthodes utilitaires pour exécuter queries & ingestions.

#### 🧰 Utilitaires intégrés
- `logging_utils`: logger structuré Airflow interne.
- `date_utils`: helpers (`utc_now()`, `days_ago()`).
- `env_utils`: chargement de configs YAML par environnement.
- `alerts.slack_failure_alert`: callback standard d’alerting Slack.

#### ⚙️ Qualité & Tooling
- Ajout des tests unitaires (pytest).
- Intégration de **ruff** (lint) & **black** (formatage).
- CI GitHub Actions :  
  - lint  
  - format  
  - tests  
  - build package

#### 📦 Packaging
- Passage à un packaging moderne via `pyproject.toml`.
- Compatibilité Python ≥ 3.10 & Airflow ≥ 2.9.

---

## Structure du projet
La librairie est désormais stable et destinée à être consommée par un second repo :
`airflow-project-template` (DAGs métiers + code externe).

---

## [Future]
- v1.1.0 : Sensors, operators cloud, Postgres Admin Operator.
- v1.2.0 : Observabilité avancée, métriques Prometheus.
