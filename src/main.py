from kivy.app import App
from db import setup_db
from kivy.lang import Builder
from window_manager import WindowManager
from admin_window import AdminWindow
from learn_window import LearnWindow

class KinkajouApp(App):
    def build(self):
        setup_db()


if __name__ == '__main__':
    KinkajouApp().run()
