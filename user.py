from test import Test
from settings import Settings
from typing import NoReturn

class User:
    def __init__(self, name: str = None, id: int = None, num_create_test: int = None,
                 num_pass_test: int = None, login: str = None, password: str = None):
        self.__name: str = name
        self.__id: int = id
        self.__num_create_test: int = num_create_test
        self.__num_pass_test: int = num_pass_test

        self.__pass_data: Pass_data = Pass_data(login, password)
        self.__current_params: Settings = Settings()


class Pass_data:
    def __init__(self, login: str, password: str):
        self.__login: str = login
        self.__password: str = password

class Pass_test:
    def choose(self, test: Test) -> NoReturn:
        """
        Choose test for pass
        """
        pass

    def show_result(self, test: Test) -> str:
        """
        Show result test
        """
        pass
