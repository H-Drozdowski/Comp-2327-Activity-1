""""
Description: An enumeration containing valid Genres.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from enum import Enum

class Genre(Enum):
    """
    An enumeration listing each of the available genres.
    To use:  Genre.GENRE_NAME.  
    Example: Genre.NON_FICTION
    """
    FICTION = 0
    """The genre is fiction"""

    NON_FICTION = 1
    """The genre is non-fiction"""

    FANTASY = 2
    """The genre is fantasy"""

    TRUE_CRIME = 3
    """The genre is ture crime"""
