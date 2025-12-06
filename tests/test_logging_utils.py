from airflow_toolkit.utils.logging_utils import get_logger


def test_get_logger_returns_logger():
    logger = get_logger("test_logger")
    assert logger is not None
    assert logger.name == "test_logger"
