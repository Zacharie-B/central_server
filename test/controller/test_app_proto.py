import pytest
from controller.applicative_protocol import ApplicativeProtocol

app_proto = ApplicativeProtocol()

app_proto.sortInputMessage('4001 fiche de paie,fiche de paie de Zacharie Baril;'
                           'rapport SDN,rapport sur la technologie SDN pour automatiser les '
                           'réseaux', 5100, '127.0.0.1')


def test_sort_code():
    a = "azerty"
    print(app_proto.sortInputMessage("1001 fsdf", 2, 'ee'))
    print(app_proto.sortInputMessage("4001 ezr,az;ae,ar", 2, 'ee'))
    print(app_proto.sortInputMessage("4003 az", 2, 'ee'))
    print(app_proto.sortInputMessage("4005 ezrz,aze", 2, 'ee'))
    assert a


def test_searching():
    result = app_proto.sortInputMessage("4003 a rapport", 2, "ee")
    print(result)
    assert result


def test_create_local_server():
    a = 1
    app_proto.sortInputMessage('4001 fiche de paie,fiche de paie de Zacharie Baril;'
                               'rapport SDN,rapport sur la technologie SDN pour automatiser les '
                               'réseaux', 5100, '127.0.0.1')
    assert a


def test_new_file():
    a = 1
    result = app_proto.sortInputMessage('4005 rapport,rapport sur les éléphants',  5100, '127.0.0.1')
    print(result)
    assert a