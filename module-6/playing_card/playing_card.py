"""This module defines the PlayingCard class."""

__author__ = "Damien Altenburg"
__version__ = "0.11.2024"

from .rank import Rank
from .suit import Suit

class PlayingCard:
    """Represents a standard playing card."""

    __SUIT_CHARACTERS = {
        'CLUB': '\u2663',
        'SPADE': '\u2660',
        'HEART': '\u2665',
        'DIAMOND': '\u2666'
    }
    """A dict containing the Unicode characters for the suits."""

    def __init__(self, rank: Rank, suit: Suit):
        """Initializes a new instance of the PlayingCard class.
        
        Args:
            rank (Rank): The rank of the PlayingCard.
            suit (Suit): The suit of the PlayingCard.
            
        Raises:
            TypeError: Raised when the rank is not a Rank or the suit
            is not a Suit.
        """
        if not isinstance(rank, Rank):
            raise TypeError("The rank must be a Rank.")
        
        if not isinstance(suit, Suit):
            raise TypeError("The suit must be a Suit.")

        self.__rank = rank
        self.__suit = suit
        self.__is_face_up = False

    @property
    def rank(self) -> Rank:
        """Gets the rank of the PlayingCard.

        Returns:
            Rank: The rank of the PlayingCard.

        Example:
            >>> print(card.rank)
            Rank.ACE
        """
        return self.__rank
    
    @rank.setter
    def rank(self, rank: Rank) -> None:
        """Sets the rank of the PlayingCard.

        Args:
            rank (Rank): The rank of the PlayingCard.

        Raises:
            TypeError: Raised when the rank is not a Rank.

        Example:
            >>> card.rank = Rank.ACE
        """
        if not isinstance(rank, Rank):
            raise TypeError("The rank must be a Rank.")
        
        self.__rank = rank

    @property
    def suit(self) -> Suit:
        """Gets the suit of the PlayingCard.

        Returns:
            Suit: The suit of the PlayingCard.

        Example:
            >>> print(card.suit)
            Suit.HEART
        """
        return self.__suit
    
    @suit.setter
    def suit(self, suit: Suit) -> None:
        """Sets the suit of the PlayingCard.

        Args:
            suit (Suit): The suit of the PlayingCard.

        Raises:
            TypeError: Raised when the suit is not a Suit.

        Example:
            >>> card.suit = Suit.HEART
        """
        if not isinstance(suit, Suit):
            raise TypeError("The suit must be a Suit.")
        
        self.__suit = suit

    @property
    def is_face_up(self) -> bool:
        """Gets whether the PlayingCard is face up or not.

        Returns:
            bool: True when the PlayingCard is face up, otherwise
            False.
        
        Example:
            >>> print(card.is_face_up)
            True
        """
        return self.__is_face_up
    
    def flip(self) -> None:
        """Flips the PlayingCard.

        When the PlayingCard is face up, it will be flipped face down
        and visa versa.

        Example:
            >>> card.flip()
        """
        self.__is_face_up = not self.__is_face_up

    def __is_face_card(self) -> bool:
        """Returns True when the PlayingCard is a face card; 
        otherwise False.
        
        Returns:
            True when the PlayingCard is a face card; otherwise False.
        """
        return self.__rank.value in [11, 12, 13]

    def __repr__(self):
        """Return the canonical string representation of the 
        PlayingCard.

        Returns:
            str: The canonical string representation of the PlayingCard.

        Example:
            >>> repr(card)
            PlayingCard(rank=Rank.ACE, suit=Suit.SPADE)
        """
        return f"PlayingCard({self.__rank}, {self.__suit})"
    
    def __str__(self):
        """Return an informal string representation of the PlayingCard.

        When the PlayingCard is face up, the card's rank and suit are
        returned. When the card is face down, the card's rank and suit 
        are considered hidden and a block character is returned to 
        represent the back of the PlayingCard.

        Returns:
            str: An informal string representation of the PlayingCard.

        Example:
            >>> str(card)
            A♥
        """
        card_string = "\u2593"
        
        if self.__is_face_up:
            rank = self.__rank.name[0] if \
                self.__is_face_card() or self.__rank.value == 1 \
                else self.__rank.value                

            suit = PlayingCard.__SUIT_CHARACTERS[self.__suit.name]

            card_string = f"{rank}{suit}"
        
        return card_string            
    