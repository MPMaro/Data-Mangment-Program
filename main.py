
import re
import helpers

#Inizialize the list
books = [
  {
    "Title" : "The Outsider",
    "Author": "JackSp",
    "IBSN" : 909009,
    "Genre" : "Thiller"
  } ,
  {
    "Title" : "Harry Potter",
    "Author": "Harry",
    "IBSN" : 23562136,
    "Genre" : "FairyTale"
  } ,
  {
    "Title" : "The 20th Victom",
    "Author": "Jaimes Aderson",
    "IBSN" : 457845,
    "Genre" : "Mystery"
  } ,
  {
    "Title" : "The Hunger Games",
    "Author": "Katniess Everdeen",
    "IBSN" : 795754,
    "Genre" : "Horror"
  } ,
]

favorite_list = [
  
]


def opt1():
        for x in range(len(books)):
            print(books[x]["Title"])
            print(books[x]["Author"])
            print(books[x]["IBSN"])
            print(books[x]["Genre"])
            print(" ") 
def opt2():
      userin = input("Type out the Genre: ")
      for x in range(len(books)):
        if userin == books[x]["Genre"]:
            print(books[x]["Title"])  
            print(books[x]["Author"])  
            print(books[x]["IBSN"])  
            print(books[x]["Genre"])  
            print(" ")  
            return
      print("Not found")
      return
    
def opt3():
      helpers.bubbleSort(books)
      for x in range(len(books)):
        print((books[x]["IBSN"]))

def opt4():
      userin = input("What book to add: ") 
      for x in range(len(books)):
        if userin == books[x]["Title"]:
          favorite_list.append(books[x])
          print("Books Added")
          return
      print("Book Not found")
      return
       
def opt5():
        userin = input("What book to remove: ")
        for book in favorite_list:
          if userin == book["Title"]:
            favorite_list.remove(book)
            print("Book Removed")
            return
        print("Book Not Found in Favourite List")
        return
      
      
def opt6():
        for x in range(len(favorite_list)):
            print(favorite_list[x]["Title"])
            print(favorite_list[x]["Author"])
            print(favorite_list[x]["IBSN"])
            print(favorite_list[x]["Genre"])
            print(" ")
  
#Set Loop True
ProgramLoop = True

#Start Looping
while ProgramLoop:

  #Options To pick From
    print("OPTION 1: Display all of the data")
    print("OPTION 2: Display some of the data")
    print("OPTION 3: Sort the data")
    print("OPTION 4: Add to Favourite List")
    print("OPTION 5: Remove Data From Favourite List")
    print("OPTION 6: Display Favoutrite List")
    print("OPTION 7: Exit")

    #Input From The user
    userInput = input("Pick your Option: ")

    #Option 1 - Display All
    if(userInput == "1"):
      opt1()
    
    #Option 2 - Display Some of the data
    elif(userInput == "2"):
      opt2()
                 
    #Option 3 - Sort the Data
    elif(userInput == "3"):
      opt3()
                
    #Option 4 - Add to a Favorite List
    elif(userInput == "4"):
      opt4()    
          
    #Option 5 - Remove from Favourite List
    elif(userInput == "5"):
      opt5()
          
     #Option 6 - Display Favorite List   
    elif(userInput == "6"):
      opt6()
    #Option 7 - End Loop
    elif(userInput == "7"):
        break
    
    
  
    
    
    
