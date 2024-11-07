"""This module is used to demonstrate using a class."""

__author__ = "Damien Altenburg"
__version__ = "0.11.2024"

from playing_card.playing_card import PlayingCard
from playing_card.rank import Rank
from playing_card.suit import Suit

def main():
    # ref_var = Constructor([arg])
    #card = PlayingCard(1, "Heart")
    card = PlayingCard(Rank.ACE, Suit.HEART)

    print(card) #__str__()

    #print(card.__rank)
    #print(card.__suit)

    print(card.rank)

    #card.rank = 9
    card.rank = Rank.NINE

    print(card.rank)

    print(card.suit)

    #card.suit = "Clubs"
    card.suit = Suit.CLUB

    print(card.suit)

    print(str(card)) # __str__()

    print(repr(card)) # __repr__()

    print(card.is_face_up)

    card.flip()

    print(card.is_face_up)

    card.flip()

    print(card.is_face_up)

    print(PlayingCard.HIGHEST_RANK)

if __name__ == "__main__":
    main()
