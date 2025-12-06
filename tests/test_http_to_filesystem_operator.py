from pathlib import Path

from airflow_toolkit.operators.http_to_filesystem import HttpToFilesystemOperator


class FakeHttpHook:
    def __init__(self, *args, **kwargs):
        pass

    def run(self, endpoint, method="GET", params=None, headers=None, return_json=True, timeout=30):
        return b"dummy-content"


def test_http_to_filesystem_operator_writes_file(monkeypatch, tmp_path: Path):
    target = tmp_path / "output.bin"

    monkeypatch.setattr(
        "airflow_toolkit.operators.http_to_filesystem.HttpJsonHook",
        FakeHttpHook,
    )

    op = HttpToFilesystemOperator(
        task_id="test_http",
        endpoint="/fake",
        target_path=str(target),
    )

    result_path = op.execute(context={})
    assert Path(result_path).exists()
    assert target.read_bytes() == b"dummy-content"
