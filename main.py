
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
    "Genre" : "Myster"
  } ,
  {
    "Title" : "The Outsider",
    "Author": "JackSp",
    "IBSN" : 909009,
    "Genre" : "Fairytale"
  } ,
  
]


#Set Loop True
ProgramLoop = True

#Start Looping
while ProgramLoop:

  #Options To pick From
    print("OPTION 1: Display all of the data")
    print("OPTION 2: Display some of the data")
    print("OPTION 3: Sort the data")
    print("OPTION 4: Select data to add to a favourites list / shopping cart")
    print("OPTION 5: Display favourites list / shopping cart")
    print("OPTION 6: Exit")

    #Input From The user
    userInput = input("Pick your Option: ")

    #Option 1 - Display All
    if(userInput == "1"):
        for x in range(len(books)):
            print(books[x]["Title"])
            print(books[x]["Author"])
            print(books[x]["IBSN"])
            print(books[x]["Genre"])
            print(",")
    

    #Option 2 - Display Some of the data
    elif(userInput == "2"):
        userin = input("Type out the Genre: ")
        for x in range(len(books)):
            if userin == books[x]["Genre"]:
                print(books[x]["Title"])
                 

    #Option 3 - Sort the Data
    elif(userInput == "3"):
        sorted_data = []
        for x in range(len(books)):
            sorted_data.append(books[x]["IBSN"])
        helpers.insertionSort(sorted_data)
        print(sorted_data)
        
    #Option 4 - New Contact
    elif(userInput == "4"):
        print("PlaceHolder")


    #Option 5 - Remove Contact
    elif(userInput == "5"):
        print("PlaceHolder")


    #Option 6 - End Loop
    elif(userInput == "6"):
        break
    
    
    
    
