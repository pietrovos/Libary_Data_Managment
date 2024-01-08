"""
Text-based User Interface Version 1.0 12/4/2022

Program can be reached at :
Team leader: Pietro Adamvoski
Phone: 613-791-4646
E-mail: pietroadamvoski@cmail.carleton.ca

-------------------------------------------------------------------------------------------------------

# Description

This program is a user interface capable of providing the tools necessary to edit or sort a dataset
of the user's choosing. The program is also capable of searchiing for books within the dataset.

-------------------------------------------------------------------------------------------------------

# Installation 

To run  the program, Install Python Version 3.10.1 at https://www.python.org/downloads/ making sure to 
add Python to PATH while in the Python setup window.

-------------------------------------------------------------------------------------------------------

Commands:

When the program is run, the user will be given a list of commands and prompted to select one.

L)
The first priority should be to load a dataset into into the user interface using the command "L". The
user will be prompted to select a file from file explorer. 
Note that none of the programs other functions will not run if there is no dataset loaded or the file type is incorrect.



A) #Prompts the user to add book information and then adds the information as a book to the rest 
R) #Prompts the user to input a Title to remove from the dataset
G) #Prompts the user to input a subcommand
--T) #Returns a list of books matching the inputted title
--R) #Returns a list of books matching the inputted rating
--A) #Returns a list of books matching the inputted Author
--P) #Returns a list of books matching the inputted publisher
--C) #Returns a list of books matching the inputted category

GCT)#Returns all categories for book title

S) #Prompts the user to input a subcommand
--T) #Returns the dataset sorted alphabetically by title 
--R) #Returns the dataset sorted by rating
--P) #Returns the dataset sorted alphabetically by publisher
--A) #Returns the dataset sorted alphabetically by author


-------------------------------------------------------------------------------------------------------

# Credits

Text-Based Interactive User Interface - Matt Turner, KKing Arnie, Pietro Adamvoski, Richard Ofordile

The following authors are credited with creating the listed functions.

Author: KKing Arnie
Functions: add_book()
           remove_book()
           
           User Interface case 1

Author: Richard Ofordile
Functions: get_books_by_author()
           get_books_by_title()
           get_books_by_rate()
           User Interface case 2

Author: Pietro Adamvoski
Functions: get_books_by_publisher()
           get_books_by_category()
           GCT()
           User Interface case 3
           
Author: Matt Turner
Functions: 
           sort_books_title()
           sort_books_rate()
           sort_books_publisher()
           sort_books_author()
           User Interface case 4


           





-------------------------------------------------------------------------------------------------------

# License 

Copyright (c) [2022] [ Matt Turner, KKing Arnie, Pietro Adamvoski, Richard Ofordile]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""