"""This module defines the tests for the PlayingCard class."""

__author__ = "Damien Altenburg"
__version__ = "0.11.2024"

import unittest
from playing_card.playing_card import PlayingCard
from playing_card.rank import Rank
from playing_card.suit import Suit

class TestPlayingCard(unittest.TestCase):
    """Defines the unit tests for the PlayingCard class."""

    def test_init_initialize_a_playing_card(self):
        # Arrange
        rank = Rank.JACK
        suit = Suit.CLUB

        # Act
        card = PlayingCard(rank, suit)

        # Assert
        expected_rank = Rank.JACK
        expected_suit = Suit.CLUB
        self.assertEqual(expected_rank, card._PlayingCard__rank)
        self.assertEqual(expected_suit, card._PlayingCard__suit)

if __name__ == "__main__":
    unittest.main()