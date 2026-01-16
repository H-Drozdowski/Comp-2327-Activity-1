""""
Description: An enumeration containing valid Genres.
"""

from enum import Enum

__author__ = "Hudson Drozdowski"
__version__ = "3.13.7"

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
