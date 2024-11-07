"""This module defines the PlayingCard class."""

__author__ = "Damien Altenburg"
__version__ = "0.11.2024"

from playing_card.rank import Rank
from playing_card.suit import Suit

class PlayingCard:
    """Represents a standard playing card."""

    HIGHEST_RANK: int = Rank.KING.value

    def __init__(self, rank: Rank, suit: Suit):
        """"""
        if not isinstance(rank, Rank):
            raise TypeError("The rank must be a Rank.")
        
        if not isinstance(suit, Suit):
            raise TypeError("The suit must be a Suit.")

        self.__rank = rank
        self.__suit = suit
        self.__is_face_up = False    
    
    @property
    def rank(self) -> Rank:
        return self.__rank
    
    @rank.setter
    def rank(self, rank: Rank) -> None:
        if not isinstance(rank, Rank):
            raise TypeError("The rank must be a Rank.")

        self.__rank = rank

    @property
    def suit(self) -> Suit:
        return self.__suit
    
    @suit.setter
    def suit(self, suit: Suit) -> None:
        if not isinstance(suit, Suit):
            raise TypeError("The suit must be a Suit.")

        self.__suit = suit

    @property
    def is_face_up(self) -> bool:
        return self.__is_face_up
    
    # TODO:
    # Behavior to determine if the card is a face card.

    def flip(self) -> None:
        self.__is_face_up = not self.__is_face_up

    def __repr__(self) -> str:
        return f"PlayingCard({self.__rank}, {self.__suit})"
    
    def __str__(self) -> str:
        # TODO:
        # Represent the card in different ways depending on whether
        # it's face up or not.
        return f"{self.__rank.name.title()} {self.__suit.name.title()}"
