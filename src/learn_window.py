from kivy.uix.screenmanager import Screen

class LearnWindow(Screen):
    __events__ = ('on_pick_word',)
    def on_pick_word(self, data):
        print("here")
