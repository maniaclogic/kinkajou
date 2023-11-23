from kivy.properties import DictProperty
from kivy.uix.boxlayout import BoxLayout

from db import insert_words


class AddForm(BoxLayout):
    data = DictProperty({})

    __events__ = ('on_save',)

    def edit(self, data=None):
        if data is not None:
            self.data = data
        else:
            self.data = {}

    def on_save(self, data):
        insert_words(data['word'], data['answer'], data['written'])
