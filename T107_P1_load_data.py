
#Created by: Matt Turner: 101169414
#Reviewed by: Pietro Adamvoski: (101238885) - Arnie Nambiar: (101183154) - Richard Ofordile: (101190357)


#Functions
import string
from typing import List

def book_dictionary_author_list(filename: str) -> dict: #Case 1
    """Returns a dictionary of a data set containing google books and sorts them 
    by author
    
    book_dictionary_category_list()
    >>>"Fiction":[ {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery",
    "author": " Barbara Allan",
    "language ": "English",
    "rating": 3.3,
    "publisher": " Kensington Publishing Corp.",
    "pages": 288
    
    
    """
    infile = open(filename, "r")
    next(infile)
    book_dic={}
    for line in infile:
        lst=[]
        dic={}
        category=line.split(",")[5]
        book_dic[str(category)] = lst
        
       
        
        dic.clear()
        lst.clear()
        dic["title"]=line.split(",")[0]
        dic["author"]=line.split(",")[1]
        dic["language"]=line.strip("\n").split(",")[6]
        dic["rating"]=line.split(",")[2]
        dic["publisher"]=line.split(",")[3]
        dic["pages"]=line.split(",")[4]

        lst.append(dic)
        book_dic[category].append(lst)
        
    infile.close()
    print(book_dic)
    return book_dic

#Main Body

#Main Script: Case 1

book_dictionary_author_list('google_books_dataset.csv')
