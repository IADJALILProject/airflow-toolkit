from __future__ import annotations

from typing import Any, Dict


def slack_failure_alert(context: Dict[str, Any]) -> None:
    """
    Callback générique pour envoyer une alerte en cas d'échec de tâche.

    Dans cette V1 open source, on se contente d'écrire sur stdout.
    Dans une vraie implémentation, on intégrerait :
    - Slack Webhook
    - Teams
    - Email
    etc.
    """
    task_id = context["task_instance"].task_id
    dag_id = context["dag"].dag_id
    execution_date = context["ts"]

    print(
        f"[ALERT] Task failed - DAG: {dag_id}, Task: {task_id}, "
        f"Execution date: {execution_date}"
    )
