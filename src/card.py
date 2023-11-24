from dataclasses import dataclass

@dataclass
class Card:
    word: str
    answer: str
    written: str
    level: int

