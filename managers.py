from user import User
from test import Test
from typing import NoReturn
from abc import ABC, abstractmethod
from typing import Any


class IUserGroup(ABC):
    """
    Interface
    """
    @abstractmethod
    def search(self, t: Any) -> NoReturn:
        pass

    @abstractmethod
    def add(self, t: Any) -> NoReturn:
        pass

    @abstractmethod
    def delete(self, t: Any) -> NoReturn:
        pass

class IUser(ABC):
    """
    Interface
    """
    @abstractmethod
    def create(self, t: Any) -> NoReturn:
        pass

    @abstractmethod
    def delete(self, t: Any) -> NoReturn:
        pass

    @abstractmethod
    def edit(self, t: Any) -> NoReturn:
        pass


class UserManager(IUser):
    def __init__(self, user=None):
        self.__manager = user

    def create(self, user: User) -> NoReturn:
        """
        Create new user
        """
        pass

    def delete(self, user: User) -> NoReturn:
        """
        Delete user
        """
        pass

    def edit(self, user: User) -> NoReturn:
        """
        Edit data user
        """
        pass

    def signout(self) -> NoReturn:
        """
        Sign out from system
        """
        pass


class TestManager(IUser):
    def __init__(self, owner=None, testee=None):
        self.__owner = owner
        self.__testee = testee

    def create(self, test: Test) -> NoReturn:
        """
        Create new test
        """
        pass

    def edit(self, test: Test) -> NoReturn:
        """
        Edit data test
        """
        pass

    def delete(self, test: Test) -> NoReturn:
        """
        Delete test
        """
        pass

    def sharetest(self, test: Test, user: User) -> NoReturn:
        """
        Share test with other users
        """
        pass


class UserManagerGroup(IUserGroup):
    def __init__(self, group_user=None, admin=None):
        self.__group_user = group_user
        self.__admin = admin

    def search(self, user: User) -> str:
        """
        Search user
        """
        pass

    def add(self, user: User) -> NoReturn:
        """
        Add new user to group
        """
        pass

    def delete(self, user: User) -> NoReturn:
        """
        Delete user from the group
        """
        pass

    def accept_request(self) -> NoReturn:
        """
        Accept request from the user
        """
        pass

    def decline_request(self) -> NoReturn:
        """
        Decline request from the user
        """
        pass
