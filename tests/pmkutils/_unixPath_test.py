import pytest

from rcluster.pmkutils import _unixPath

val = "hello/this/is.text"


def test_valid():
    assert _unixPath(val) == val


def test_windows():
    assert _unixPath("hello\\this\\is.text") == val


def test_mix():
    assert _unixPath("hello\\this/is.text") == val


def test_none():
    with pytest.raises(AttributeError) as exc:
        _unixPath(None)
    assert "'NoneType' object has no attribute 'replace'" in str(exc.value)