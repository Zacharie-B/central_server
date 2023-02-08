import pytest
from controller.applicative_protocol import ApplicativeProtocol

app_proto = ApplicativeProtocol()


def test_sort_code():
    a = "azerty"
    app_proto.sortInputMessage("1001 fsdf")
    app_proto.sortInputMessage("4001 erz")
    app_proto.sortInputMessage("4003 ezr")
    app_proto.sortInputMessage("4005 ezrz")
    assert a


def test_searching():
    result = app_proto.sortInputMessage("4003 rapport moteur")
    assert result
