from airflow_toolkit.utils.date_utils import utc_now, days_ago


def test_utc_now_is_timezone_aware():
    now = utc_now()
    assert now.tzinfo is not None


def test_days_ago_is_in_the_past():
    d = days_ago(3)
    now = utc_now()
    assert (now - d).days >= 3
