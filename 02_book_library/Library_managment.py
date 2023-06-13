"""
Requirement:
1. create a library class
2. display book
3. lend book (who owns the book if not present)
4. add book
5. return book

Library: listofbooks, library_name
dictionary: (books : nameofperson)

create a  main function and run an infinite
while loop asking user for their input

"""
class Library:
    def __init__(self, list, library_name) -> None:
        self.bookOfList = list
        self.library_name = library_name
        self.bookDist = {}

    # display or show all the book to the user 
    def display_book(self):
        print(f'\nWelcome to our library {self.library_name}')
        print(f'\n{"*"*10} BOOK LIST {"*"*10}')
        for book in self.bookOfList:
            print(book)

    def lend_book(self, book_name, user_name):
        if book_name not in self.bookDist:
            self.bookDist[book_name] = user_name
            print('Books database updated! You can take the book')
        else:
            print(f'Book is already taken by {self.user_name}')
            

    def add_book(self, book_name):
        add = self.bookOfList.append(book_name)
        print('book added: ',add)
        print('Book added successfully')

    def return_book(self, book_name):
        if book_name in self.bookDist:
            remove = self.bookDist.pop(book_name)
            print('book removed: ',remove)
            print(f'{book_name} is removed successfully')
        else:
            print('Book is not found')


