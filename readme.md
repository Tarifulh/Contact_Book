Contact Book

A beginner-friendly Python contact management application built to practice core Python concepts and persistent data storage.

Features

Load contacts automatically when the application starts

Display saved contacts

Add new contacts

Search contacts by name

Delete contacts

Save changes permanently to a JSON file

Case-insensitive contact searching

Technologies

Python

JSON

File handling

Lists and dictionaries

Loops and conditional statements

Project Structure

ContactBook/
├── contact_book.py
├── contacts.json
└── README.md

How It Works

The application keeps contacts in a Python list while it is running.

When the program starts, json.load() reads the saved contacts from contacts.json into the Python list.

When a contact is added or deleted, json.dump() writes the updated list back to contacts.json.

contacts.json
     ↓
 json.load()
     ↓
Python list (RAM)
     ↓
Add / Search / Delete
     ↓
 json.dump()
     ↓
contacts.json

How to Run

Make sure Python is installed, then run:

python contact_book.py

Current Status

Working console-based version.

Future Improvements

Refactor repeated code into functions

Add contact editing/updating

Sort contacts alphabetically

Validate phone numbers and empty names

Replace JSON storage with SQLite

Build a graphical user interface

Author- MD TARIFUL HOQUE
