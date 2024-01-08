#T107 - P4 Task 2: Milestone 2's Final Team code
#Created by: (Arnie Nambiar, 101183154),(Matt Turner, 101169414),(Pietro Adamvoski, 101238885),(Richard Ofordile, 101190357)

#imports
from T107_P1_load_data import book_dictionary_category_list
from T107_P2_add_remove_search_dataset import (get_books_by_category, 
get_books_by_publisher, get_all_categories_for_book_title, add_book, remove_book, get_books_by_rate, get_books_by_title, get_books_by_author)
from T107_P3_sorting_fun import dictionary_to_list, sort_books_title, sort_books_publisher, sort_books_author, sort_books_ascending_rate

#Functions
#Created by: Pietro Adamvoski (101238885)
def available_commands_function()->None: 
    """Displays available commands 
    
    >>>available_commands_function()
    1- L)oad data
    2- A)dd book
    3- R)emove book
    4- G)et books
	 T)itle	R)ate  A)uthor	P)ublisher  C)ategory
    5 -GCT)Get all Categories for book Title
    6-S)ort books
	T)itle	R)ate  A)uthor	P)ublisher  C)ategory
    7-Q)uit
    """
    print("The available commands are:\n1- L)oad data\n2- A)dd book\n3- R)emove book\n4- G)et books\n\t T)itle\tR)ate  A)uthor\tP)ublisher  C)ategory\n5 -GCT)Get all Categories for book Title\n6-S)ort books\n\tT)itle\tR)ate  A)uthor\tP)ublisher  C)ategory\n7-Q)uit")

#Created by: Arnie Nambiar (101183154), Matt Turner (101169414), Pietro Adamvoski (101238885), Richard Ofordile (101190357)
def ui()->None:
    """User Interface containing 7 different commands to search through a dictionary
    Preconditions: Dictionary must be a book dictionary; 
    
    >>>ui()
    User Interface for Case 3 has started
    The available commands are:
    1- L)oad data
    2- A)dd book
    3- R)emove book
    4- G)et books
	 T)itle	R)ate  A)uthor	P)ublisher  C)ategory
    5 -GCT)Get all Categories for book Title
    6-S)ort books
	T)itle	R)ate  A)uthor	P)ublisher  C)ategory
    7-Q)uit
    >>>L
    Enter a dataset: 
    >>>google_books_dataset.csv
    Please type your command: 
    >>>GCT
    Enter a title: 
    >>>Rework
    Number of categories for given title:  2
    The book title " Rework " belongs to the following categories:
    Category 1 : Economics
    Category 2 : Business
    This book belongs in 2 categories
    The available commands are:
    1- L)oad data
    2- A)dd book
    3- R)emove book
    4- G)et books
	 T)itle	R)ate  A)uthor	P)ublisher  C)ategory
    5 -GCT)Get all Categories for book Title
    6-S)ort books
	T)itle	R)ate  A)uthor	P)ublisher  C)ategory
    7-Q)uit
    >>>Q
    User Interface has stopped
    """
    
    available_commands = ["G", "g","A", "a", "R", "r","S", "s","GCT","gct"]
    available_commands_get_books = ["T", "t", "P", "p", "C", "c","A", "a", "R", "r",]
    load_quit = ["Q","q","L","l"]
    ui_command = ""
    file = ""
    ui_command2 = ""  
    ui_command3 = ""
    ui_command4 = ""
    print("User Interface for Case 3 has started")
    available_commands_function()
    while ui_command!="Q" and ui_command!="q" and ui_command2!="Q" and ui_command2!="q":
        ui_command = input("Please type your command:"+" ")
        if ui_command == "Q" or ui_command =="q":
            print("User Interface has stopped")
            break
        elif ui_command in available_commands:
            print("File not loaded")
        elif ui_command not in available_commands and ui_command not in load_quit:
            print("No such command")
        elif ui_command == "L" or ui_command == "l":
            file = input("Enter a dataset:"+" ")
            while True:
                ui_command2 = input("Please type your command:"+" ")
                if ui_command2 == "Q" or ui_command2 == "q":
                    print("User Interface has stopped")
                    break 
                elif ui_command2 == "G" or ui_command2 == "g":
                    ui_command3 = input("How would you like to get books?"+" ")
                    while ui_command3 not in available_commands_get_books:
                        print("invalid way to get books")
                        ui_command3 = input("How would you like to get books?"+" ")
                        if ui_command3 in available_commands:
                            break
                        
                elif ui_command2 == "S" or ui_command2 == "s":
                    ui_command4 = input("How would you like to sort books?"+" ")                                 
                    while ui_command4 not in available_commands_get_books:
                        print("invalid way to get books")
                        ui_command4 = input("How would you like to sort books?"+" ")
                        if ui_command4 in available_commands:
                            break   
                        
                elif ui_command2 == "l" or ui_command2 == "L":
                            print("dataset already entered")                
                       
                elif ui_command2 not in available_commands:
                            print("No such command")                 
                
                #Get books
                if ui_command3 == "P" or ui_command3 == "p":
                    publisher = input("Enter a publisher: ")
                    print(get_books_by_publisher(publisher,book_dictionary_category_list(file)))
                    available_commands_function()
                    ui_command2=""
                    ui_command3=""
                
                         
                elif ui_command3 == "C" or ui_command3 == "c":
                    category_ui=input("Enter a Category: ")
                    print(get_books_by_category(category_ui, book_dictionary_category_list(file)))
                    available_commands_function()
                    ui_command2=""
                    ui_command3=""
                
                
                elif ui_command3 == "R" or ui_command3 == "r":
                    rating_ui=input("Enter a Rating: ")
                    rating_ui=float(rating_ui)
                    print(get_books_by_rate((book_dictionary_category_list(file)), rating_ui))
                    available_commands_function()
                    ui_command2=""
                    ui_command3=""
                    
                elif ui_command3 == "T" or ui_command3 == "t":
                    title_ui=input("Enter a Title: ")
                    print(get_books_by_title((book_dictionary_category_list(file)), title_ui))
                    available_commands_function()
                    ui_command2=""
                    ui_command3="" 
               
                elif ui_command3 == "A" or ui_command3 == "a":
                    author_ui=input("Enter an Author: ")
                    print(get_books_by_author(author_ui,book_dictionary_category_list(file)))
                    available_commands_function()
                    ui_command2=""
                    ui_command3=""                     
                
                #Sort books
                if ui_command4 == "T" or ui_command4 == "t":
                    print(sort_books_title(dictionary_to_list(book_dictionary_category_list("google_books_dataset.csv"))))
                    available_commands_function()
                    ui_command2=""
                    ui_command4="" 
                    
                if ui_command4 == "R" or ui_command4 == "r":
                    print(sort_books_ascending_rate(dictionary_to_list(book_dictionary_category_list("google_books_dataset.csv"))))
                    available_commands_function()
                    ui_command2=""
                    ui_command4=""   
              
                if ui_command4 == "P" or ui_command4 == "p":
                    print(sort_books_publisher(dictionary_to_list(book_dictionary_category_list("google_books_dataset.csv"))))
                    available_commands_function()
                    ui_command2=""
                    ui_command4=""    
                
                if ui_command4 == "A" or ui_command4 == "a":
                    print(sort_books_author(dictionary_to_list(book_dictionary_category_list("google_books_dataset.csv"))))
                    available_commands_function()
                    ui_command2=""
                    ui_command4=""                
                
                #add_book, remove_book, GCT           
                elif ui_command2 == "A" or ui_command2 == "a":
                    title_ui=input("Enter a Title: ")
                    author_ui=input("Enter an Author: ")
                    rating_ui=float(input("Enter a Rating: "))
                    publisher_ui=input("Enter a Publisher: ")
                    pages_ui=int(input("Enter number of Pages: "))
                    category_ui=input("Enter a Category: ")
                    language_ui=input("Enter a Language: ")
                    book_ui=(title_ui, author_ui, rating_ui, publisher_ui, pages_ui, category_ui, language_ui)
                    print(add_book(book_dictionary_category_list('google_books_dataset.csv'),book_ui))
                    available_commands_function()
                    ui_command2=" "
                
                elif ui_command2 == "R" or ui_command2 == "r":
                    title_ui=input("Enter the book title: ")
                    category_ui=input("Enter the book category: ")
                    print(remove_book(title_ui, category_ui, book_dictionary_category_list('google_books_dataset.csv')))
                    available_commands_function()
                    ui_command2=""                       
                    
                elif ui_command2 == "GCT" or ui_command2 == "gct":
                    title_ui=input("Enter a title: ")
                    print(get_all_categories_for_book_title(book_dictionary_category_list(file), title_ui))
                    available_commands_function()
                    ui_command2=""
                    

         

