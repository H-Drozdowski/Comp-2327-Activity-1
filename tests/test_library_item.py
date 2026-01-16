"""
Description: Unit tests for the Book class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_library_item.py
"""

import unittest
from genre.genre import Genre
from library_item.library_item import LibraryItem

__author__ = "Hudson Drozdowski"
__version__ = "3.13.7"

class TestLibraryItem(unittest.TestCase):
    """Test for the library item class"""
    
    def test_init_initializes_state(self):
        """Tets if the module is initialized properly when
        entering the correct values."""

        #Arange
        title = "Book_Name"
        author = "Author_Name"
        genre = Genre.FICTION

        #Act
        target = LibraryItem(title, author, genre)

        #Assert
        #Checks that all the instance attributes match the inputs.
        self.assertEqual(title, target.title)
        self.assertEqual(author, target.author)
        self.assertEqual(genre, target.genre)

        
    def test_init_exception_when_title_is_blank(self):
        """Tests if the propper exception is raised
        when title is blank"""

        #Arange
        #These variables will be input into an instance of LibraryItem
        #to test for a ValueError when the title is set blank.
        title = " "
        author = "Author Name"
        genre = Genre.NON_FICTION

        #Act
        #Test fails if a ValueError is not raised when target is initialized.
        with self.assertRaises(ValueError) as exception_context:
            target = LibraryItem(title, author, genre)

        #Assert
        expected = "Title cannot be blank."
        actual = str(exception_context.exception)

        #If the expected and the exception raised match the test passes.
        self.assertEqual(expected, actual)


    def test_init_exception_when_author_is_blank(self):
        """Tests if the propper exception is raised
        when author is blank"""

        #Arange
        #These variables will be input into an instance of LibraryItem
        #to test for a ValueError when the author is set blank.
        title = "Book_Name"
        author = " "
        genre = Genre.TRUE_CRIME

        #Act
        #Test fails if a ValueError is not raised when target is initialized.
        with self.assertRaises(ValueError) as exception_context:
            target = LibraryItem(title, author, genre)

        #Assert
        expected = "Author cannot be blank."
        actual = str(exception_context.exception)

        #If the expected and the exception raised match, the test passes.
        self.assertEqual(expected, actual)

    def test_init_exception_when_invalid_genre(self):
        """Tests if the propper exception is raised
        when genre is invalid/not the correct input"""
        #Arange
        #These variables will be input into an instance of LibraryItem
        #to test for a ValueError when the genre is set to an invalid
        #value.
        title = "Book Name"
        author = "Author Name"
        genre = "This is wrong"
        
        #Act
        #Test fails if a ValueError is not raised when target is initialized.
        with self.assertRaises(ValueError) as exception_context:
            target = LibraryItem(title, author, genre)

        #Assert
        expected = "Invalid Genre."
        actual = str(exception_context.exception)

        #If the expected and the exception raised match, the test passes.
        self.assertEqual(expected, actual)


    def test_title_returns_current_state(self):
        """Tests if title returns the current state correctly"""
        #Arrange
        #Variables used to create a the target instance with correct values.
        title = "Book Name"
        author = "Author Name"
        genre = Genre.FICTION
        target = LibraryItem(title, author, genre)

        #Act

        #Assert
        #If the expected is the same as target.title the test passes.
        expected = title
        self.assertEqual(expected, target.title)


    def test_author_returns_current_state(self):
        """Tests if author returns the current state correctly"""
        #Arrange
        #Variables used to create a the target instance with correct values.
        title = "Book Name"
        author = "Author Name"
        genre = Genre.FICTION
        target = LibraryItem(title, author, genre)

        #Act

        #Assert
        #If the expected is the same as target.author the test passes.
        expected = author
        self.assertEqual(expected, target.author)


    def test_genre_returns_current_state(self):
        """Tests if genre returns the current state correctly"""
        #Arrange
        #Variables used to create a the target instance with correct values.
        title = "Book Name"
        author = "Author Name"
        genre = Genre.FICTION
        target = LibraryItem(title, author, genre)

        #Act

        #Assert
        #if the expected is the same as target.genre the test passes.
        expected = genre
        self.assertEqual(expected, target.genre)


