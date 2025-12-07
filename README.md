# airflow-toolkit

Librairie interne d’**operators**, **hooks** et **utilitaires** pour [Apache Airflow](https://airflow.apache.org/).

Objectif : factoriser le code récurrent (ingestion fichiers, HTTP, SQL, dbt, logging, config…) dans une
lib Python réutilisable entre plusieurs projets Airflow (data engineering, dataops, administration BD).

Version actuelle : **1.0.0**

---

## 1. Fonctionnalités

### 🧩 Operators
- `FilesystemTransferOperator` → copie de fichiers / dossiers, synchronisation.
- `HttpToFilesystemOperator` → téléchargement HTTP(s) vers le système de fichiers.
- `DbtRunnerOperator` → exécution de commandes `dbt` orchestrées dans Airflow.
- `SqlExecuteOperator` → exécution de requêtes SQL génériques (admin, maintenance, dataops).

### 🔌 Hooks
- `ClickHouseHook` → connexion + exécution de requêtes ClickHouse.

### 🛠️ Utilitaires
- `logging_utils.get_logger` → logger structuré et homogène.
- `date_utils` → helpers temporels (`utc_now`, `days_ago`).
- `env_utils.load_env_config` → chargement YAML par environnement (`env_dev.yaml`, etc.).
- `alerts.slack_failure_alert` → callback Slack en cas d’échec Airflow.

### 🧪 Qualité
- Lint : `ruff`
- Formatage : `black`
- Tests : `pytest`
- CI : GitHub Actions (`ruff` + `black` + `pytest`)

---

## 2. Installation

### 2.1 Installation dans un autre projet Airflow

Dans `pyproject.toml` :

```toml
[project]
dependencies = [
  "apache-airflow>=2.9.0",
  "airflow-toolkit @ git+https://github.com/IADJALILProject/airflow-toolkit.git",
]
```

Ou installation directe :

```bash
pip install "git+https://github.com/IADJALILProject/airflow-toolkit.git"
```

---

## 3. Exemples d’utilisation

### 3.1 Import

```python
from airflow_toolkit.operators import (
    FilesystemTransferOperator,
    HttpToFilesystemOperator,
    DbtRunnerOperator,
    SqlExecuteOperator,
)
from airflow_toolkit.utils import get_logger, slack_failure_alert
```

---

### 3.2 DAG d’ingestion fichiers

```python
from datetime import datetime
from airflow import DAG
from airflow_toolkit.operators import FilesystemTransferOperator

with DAG(
    dag_id="example_filesystem_ingestion",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:
    transfer = FilesystemTransferOperator(
        task_id="copy_raw_to_processed",
        source_path="/data/raw",
        target_path="/data/processed",
    )
```

---

### 3.3 Téléchargement HTTP → filesystem

```python
from datetime import datetime
from airflow import DAG
from airflow_toolkit.operators import HttpToFilesystemOperator

with DAG(
    dag_id="example_http_download",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:
    download = HttpToFilesystemOperator(
        task_id="download_daily_json",
        http_conn_id="my_api",
        endpoint="/v1/data",
        method="GET",
        target_path="/data/raw/api/daily.json",
    )
```

---

### 3.4 Exécution dbt

```python
from datetime import datetime
from airflow import DAG
from airflow_toolkit.operators import DbtRunnerOperator

with DAG(
    dag_id="example_dbt_run",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:
    dbt_run = DbtRunnerOperator(
        task_id="dbt_run_models",
        project_dir="/opt/dbt/project",
        profiles_dir="/opt/dbt/profiles",
        commands=["run", "--select", "tag:daily"],
    )
```

---

### 3.5 Exécution SQL

```python
from datetime import datetime
from airflow import DAG
from airflow_toolkit.operators import SqlExecuteOperator

with DAG(
    dag_id="example_sql_maintenance",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:
    vacuum = SqlExecuteOperator(
        task_id="vacuum_analyze",
        conn_id="postgres_admin",
        sql="VACUUM (VERBOSE, ANALYZE);",
    )
```

---

## 4. Utilitaires

### 4.1 Logger standardisé

```python
from airflow_toolkit.utils import get_logger

logger = get_logger(__name__)
logger.info("Traitement en cours…")
```

---

### 4.2 Dates utilitaires

```python
from airflow_toolkit.utils import utc_now, days_ago

now = utc_now()
three_days = days_ago(3)
```

---

### 4.3 Chargement YAML par environnement

```python
from airflow_toolkit.utils import load_env_config

config = load_env_config(env="dev")
db_url = config["database"]["url"]
```

---

## 5. Développement local

### 5.1 Setup

```bash
git clone https://github.com/IADJALILProject/airflow-toolkit.git
cd airflow-toolkit

python -m venv .venv
source .venv/bin/activate

pip install -e ".[dev]"
```

---

### 5.2 Commandes locales

```bash
ruff check .
black .
pytest
```

---

## 6. Intégration Continue (CI)

Le workflow `.github/workflows/ci.yml` exécute automatiquement :

- `ruff check .`
- `black --check .`
- `pytest`

---

## 7. Versioning & Releases

- Version actuelle : **1.0.0**
- Versioning sémantique : `MAJOR.MINOR.PATCH`
- Historique des changements : `CHANGELOG.md`

---

## 8. Auteur

**Abdeldjalil Salah-Bey**  
