from user import User
from test import Test
from managers import UserManager, UserManagerGroup, TestManager
from settings import Settings, Language
from UI.UI import Myapp, RegScreen, SettingScreen, ProfileScreen, ChangepassScreen, ViewCreateTestScreen, AddTestScreen, CreateQuestionScreen, EditTestScreen, EditQuestionScreen, AccessTestScreen, PassTestScreen, StartTestScreen, ShowUserScreen


class SystemTesting:
    def start(self):
        self.testinteraction = TestInteraction()
        self.testinteraction.build()


class TestInteraction:
    def build(self):
        self.user = User()
        self.test = Test()
        self.user_manager = UserManager()
        self.user_manager_group = UserManagerGroup()
        self.test_manager = TestManager()
        self.language = Language()
        self.settings = Settings()
        self.view_create = ViewCreateTestScreen()
        self.addtest = AddTestScreen()
        self.create_qustion = CreateQuestionScreen()
        self.edit_test = EditTestScreen()
        self.edit_question = EditQuestionScreen()
        self.access_test = AccessTestScreen()
        self.pass_t = PassTestScreen()
        self.start = StartTestScreen()
        self.show_user = ShowUserScreen()
        self.reg = RegScreen()
        self.set = SettingScreen()
        self.prof = ProfileScreen()
        self.change_pass = ChangepassScreen()
        self.ui = Myapp().run()


app = SystemTesting()
app.start()
