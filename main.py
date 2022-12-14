
import re
import helpers
import json

#Inizialize the list

#Load book data from JSON file
file = open("book_data.json", "r")
dataStr = file.read()
file.close()
books = json.loads(dataStr)

#Load Favourites from JSON file
file2 = open("fav.json", "r")
dataStr2 = file2.read()
file2.close()
favorite_list = json.loads(dataStr2)

#Load User Information From JSON file
file3 = open("userinformation.json", "r")
dataStr3 = file3.read()
file3.close()
userinfo = json.loads(dataStr3)


def opt1():
        for x in range(len(books)):
            print(books[x]["Title"])
            print(books[x]["Author"])
            print(books[x]["IBSN"])
            print(books[x]["Genre"])
            print(" ") 
def opt2():
      userin = input("Type out the Genre: ").capitalize()
      for x in range(len(books)):
        if userin == books[x]["Genre"]:
            print(" ")
            print(books[x]["Title"])  
            print(books[x]["Author"])  
            print(books[x]["IBSN"])  
            print(books[x]["Genre"])  
            print(" ")  
            return
      print("Not found")
      return
    
def opt3():
      userin = input("Type in the Data To Sort: ")
      if userin == "Title" or "Genre" or  "IBSN" or "Author":
          helpers.bubbleSort(books,userin)
          print("Data Sorted")
        

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
        favlist_length = len(favorite_list)
        for x in range(len(favorite_list)):
            print(favorite_list[x]["Title"])
            print(favorite_list[x]["Author"])
            print(favorite_list[x]["IBSN"])
            print(favorite_list[x]["Genre"])
            print(" ")
        if favlist_length == 0:
            print("No Books in Favorite LIst")
  
  
userlogin = True

#Set Loop True
ProgramLoop = False
while userlogin:

    #Print the Options
    print("Enter 'L' to log in:")
    print("Enter 'S' to sign up:")
    print("Enter 'E' to exit:")

    # Get the user's choice
    choice = input("Please Enter Your choice:\n").lower()


    #Log In
    if choice == "l":
      #Get the User Informationj
      username = input("Enter your username:")
      password = input("Enter your password:")

      #Log the User In
      if username in userinfo and userinfo[username] == password:
        logged_in = True
        print("Login successful!")
        ProgramLoop = True
        break

      else:
          #Incase UserInformation Not Found
        print("Incorrect username or password.")


    # Signup
    elif choice == "s":
      username = input("Create a username:")
      password = input("Create a password:")

      # If the username is not already in the users dictionary, add it
      if username not in userinfo:
        userinfo[username] = password
        print("Sign up successful!")
        ProgramLoop = True

        #Upload To JSON
        json_str = json.dumps(userinfo)
        with open("userinformation.json", "w") as f:
            f.write(json_str)

        break
      else:
        # Display an error message
        print("Username already exists")


    #Exit the Loop
    elif choice == "e":
        break


    #Invalid Input
    else:
        print("Please enter a valid input")

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
      json_str = json.dumps(favorite_list)
      with open("fav.json", "w") as f:
            f.write(json_str)  
      break
    
    
  
    
    
    
