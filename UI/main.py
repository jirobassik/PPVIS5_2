from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
Window.size = (350, 600)

class RegScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class SettingScreen(Screen):
    pass

class ChangepassScreen(Screen):
    pass

class ViewCreateTestScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(RegScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(SettingScreen(name='settings'))
sm.add_widget(ChangepassScreen(name='changepass'))
sm.add_widget(ViewCreateTestScreen(name='create_tests'))

class Myapp(MDApp):
    def build(self):
        return

Myapp().run()