""""
Description: A client program written to verify correctness of 
the activity classes.
"""

from library_item.library_item import LibraryItem
from genre.genre import Genre

__author__ = "Hudson Drozdowksi"
__version__ = "3.13.7"

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates an instance of the LibraryItem class with valid inputs.
    # Use your own unique valid values for the inputs to the class.

    valid_library_item = LibraryItem(1, "Valid Title", "Valid Author", Genre.FICTION, False)

    # 2. Using the instance defined above, and the class Accessors, print 
    # each of the attributes of the LibraryItem instance.

    #Prints all the atributes of valid_library_item

    print(valid_library_item.item_id)
    print(valid_library_item.author)
    print(valid_library_item.title)
    print(valid_library_item.genre)
    print(valid_library_item.is_barrowed)

    # 3. Code a statement which creates an instance of the LibraryItem class with one or more invalid inputs.
    # Use your own unique valid values for the inputs to the class.

    #trys to create the instance with the error.
    try:
        invalid_library_item = LibraryItem(1, "Book Title", " ", Genre.FANTASY, True)

    #after trying above if theres a value error its printed to the terminal.
    except ValueError as exception:
        print(exception)


if __name__ == "__main__":
    main()