""""
Description: A class to manage LibraryItem objects.
"""

from genre.genre import Genre

__author__ = "Hudson Drozdowksi"
__version__ = "3.13.7"

class LibraryItem:

    def __init__(self, title : str, author : str, genre : Genre):
        """
        Docstring for __init__
        
        :param self: Description
        :param title: The title of the library item
        :type title: str
        :param author: The author of the library item
        :type author: str
        :param genre: The genre of the library item
        :type genre: Genre
        """

        #If the length of the title is empty raises a ValueError
        if len(title.strip()) == 0:
            raise ValueError("Title cannot be blank.")
        
        #If the length of the author name is empty raises a ValueError
        if len(author.strip()) == 0:
            raise ValueError("Title cannot be blank.")
        
        #If the genre is not in the enum raises a ValueError
        if genre not in Genre:
            raise ValueError("Invalid Genre")

        self.__title = title

        self.__author = author

        self.__genre = genre


    @property
    def title(self) -> str:
        return self.__title
    
    @property
    def author(self) -> str:
        return self.__author
    
    @property
    def genre(self) -> Genre:
        return self.__genre
     