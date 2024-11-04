"""This module is used to demonstrate using a class."""

__author__ = "Damien Altenburg"
__version__ = "0.11.2024"

from playing_card.playing_card import PlayingCard

def main():
    # ref_var = Constructor([arg])
    card = PlayingCard(1, "Heart")

    print(card)

    #print(card.__rank)
    #print(card.__suit)

if __name__ == "__main__":
    main()
