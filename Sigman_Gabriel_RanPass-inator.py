# Program name: RanPass-Inator
# Author: Gabriel Sigman
# Date: From 04/20/2022 - 05/03/2022
# Variables:
# alphaUP - List - list of uppercase letters
# alphaDown - List - list of lowercase letters
# digits - List - list of numbers
# special_characters - List - list of symbols
# characters - List - added variable with all 3 listed variables combined.
# length - Integer - length of the password in characters
# upper_count - Integer - number of uppercase characters in the password
# lower_count - Integer - number of lowercase characters in the password
# num_count - Integer - number of numbers in the password
# symbol_count - Integer - number of symbols in the password
# clicks - Integer - number of times the yellow button has been clicked

## imports the needed libraries and assignes them to variables
try:
    import Tkinter as tk
    import tkMessageBox as mb
    from tkinter import *    
except ImportError:
    import tkinter as tk
    import tkinter.messagebox as mb
##Creates the window with a 600x500 resolution, and assigns root to tk.Tk() for ease.
root = tk.Tk()
root.geometry("600x500")

## Imports string function as well as random function to generate the lists, and allow for the randon number to be generated in the "moving" function
import string
import random

## Generates the lists of characters to be used to make the passwords.
alphaUp= list(string.ascii_uppercase)
alphaLo= list(string.ascii_lowercase)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

##Creates the title at the top of the screen, and allows me to change the font. Any Label with "" as the output is just a way for me to "double space" the buttons. 
tk.Label(root, text="RanPass-Inator", font="ComicSans").pack()
tk.Label(root, text="").pack()



##Assigns the variables.
length = 28
upper_count = 7
lower_count = 7
num_count = 7
symbol_count = 7
clicks = 0
password = []


##Imports the string and random function. They would not work when imported with the other function above, so i dragged them down here and they work. 
import string
import random

##Funtion used to move the yellow button around the screen.

def moving():
    global clicks
    ran1 = random.randint(0,450)
    ran2 = random.randint(0,350)
    btn.place(x=ran1, y=ran2)
    clicks += 1
    return
##Imports the .py file with a function to exit the program
def exitimport():
    import ImportExit
    ImportExit.exitpro("Good bye!")
##Creates a symbol heavy password by cycling through for loops a certain amount of times,
##indicated by the X_count variable. 
def symbols():
    ## This makes it so you need to click the yellow button 3 times in order to generate a password
    global clicks
    if clicks < 3:
        print("   Please click the yellow button 3 times to active the generator.   ")        
        return   
    password = []
    while len(password) < length:
        symbol_count = 13
        upper_count = 5
        lower_count = 5
        num_count = 5
        for i in range(symbol_count):
            password.append(random.choice(special_characters))
        for i in range(upper_count):
            password.append(random.choice(alphaUp))
        for i in range(lower_count):
            password.append(random.choice(alphaLo))
        for i in range(num_count):
            password.append(random.choice(digits))
    
        for i in range (length - len(password)):
            password.append(random.choice(characters))
    random.shuffle(password)
    print("".join(password))
    return

##Creates a number heavy password by cycling through for loops a certain amount of times,
##indicated by the X_count variable. 
def num():
    ## This makes it so you need to click the yellow button 3 times in order to generate a password
    global clicks
    if clicks < 3:
        print("   Please click the yellow button 3 times to active the generator.   ")        
        return 
    password = []
    while len(password) < length:
        symbol_count = 5
        upper_count = 5
        lower_count = 5
        num_count = 13
        for i in range(symbol_count):
            password.append(random.choice(special_characters))
        for i in range(upper_count):
            password.append(random.choice(alphaUp))
        for i in range(lower_count):
            password.append(random.choice(alphaLo))
        for i in range(num_count):
            password.append(random.choice(digits))
    
        for i in range (length - len(password)):
            password.append(random.choice(characters))
    random.shuffle(password)
    print("".join(password))
    return
##Creates a lowercase heavy password by cycling through for loops a certain amount of times,
##indicated by the X_count variable.    
def lower():
    ## This makes it so you need to click the yellow button 3 times in order to generate a password
    global clicks
    if clicks < 3:
        print("   Please click the yellow button 3 times to active the generator.   ")        
        return 
    password = []
    while len(password) < length:
        symbol_count = 5
        upper_count = 5
        lower_count = 13
        num_count = 5
        for i in range(symbol_count):
            password.append(random.choice(special_characters))
        for i in range(upper_count):
            password.append(random.choice(alphaUp))
        for i in range(lower_count):
            password.append(random.choice(alphaLo))
        for i in range(num_count):
            password.append(random.choice(digits))
    
        for i in range (length - len(password)):
            password.append(random.choice(characters))
    random.shuffle(password)
    print("".join(password))
    return
##Creates a uppercase heavy password by cycling through for loops a certain amount of times,
##indicated by the X_count variable. 
def upper():
    ## This makes it so you need to click the yellow button 3 times in order to generate a password
    global clicks
    if clicks < 3:
        print("   Please click the yellow button 3 times to active the generator.   ")        
        return 
    password = []
    while len(password) < length:
        symbol_count = 5
        upper_count = 13
        lower_count = 5
        num_count = 5
        for i in range(symbol_count):
            password.append(random.choice(special_characters))
        for i in range(upper_count):
            password.append(random.choice(alphaUp))
        for i in range(lower_count):
            password.append(random.choice(alphaLo))
        for i in range(num_count):
            password.append(random.choice(digits))
    
        for i in range (length - len(password)):
            password.append(random.choice(characters))
    random.shuffle(password)
    print("".join(password))
    return
##Creates all of the buttons on screen. root adds it to the window, text lets me edit the text on the button,
## bg is the background color, and command is where i can choose which funciton the button executes. 
btn = tk.Button(root, text = "Click Me!", bg="yellow", command=moving)
btn.place(x=1,y=2)
btn2 = tk.Button(root, text = "Exit", bg="red", command=exitimport)
btn2.place(x=290, y=325)
btn1 = tk.Button(root, text="Symbol heavy password", bg="coral", command=symbols).pack()
tk.Label(root, text="").pack()
tk.Button(root, text="Uppercase heavy password", bg="lime", command=upper).pack()
tk.Label(root, text="").pack()
tk.Button(root, text="Lowercase heavy password", bg="khaki", command=lower).pack()
tk.Label(root, text="").pack()
tk.Button(root, text="Number heavy password", bg="blue", command=num).pack()


root.mainloop()
