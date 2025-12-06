from __future__ import annotations

from datetime import datetime, timedelta, timezone


def utc_now() -> datetime:
    """
    Retourne la date/heure actuelle en UTC (timezone-aware).
    """
    return datetime.now(timezone.utc)


def days_ago(days: int) -> datetime:
    """
    Retourne la date/heure UTC il y a `days` jours.
    """
    return utc_now() - timedelta(days=days)
