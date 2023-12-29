import pytest
from seasons import get_timedelta, int2str


def test_get_timedelta():
    with pytest.raises(SystemExit):
        get_timedelta("Dec 07, 1993")


def test_int2str():
    assert int2str(100) == "One hundred"
    assert int2str(101) == "One hundred one"
    assert int2str(365101) == "Three hundred sixty-five thousand, one hundred one"