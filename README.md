# Airflow Toolkit

**Airflow Toolkit** est une librairie interne d’opérateurs, hooks et utilitaires destinée à
standardiser et accélérer le développement de pipelines Airflow en production.

Elle fournit :

- Des opérateurs robustes (HTTP → fichier, transfert local, SQL générique, dbt).
- Des hooks pour interagir avec des moteurs externes (ClickHouse).
- Des utilitaires transverses : logging, gestion d’environnements, dates, alerting.
- Une base solide pour construire un framework interne Airflow.

---

## 🔧 Installation

### Depuis GitHub (recommandé pour usage interne) :

```bash
pip install git+https://github.com/IADJALILProject/airflow-toolkit.git@v1.0.0
