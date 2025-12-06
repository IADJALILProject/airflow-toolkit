from airflow_toolkit.utils.date_utils import days_ago, utc_now


def test_utc_now_has_timezone():
    now = utc_now()
    assert now.tzinfo is not None


def test_days_ago_returns_correct_date():
    now = utc_now()
    three_days_ago = days_ago(3)

    delta_days = (now.date() - three_days_ago.date()).days
    assert delta_days == 3
