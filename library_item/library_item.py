""""
Description: A class to manage LibraryItem objects.
"""

from genre.genre import Genre

__author__ = "Hudson Drozdowksi"
__version__ = "3.13.7"

class LibraryItem:

    def __init__(self, title : str, author : str, genre : Genre):
        """
        Initializes a new instance of the LibraryItem class.

        args:
            title (str): The title of the library item
            author (str): The title of the author of the library item
            genre: (Genre): The genre of the library item
        """

        #If the length of the title is empty raises a ValueError
        if len(title.strip()) == 0:
            raise ValueError("Title cannot be blank.")
        
        #If the length of the author name is empty raises a ValueError
        if len(author.strip()) == 0:
            raise ValueError("Adiduthor cannot be blank.")
        
        #If the genre is not in the enum raises a ValueError
        if not isinstance(genre, Genre):
            raise ValueError("Invalid Genre.")

        #Sets the entered attributes 
        self.__title = title
        self.__author = author
        self.__genre = genre


    #Title property
    @property
    def title(self) -> str:
        """gets: the title of the librabary item
        
        returns: the library items title"""
        return self.__title
    
    #Author property
    @property
    def author(self) -> str:
        """gets: the name of the author of the library item
        
        returns: the name of the library items author"""
        return self.__author
    
    #Genre property
    @property
    def genre(self) -> Genre:
        """gets: The Genre of the library item
        
        returns: The genre of the library item"""
        return self.__genre
     