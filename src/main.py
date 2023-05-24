from kivy.app import App
from add_form import AddForm
from db import setup_db


class KinkajouApp(App):
    def build(self):
        setup_db()
        return AddForm()


if __name__ == '__main__':
    KinkajouApp().run()
