# Password-Manager-Python

# Password Manager (Python)
## Project Overview

This project is a simple Password Manager built using Python.  
It allows users to store, view, search, and delete account credentials.

All data is stored in a file (`passwords.txt`), making it a basic example of file-based data management.

## Features

- Add new account and password  
- View all stored accounts  
- Search password by account name  
- Delete account  
- Persistent storage using file handling  

## Technologies Used

- Python  
- File Handling  

## How the Program Works

### 1. Add Account

- User enters account name and password  
- Data is stored in file  

Example: gmail,1234

### 2. View Accounts

- Reads all data from file  
- Displays account names and passwords  

Example:
gmail -> 1234
facebook -> abcd

### 3. Search Password

- User enters account name  
- Program searches and displays password  

### 4. Delete Account

- User enters account name  
- Account is removed from file  

### 5. Exit
- Stops the program 

## How to Run

1. Install Python  
2. Save file as `password_manager.py`  
3. Run the program:
python password_manager.py

## Concepts Used:

File handling (read, write, append)
Loops (while, for)
Conditional statements
String manipulation
Searching data in files
Learning Outcomes

## After completing this project, you will learn:

How to store sensitive data in files
How to search and delete records
How to manage structured data using text files
How to build real-world CLI applications

## Possible Improvements:

Hide password while typing
Encrypt passwords for security
Add update/edit password feature
Add login authentication
Build GUI using Tkinter

## Author
Harsha G
Learning Python | Embedded Systems | IoT
