from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class Kinkajou(Widget):
    pass


class KinkajouApp(App):
    def build(self):
        return Kinkajou()


if __name__ == '__main__':
    KinkajouApp().run()
