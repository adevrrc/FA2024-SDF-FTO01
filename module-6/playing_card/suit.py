"""This module defines the Suit enumeration."""

__author__ = "Damien Altenburg"
__version__ = "0.11.2024"

from enum import Enum

class Suit(Enum):
    """Represents a suit for a standard playing card."""
    
    HEART = 1
    """The heart suit."""
    
    DIAMOND = 2
    """The diamond suit."""    
    
    SPADE = 3
    """The spade suit."""    
    
    CLUB = 4
    """The club suit."""
