from typing import NoReturn


class Language:
    """
    Enumeration languages
    """
    def __init__(self):
        self.english = "English"
        self.russian = "Russian"

class Settings:
    def change_mail(self) -> NoReturn:
        """
        Change mail user
        """
        pass

    def change_name(self) -> NoReturn:
        """
        Change name user
        """
        pass

    def change_password(self) -> NoReturn:
        """
        Change password user
        """
        pass

    def change_language(self, language: Language) -> NoReturn:
        """
        Change language system
        """
        pass

