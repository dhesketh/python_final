#!/usr/bin/env python3

# import functions from db file
from db import get_patron, patron_exists, get_books_by_user, get_library_books, book_exists, checkout_book, checkin_book, checkin_all_books, is_book_available

# function to validate if the patron exists, and is not userID 1 which is the library
def validate_patron(user_id):
    if not patron_exists(user_id):
        print("\nInvalid Patron ID.")
        return False
    if user_id == 1:
        print("\nInvalid UserID. The library cannot be used as a patron.")
        return False
    return True

# function to validate if the bookID exists, and if book is in library and available
def validate_book(book_id):
    if not book_exists(book_id):
        print("\nInvalid Book ID.")
        return False
    if not is_book_available(book_id):
        print("\nThe book is not available for checkout.")
        return False
    return True

# function to call the validation functions and if the pass, then check out the book
def check_out_book(user_id, book_id):
    if not validate_patron(user_id):
        return
    if not validate_book(book_id):
        return

    checkout_book(user_id, book_id)
    print(f"\nBook {book_id} successfully checked out to user {user_id}.")

# function to validate the bookID and then check in the book
def check_in_book(book_id):
    if not book_exists(book_id):
        print("\nInvalid Book ID.")
        return

    checkin_book(book_id)
    print(f"\nBook {book_id} successfully checked in.")

# function to display the books a user has checked out
def display_user_books(user_id):
    if user_id == 1:
        print("\nInvalid UserID. The library cannot be used as a patron.")
        return

    patron = get_patron(user_id)
    if not patron:
        print("\nPatron not found.")
        return

    print(f"\nName: {patron['name']}")
    books = get_books_by_user(user_id)
    if not books:
        print("\nNo books checked out.")
    else:
        for book in books:
            print(f"\nBookID: {book['bookID']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")

# function to display the books in the library available for checkout
def display_library_books():
    books = get_library_books()
    print("\nBooks currently in the library:")
    if not books:
        print("\nNo books found.")
    else:
        for book in books:
            print(f"BookID: {book['bookID']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")

# function to check in all books/reset
def check_in_all_books():
    checkin_all_books()
    print("\nAll books have been checked in.")
