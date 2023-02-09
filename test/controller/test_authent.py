from entities.local_server import LocalServer
from entities.user import User
from use_case.user_manager import UserManager


def test_registering():
    um = UserManager()
    print(um.choice_authent_method(['Mano', 'FSDVDFGOSSZERIùmlù&']))
    print(um.get_users()[0])
    assert um
