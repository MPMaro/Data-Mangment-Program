
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

# Global 
userpos = -1



  
  
#Loops
userlogin = True
ProgramLoop = False

# User Login and Create Account

while userlogin:

    # Print the options
    print("Enter '1' to log in:")
    print("Enter '2' to sign up:")
    print("Enter '3' to exit:")

    # Get the user's choice
    choice = input("Please Enter Your choice:\n").lower()

    # Log In
    if choice == "1":
        # Get the user information
        username = input("Enter your username:")
        password = input("Enter your password:")

        for i in range(len(userinfo)):
            if userinfo[i]["username"] == username and userinfo[i]["password"] == password:
                userpos = i
                print("Login successful!")
                ProgramLoop = True
                userlogin = False
                break
            else:
                print("Incorrect username or password.")

    # Signup
    elif choice == "2":
        username = input("Create a username:")
        password = input("Enter your password:")

        # If the username is not already in the users dictionary, add it
        for i in range(len(userinfo)):
            if userinfo[i]["username"] == username:

                print("Account  exists")
                break
        else:
            userinfo.append({"username": username, "password": password, "favour":[]})
            userpos = len(userinfo)
            print("Sign up successful!")
            ProgramLoop = True
            userlogin = False

    # Exit the loop
    elif choice == "3":
        # Set the userlogin variable to False to exit the loop
        userlogin = False

    # Invalid input
    else:
        print("Please enter a valid input")


# Upload to JSON
with open("userinformation.json", "w") as f:
    json.dump(userinfo, f)
 
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
      print(userin)
      for x in range(len(books)):
        if userin == books[x]["Title"]:
          print(userin)
          userinfo[userpos]["favour"].append(books[x]["Title"])
          print("Books Added")
          return
        print("Book Not found")
        return
       
def opt5():
        userin = input("What book to remove: ")
        for book in favorite_list:
          if userin == book["Title"]:
            userinfo[userpos]["favour"].remove(book)
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
# Upload to JSON
      with open("userinformation.json", "w") as f:
        json.dump(userinfo, f)  
      break
    
    
  
    
    
    
