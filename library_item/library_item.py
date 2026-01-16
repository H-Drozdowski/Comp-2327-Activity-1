""""
Description: A class to manage LibraryItem objects.
"""

from genre.genre import Genre

__author__ = "Hudson Drozdowksi"
__version__ = "3.13.7"

class LibraryItem:

    def __init__(self, item_id : int, title : str, author : str, genre : Genre, is_borrowed : bool):
        """
        Initializes a new instance of the LibraryItem class.

        args:
            item_id (int): The id representing the library item
            title (str): The title of the library item
            author (str): The title of the author of the library item
            genre (Genre): The genre of the library item
            is_barrowed (bool): represents if the item is barrowed or not
        """

        #If item id is not an int raises a ValueError
        if not isinstance(item_id, int):
            raise ValueError("Item Id must be numeric.")

        #If the length of the title is empty raises a ValueError
        if len(title.strip()) == 0:
            raise ValueError("Title cannot be blank.")
        
        #If the length of the author name is empty raises a ValueError
        if len(author.strip()) == 0:
            raise ValueError("Author cannot be blank.")
        
        #If the genre is not in the enum raises a ValueError
        if not isinstance(genre, Genre):
            raise ValueError("Invalid Genre.")

        #If is barrowed is not a bool raises a ValueError
        if not isinstance(is_borrowed, bool):
            raise ValueError("Is Barrowed must be a boolean value.")

        #Sets the entered attributes 
        self.__item_id = item_id
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__is_borrowed = is_borrowed

    #Item Id accessor
    @property
    def item_id(self) -> int:
        """gets: the library items item id
        
        returns: the items id"""

        return self.__item_id

    #Title accessor
    @property
    def title(self) -> str:
        """gets: the title of the librabary item
        
        returns: the library items title"""
        return self.__title
    
    #Author accessor
    @property
    def author(self) -> str:
        """gets: the name of the author of the library item
        
        returns: the name of the library items author"""
        return self.__author
    
    #Genre accessor
    @property
    def genre(self) -> Genre:
        """gets: The Genre of the library item
        
        returns: The genre of the library item"""
        return self.__genre
     
    #Is Barrowed acessor
    @property
    def is_barrowed(self) -> bool:
        """gets: The value of the bool is_barrowed
        
        returns: The value of the bool is_barrowed"""
        return self.__is_borrowed