from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.button import MDFlatButton
from typing import NoReturn
from managers import UserManagerGroup
from user import User, Pass_test
from test import Test

Window.size = (350, 600)


class NotifyAddConfirm(TwoLineAvatarIconListItem):
    pass


class ItemConfirm(TwoLineAvatarIconListItem):
    pass


# -------------------------------------------------------------

class RegScreen(Screen):
    def signupForm(self) -> NoReturn:
        pass

    def signIn(self) -> NoReturn:
        pass

    def create_new_account(self) -> NoReturn:
        pass

    def forgot_password(self) -> NoReturn:
        pass


class SettingScreen(Screen):
    def but_change_language(self) -> NoReturn:
        pass

    def form_change_mail(self) -> NoReturn:
        pass

    def form_change_password(self) -> NoReturn:
        pass

    def form_change_name(self) -> NoReturn:
        pass


class ProfileScreen(Screen):
    def show_data_user(self) -> NoReturn:
        pass

    def signOut(self) -> NoReturn:
        pass

    def show_num_create_test(self) -> NoReturn:
        pass

    def show_puss_test(self) -> NoReturn:
        pass

    def settings(self, settings: SettingScreen) -> NoReturn:
        pass


class ChangepassScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.view_create = User()

    def form_change_password(self) -> NoReturn:
        pass

    def confirm(self) -> NoReturn:
        pass


class ViewCreateTestScreen(Screen):
    dialog = None

    def __init__(self, **kw):
        super().__init__(**kw)
        self.view_create = Test()

    def show_share(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Name test",
                type="confirmation",
                items=[
                    ItemConfirm(text="4335345",
                                secondary_text="Callisto"),
                    ItemConfirm(text="4535435",
                                secondary_text="Luna"),
                    ItemConfirm(text="4154356",
                                secondary_text="Night"),
                    ItemConfirm(text="3325567",
                                secondary_text="Solo"),
                    ItemConfirm(text="1345436",
                                secondary_text="Prince"),
                    ItemConfirm(text="1345436",
                                secondary_text="Prince"),
                    ItemConfirm(text="1345436",
                                secondary_text="Prince"),
                    ItemConfirm(text="1345436",
                                secondary_text="Prince"),
                    ItemConfirm(text="1345436",
                                secondary_text="Prince"),
                    ItemConfirm(text="1345436",
                                secondary_text="Prince"),
                    ItemConfirm(text="1345436",
                                secondary_text="Prince"),
                ],
                buttons=[
                    MDFlatButton(
                        text="Add users",
                    ),
                ],
            )
        self.dialog.open()


class AddTestScreen(Screen):
    def form_data(self) -> NoReturn:
        pass

    def check_show_ans(self) -> NoReturn:
        pass

    def checkbox_repeat(self) -> NoReturn:
        pass

    def nextButton(self) -> NoReturn:
        pass


class CreateQuestionScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.create_quest = Test()

    def form_data(self) -> NoReturn:
        pass

    def button_create_another_question(self) -> NoReturn:
        pass

    def delete_ans(self) -> NoReturn:
        pass

    def mark_ans(self) -> NoReturn:
        pass

    def radio_button_check(self) -> NoReturn:
        pass

    def backButton(self) -> NoReturn:
        pass

    def finishButton(self) -> NoReturn:
        pass


class EditTestScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.edit_test = Test()

    def edit_form_data(self) -> NoReturn:
        pass

    def edit_checkbox_show_ans(self) -> NoReturn:
        pass

    def edit_checkbox_repeat(self) -> NoReturn:
        pass

    def next_button(self) -> NoReturn:
        pass


class EditQuestionScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.edit_quest = Test()

    def edit_form_data(self) -> NoReturn:
        pass

    def button_create_another_question(self) -> NoReturn:
        pass

    def delete_ans(self) -> NoReturn:
        pass

    def edit_mark_ans(self) -> NoReturn:
        pass

    def edit_radio_button_check(self) -> NoReturn:
        pass

    def backButton(self) -> NoReturn:
        pass

    def finishButton(self) -> NoReturn:
        pass


class AccessTestScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.accessmodel = Test()

    def access_test(self) -> NoReturn:
        pass

    def view_data(self) -> NoReturn:
        pass


class PassTestScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.pass_test_mod = Pass_test()

    def question(self, test: Test) -> NoReturn:
        pass

    def answers(self, test: Test) -> NoReturn:
        pass


class StartTestScreen(Screen):
    dialog = None

    def __init__(self, **kw):
        super().__init__(**kw)
        self.addmodel = Test()

    def data_test(self, test: Test) -> NoReturn:
        pass

    def start_but(self) -> NoReturn:
        pass

    def show_statistics(self) -> NoReturn:
        if not self.dialog:
            self.dialog = MDDialog(
                title="Statistics",
                text="Number of correct answers: 0\n"
                     "Number of wrong answers: 0",
            )
        self.dialog.open()


class ShowUserScreen(Screen):
    dialog = None

    def __init__(self, **kw):
        super().__init__(**kw)
        self.user = User()
        self.mod_user_integr = UserManagerGroup()

    def search_user(self, user: User) -> str:
        pass

    def add_user(self, user: User) -> NoReturn:
        pass

    def delete_user(self, user: User) -> NoReturn:
        pass

    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Users that want add you to group",
                type="confirmation",
                items=[
                    NotifyAddConfirm(text="4335345",
                                     secondary_text="Callisto"),
                    NotifyAddConfirm(text="4535435",
                                     secondary_text="Luna"),
                    NotifyAddConfirm(text="4154356",
                                     secondary_text="Night"),
                    NotifyAddConfirm(text="3325567",
                                     secondary_text="Solo"),
                    NotifyAddConfirm(text="1345436",
                                     secondary_text="Prince"),
                    NotifyAddConfirm(text="1345436",
                                     secondary_text="Prince"),
                    NotifyAddConfirm(text="1345436",
                                     secondary_text="Prince"),
                    NotifyAddConfirm(text="1345436",
                                     secondary_text="Prince"),
                    NotifyAddConfirm(text="1345436",
                                     secondary_text="Prince"),
                    NotifyAddConfirm(text="1345436",
                                     secondary_text="Prince"),
                    NotifyAddConfirm(text="1345436",
                                     secondary_text="Prince"),
                ],
            )
        self.dialog.open()


sm = ScreenManager()
sm.add_widget(RegScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(SettingScreen(name='settings'))
sm.add_widget(ChangepassScreen(name='changepass'))
sm.add_widget(ViewCreateTestScreen(name='create_tests'))
sm.add_widget(AddTestScreen(name='add_test'))
sm.add_widget(CreateQuestionScreen(name='create_question'))
sm.add_widget(EditTestScreen(name='edit_test'))
sm.add_widget(EditQuestionScreen(name='edit_question'))
sm.add_widget(AccessTestScreen(name='access_tests'))
sm.add_widget(StartTestScreen(name='start_test'))
sm.add_widget(PassTestScreen(name='pass_test'))
sm.add_widget(ShowUserScreen(name='show_user'))


class Myapp(MDApp):
    def build(self):
        return
