"""This module defines the Rank enumeration."""

__author__ = "Damien Altenburg"
__version__ = "0.11.2024"

from enum import Enum

class Rank(Enum):
    """Represents a rank for a standard playing card."""
    
    ACE = 1
    """The ace rank."""
    
    TWO = 2
    """The two rank."""    
    
    THREE = 3
    """The three rank."""    
    
    FOUR = 4
    """The four rank."""

    FIVE = 5
    """The five rank."""

    SIX = 6
    """The six rank."""

    SEVEN = 7
    """The seven rank."""

    EIGHT = 8
    """The eight rank."""

    NINE = 9
    """The nine rank."""

    TEN = 10
    """The ten rank."""

    JACK = 11
    """The jack rank."""

    QUEEN = 12
    """The queen rank."""

    KING = 13
    """The king rank."""
