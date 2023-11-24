from random_word import RandomWords
from db import insert_words

def populate_words(count):
    r = RandomWords()
   
    for _ in range(1, count):
        word = r.get_random_word()
        answer = r.get_random_word()
        written = r.get_random_word()
        insert_words(word, answer, written)

if __name__ == '__main__':
    populate_words(15)
