from src.db import select_cards
from src.card import Card

def test_load_10_new_cards_when_level_0():
    # When
    result = select_cards(level=0, count=2)

    # Then
    assert len(result) == 2
    assert isinstance(result, list)
    assert isinstance(result[0], Card)
