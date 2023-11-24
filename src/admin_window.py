from kivy.properties import DictProperty
from kivy.uix.screenmanager import Screen

from db import insert_words

class AdminWindow(Screen):
    data = DictProperty({})

    __events__ = ('on_save',)

    def edit(self, data=None):
        if data is not None:
            self.data = data
        else:
            self.data = {}

    def clear_input(self):
        for value in self.ids.values():
            value.text = ""
    
    def validate_input(self, data):
        try:
            return data['word'] and data['answer'] and data['written']     
        except Exception:
            return False
            
    def on_save(self, data):
        print(data)
        if self.validate_input(data):
            insert_words(data['word'], data['answer'], data['written'])
        else:
            print("Validation Error")
        self.clear_input()
