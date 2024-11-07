"""This module defines the tests for the PlayingCard class."""

__author__ = "Damien Altenburg"
__version__ = "0.11.2024"

import unittest
from playing_card.playing_card import PlayingCard
from playing_card.rank import Rank
from playing_card.suit import Suit

class TestPlayingCard(unittest.TestCase):
    """Defines the unit tests for the PlayingCard class."""

    def test_init_rank_is_not_a_Rank(self):
        # Arrange
        rank = "Rank.JACK"
        suit = Suit.CLUB

        # Act
        with self.assertRaises(TypeError) as context:
            card = PlayingCard(rank, suit)

        # Assert
        expected = "The rank must be a Rank."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_initialize_a_playing_card(self):
        # Arrange
        rank = Rank.JACK
        suit = Suit.CLUB

        # Act
        card = PlayingCard(rank, suit)

        # Assert
        expected_rank = Rank.JACK
        expected_suit = Suit.CLUB
        expected_is_face_up = False

        self.assertEqual(expected_rank, card._PlayingCard__rank)

        # WRONG
        # self.assertEqual(expected_rank, card.__rank) # AttributeError
        # self.assertEqual(expected_rank, card.rank) # Not isolating
        
        self.assertEqual(expected_suit, card._PlayingCard__suit)
        self.assertEqual(expected_is_face_up, card._PlayingCard__is_face_up)

    ### suit Property

    def test_suit_returns_current_state(self):
        # Arrange
        rank = Rank.JACK
        suit = Suit.CLUB

        card = PlayingCard(rank, suit)

        # Act
        actual = card.suit

        # Assert
        expected = Suit.CLUB
        self.assertEqual(expected, actual)

    def test_suit_raise_TypeError_suit_not_a_Suit(self):
        # Arrange
        rank = Rank.JACK
        suit = Suit.CLUB

        card = PlayingCard(rank, suit)

        # Act
        with self.assertRaises(TypeError) as context:
            card.suit = "Suit.CLUB"

        # Assert
        expected = "The suit must be a Suit."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_suit_modifies_the_state(self):
        # Arrange
        rank = Rank.JACK
        suit = Suit.CLUB

        card = PlayingCard(rank, suit)

        # Act
        card.suit = Suit.HEART

        # Assert
        expected = Suit.HEART
        actual = card._PlayingCard__suit
        self.assertEqual(expected, actual)

    ### flip()

    def test_flip_starts_off_face_down(self):
        # Arrange
        rank = Rank.JACK
        suit = Suit.CLUB

        card = PlayingCard(rank, suit)

        # Act
        card.flip()

        # Assert
        #expected = True
        actual = card._PlayingCard__is_face_up
        #self.assertEqual(expected, actual)
        self.assertTrue(actual)

    def test_flip_modified_to_face_down(self):
        # Arrange
        rank = Rank.JACK
        suit = Suit.CLUB

        card = PlayingCard(rank, suit)

        # wRONG
        #card.flip()
        card._PlayingCard__is_face_up = True

        # Act
        card.flip()

        # Assert
        actual = card._PlayingCard__is_face_up
        self.assertFalse(actual)

    ### __repr__()

    def test_repr_returns_string_representation(self):
        # Arrange
        rank = Rank.JACK
        suit = Suit.CLUB

        card = PlayingCard(rank, suit)

        # Act
        actual = card.__repr__()

        # Assert
        expected = "PlayingCard(Rank.JACK, Suit.CLUB)"
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()