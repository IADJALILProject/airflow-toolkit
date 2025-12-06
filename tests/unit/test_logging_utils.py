from airflow_toolkit.utils.logging_utils import get_logger


def test_logger_creation():
    logger = get_logger("test_logger")
    logger.info("hello from test")
    assert logger.name == "test_logger"
