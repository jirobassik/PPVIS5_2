from typing import NoReturn

class Question:
    def __init__(self, id: str, name_q: str, answers: list, onemanyans: bool, id_t: str, name: str, theme: str,
                 time_limit: int, view_cor_ans: bool, reptest: bool, questions: str):
        self.__id: str = id
        self.__name_q: str = name_q
        self.__answers: list = answers
        self.__onemanyans: bool = onemanyans

        self.__test: Test = Test(id_t, name, theme, time_limit, view_cor_ans, reptest, questions)

    def create_ans(self) -> NoReturn:
        """
        Create another answer
        """
        pass


class Test:
    def __init__(self, id: str = None, name: str = None, theme: str = None, time_limit: int = None,
                 view_cor_ans: bool = None, reptest: bool = None, questions: str = None):
        self.__id: str = id
        self.__name: str = name
        self.__theme: str = theme
        self.__time_limit: int = time_limit
        self.__view_cor_ans: bool = view_cor_ans
        self.__reptest: bool = reptest
        self.__questions: str = questions

    def create_question(self, question: Question) -> NoReturn:
        """
        Create new question
        """
        pass

    def delete_question(self, question: Question) -> NoReturn:
        """
        delete new question
        """
        pass

    def calc_result(self) -> NoReturn:
        """
        Calculate test result
        """
        pass
