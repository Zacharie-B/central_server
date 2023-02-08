from use_case.file_manager import FileManager
from controller.applicative_protocol import ApplicativeProtocol


def test_create_local_server():
    a = 1
    app_pro = ApplicativeProtocol()
    app_pro.sortInputMessage('4001 fiche de paie,fiche de paie de Zacharie '
                             'Baril;'
                             'rapport SDN,rapport sur la technologie SDN pour " \
                            "automatiser les réseaux', 5100, '127.0.0.1')
    assert a
