#!/usr/bin/env python3

# This program manages books for my Little Free Library. It can check them in
# and out, add new books, add new patrons, and display the books a patron has
# and the books the library has available to check out.
# Written by David Hesketh

# import functions from other files
from db import connect, add_patron, add_book
from business import check_out_book, check_in_book, display_user_books, display_library_books, check_in_all_books

# define genres
GENRES = ("Fiction", "Non-Fiction", "Mystery", "Fantasy", "Sci-Fi", "Reference")

# display genres
def display_genres():
    print("\nAvailable genres: ", ", ".join(GENRES))

# check if genre is valid
def get_valid_genre():
    while True:
        genre = input("Enter book genre: ").title()
        if genre in GENRES:
            return genre
        else:
            print("\nInvalid genre. Please choose from the available options.")
            display_genres()

# Menu to display options
def main_menu():
    print("\nLittle Free Library")
    print("1. Check Out Book")
    print("2. Check In Book")
    print("3. View My Books")
    print("4. Add New Patron")
    print("5. Add New Book")
    print("6. Display Library Books")
    print("7. Check In All Books")
    print("8. Exit")

# Main function for user to decide which option they want
def main():
    connect()
    while True:
        main_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            user_id = int(input("Enter your UserID: "))
            book_id = int(input("Enter the BookID to check out: "))
            check_out_book(user_id, book_id)


        elif choice == "2":
            book_id = int(input("Enter the BookID to check in: "))
            check_in_book(book_id)


        elif choice == "3":
            user_id = int(input("Enter your UserID: "))
            display_user_books(user_id)

        elif choice == "4":
            name = input("Enter the name of the new patron: ")
            user_id = add_patron(name)
            print(f"New patron added with UserID: {user_id}")

        elif choice == "5":
            title = input("Enter book title: ").title()
            author = input("Enter book author: ").title()
            display_genres()
            genre = get_valid_genre()
            add_book(title, author, genre)
            print("Book added to the library.")

        elif choice == "6":
            display_library_books()

        elif choice == "7":
            check_in_all_books()

        elif choice == "8":
            print("Bye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
