#Pietro Adamvoski - 101238885

import string
from typing import List
from T107_P1_load_data import book_dictionary_category_list

#Functions
#Function 5
def get_books_by_title(dic:dict, title:str)->str:
    """Returns True if title exists in dictionary. If title does not exists 
    in dictionary, returns False.
    
    >>>get_books_by_title('After Anna')
    True
    The book has been found
    
    >>>get_books_by_title('Ater Anna')
    False
    The book has NOT been found
    """
    
    counter=0
    dictionary_book_list = dic.values()
    for row in dictionary_book_list:
        for column in row:
            if column.get("title") == title:
                counter=1
                return "{i}: The book has been found".format(i=bool(column.get("title") == title))
    if counter==0:       
        print("{i}: The book has NOT been found".format(i=bool(column.get("title") == title)))
                
                

#Function 8
def get_all_categories_for_book_title(dic:dict, title:str)->str:
    """Returns the number of categories associated with given book title. Also, 
    returns all the categories associated with given book title. 
    
    >>>get_all_categories_for_book_title('After Anna')
    Number of categories for given title: 4
    Category 1: "Fiction"
    Category 2: "Adventure"
    Category 3: "Thrillers"
    Category 4: "Mystery"
    
    >>>get_all_categories_for_book_title('Ultimate Spider-Man Vol. 11: Carnage')
    Number of categories for given title: 1
    Category 1: "Comics"
    """    
    category_list = []
    counter=0
    for category in dic.keys():
        for book in dic.get(category):
            if book.get("title") == title:
                counter+=1
                if category not in category_list:
                    category_list.append(category)
     
   
    print("Number of categories for given title: ", counter)
    counter=0
    print("The book title",'"', title,'"', "belongs to the following categories:") 
    for i in category_list:
        counter+=1
        print("Category",counter,":",i)
    return counter

