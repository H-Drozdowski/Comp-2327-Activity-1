"""
Description: Unit tests for the Book class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_library_item.py
"""
__author__ = "Hudson Drozdowski"
__version__ = "3.13.7"

import unittest
from genre.genre import Genre
from library_item.library_item import LibraryItem

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
        #These variables will be input into an instance of LibraryItem
        #to test for a ValueError when the genre is set to an invalid
        #value.
        
        #Arange

        title = "Book Name"
        author = "Author Name"
        genre = "This is wrong"
        
        #Act
        with self.assertRaises(ValueError) as exception_context:
            target = LibraryItem(title, author, genre)

        #Assert
        expected = "Invalid Genre."
        actual = str(exception_context.exception)

        #If the expected and the exception raised match, the test passes.
        self.assertEqual(expected, actual)


# def test_init_library_item_initialized() -> None:
#     #Setup

#     title = "Book Name"
#     author = "Author Name"
#     genre = Genre.FICTION

#     #Invoke
#     library_item = LibraryItem(title, author, genre)

#     #Verify
#     expected = "Book Name"
#     actual = library_item.title

#     print(f"Expected: {expected}")
#     print(f"Actual: {actual}\n")

#     expected = "Author Name"
#     actual = library_item.author

#     print(f"Expected: {expected}")
#     print(f"Actual: {actual}\n")

#     expected = "FICTION"
#     actual = library_item.genre

#     print(f"Expected: {expected}")
#     print(f"Actual: {actual}\n")


