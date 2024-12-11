#!/usr/bin/env python3

# import sqlite3 and closing 
import sqlite3
from contextlib import closing

conn = None

# function to conect to database
def connect():
    global conn
    if not conn:
        DB_FILE = "final.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        
# function to query userID from database
def get_patron(user_id):
    query = '''SELECT * 
	     FROM patrons 
	     WHERE userID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (user_id,))
        return c.fetchone()

# function to check if patron already exists before adding to database
def patron_exists(user_id):
    query = '''SELECT COUNT(*)
            FROM patrons
            WHERE userID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (user_id,))
        return c.fetchone()[0] > 0

# function to display which books a user has checked out
def get_books_by_user(user_id):
    query = '''SELECT * 
	    FROM books 
            WHERE userID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (user_id,))
        return c.fetchall()

# function to display which books are in the library
def get_library_books():
    query = '''SELECT * 
	    FROM books 
	    WHERE userID = 1'''
    with closing(conn.cursor()) as c:
       	c.execute(query)
       	return c.fetchall()

# function to see if a bookID exists in the database before checking it out
def book_exists(book_id):
    connect()
    query = '''SELECT COUNT(*)
            FROM books
            WHERE bookID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (book_id,))
        return c.fetchone()[0] > 0

#function to check out book
def checkout_book(user_id, book_id):
    query = '''UPDATE books 
               SET userID = ? 
               WHERE bookID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (user_id, book_id))
        conn.commit()

# function to check if a book is available/assigned to 1, the library, before checking out
def is_book_available(book_id):
    query = '''SELECT COUNT(*)
               FROM books
               WHERE bookID = ? AND userID = 1'''
    with closing(conn.cursor()) as c:
        c.execute(query, (book_id,))
        return c.fetchone()[0] > 0

#function to check in a book
def checkin_book(book_id):
    query = '''UPDATE books 
	    SET userID = 1 
	    WHERE bookID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (book_id,))
        conn.commit()

# function to add a patron to the list of userIDs
def add_patron(name):
    query = '''INSERT INTO patrons (name) 
	    VALUES (?)'''
    with closing(conn.cursor()) as c:
        c.execute(query, (name,))
        conn.commit()
        return c.lastrowid

# function to add a book
def add_book(title, author, genre):
    query = '''INSERT INTO books (userID, title, author, genre) 
	    VALUES (1, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(query, (title, author, genre))
        conn.commit()

# function to check in all books from all users/reset back to default
def checkin_all_books():
    query = '''UPDATE books 
               SET userID = 1 
               WHERE userID != 1'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()

# close the database connection
def close():
    if conn:
        conn.close()
