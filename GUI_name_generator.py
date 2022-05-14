from tkinter import *
import random

#------------------LIST OF ALL OF THE PREFIXES, ROOTS, AND SUFFIXES-----------------------------------------------------------------------------------------------------------------------

#The reason all of these variables are declared as global is to optimize the code. 
#Instead of having to put these big lists in every function, I only need to declare them once.

#List of prefixes
global prefix1 
prefix1 = ["A", "De" , "Dis", "En" , "Ex" , "Extra" , "Hetero" "Hyper" , "Inter" , "Intra" , "Macro" , "Micro" , "Mono" , "Non" , "Omni" , "Post" , "Sub" , "Sym" , "Tele" , "Trans" , "Tri" , "Un" , "Uni" , "Up" , "Ante" , "Anti" , "Auto" , "Co" , "Com" , "Con" , "Contra" , "Contro" , "Re", "An", "In", "Mis", "Dif" , "Def", "Em", "Pre", "El", "Mid", "Nano", "Giga", "Tera", "Kilo", "Therm", "Para", "Ir", "Il", "Epi", "Iso", "Di", "Hypo", "Endo", "Poly", "Sub", "Penta", "Hexa", "Auto", "Ab", "Bi", "Be", "Retro", "Tele", "Fore", "Neo", "Her"]

#List of roots
global root1
root1 = ["act", "aqu" , "arch" , "aster" , "aud" , "bio" , "cad" , "chrome" , "chron" , "corp" , "duc" , "dynamo" , "fund", "gamy" , "geo" , "gen" , "gin" , "grad" , "her" , "hydro" , "jug" , "jud" , "kine" , "labor"  "lect" , "leg" , "liter" , "magna" , "mania" , "mis" , "mort" , "nat" , "ocle" , "pac" , "pass" , "path" , "ped" , "pod" , "pel" , "puls" , "pend" , "pens" , "pond" , "pet" , "phobia" , "phon" , "pict" , "plac" , "plic" , "plex" , "ply" , "polis" , "polit" , "poly" , "port" , "punct" , "pung" , "point" , "quer" , "quis" , "reg" , "rect" , "right" , "rog" , "scope" , "scrib" , "scrip" , "sens" , "sent" , "sequi" , "secut" , "suit" , "sid" , "sed" , "sess" , "sim" , "sign" , "sys" , "sol" , "son" , "solv" , "spir" , "sta" , "sist" , "sti" , "struct" , "tract" , "ten" , "tain" , "tin" , "tend" , "ter" , "therm" , "urb" , "vac" , "void" , "val" , "valu" , "ven" , "vent" , "vita" , "volu" , "vers"]

#List of suffixes
global suffix1
suffix1 = ["acy" , "al", "ance" , "dom" , "er" , "or" , "ism" , "ist", "ity" , "ment" , "ness" , "ship", "ate" , "en", "ify" , "ize" , "able" , "ful" , "esqe" , "less" "s", "ward", "osis", "itis", "ile", "ic", "tion", "ed", "ous", "ness", "ion"]

#--------------------LIST OF FIRST, MIDDLE, AND LAST NAMES---------------------------------------------------------------------------------------------------------------------

#List of first names
global firstname1 
firstname1 = ["Ava", "Amelia", "Abigail", "Alexander", "Aiden", "Anthony", "Emma", "Evelyn", "Emily", "Elijah", "Ethan", "Ezra", "James", "Robert", "John", "Michael", "William", "David", "Richard", "Joseph", "Thomas","Charles", "Christopher", "Matthew", "Donald", "Anthony", "Steven", "Paul","Joshua", "Kevin", "Brian", "George", "Edward", "Timothy", "Jason", "Jeffrey", "Ryan", "Jacob", "Gary", "Eric","Jonathan", "Stephen", "Larry", "Justin", "Scott", "Brandon", "Benjamin","Samuel", "Frank", "Alexander", "Raymond", "Patrick", "Jack", "Jerry", "Tyler", "Mary", "Patricia", "Jennifer", "Linda","Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen", "Nancy","Lisa", "Betty", "Margaret", "Sandra", "Ashley", "Kimberly", "Emily", "Donna", "Michelle", "Dorothy", "Carol", "Amanda","Melissa", "Deborah", "Stephanie", "Rebecca", "Sharon", "Laura", "Cynthia","Amy", "Angela", "Helen", "Anna", "Brenda", "Pamela", "Nicole", "Samantha", "Christine", "Debra", "Rachel", "Catherine","Carolyn", "Janet", "Ruth", "Maria", "Heather", "Diane"]

#List of middle names
global middlename1
middlename1 = ["Penelope" , "Elizabeth" , "Grace" , "Hazel" , "Violet" , "Ivy" , "Anna" , "Sadie" , "Iris" , "Faith" , "Olive" , "Rosalie" , "Willa" , "Joy" , "Aurelia" , "Jane" , "Myra" , "Priscilla" , "Mina" , "Theo" , "Wesley" , "Harrison" , "Luke" , "David" , "Charles" , "Calvin" , "Timothy" , "Carlos" , "Finn" , "Alan" , "Leon" , "Grant" , "Jax" , "Chance" , "Kane" , "Hector" , "Dax" , "Bruce" , "Jeremiah" , "Clay" , "Wayne" , "Trent" , "Marc" , "Steve" , "Kent" , "Aris" , "Dan" , "Rush" , "Penn" , "Burke" , "Niles" , "Jai" , "Roan" , "Clint" , "Shai" , "Kolt" ]
        
#List of last names
global lastname1
lastname1 = ["Smith", "Johnson" , "Williams" , "Brown" , "White" , "Jones" , "Garcia", "Miller", "Davis" , "Lopez" , "Gonzales" , "Wilson" , "Anderson" , "Thomas" , "Taylor" , "Moore" , "Jackson" , "Martin", "Lee" , "Thompson" , "Perez" , "Harris" , "Clark" , "Ramirez", "Lewis", "Robinson" , "Walker" , "Young" , "Allen" , "King" , "Wright" , "Scott" , "Torres" , "Nguyen" , "Hill", "Flores" , "Green" , "Adams" , "Nelson" , "Baker" , "Hall", "Rivera", "Campbell" , "Carter" , "Roberts" , "Gomez" , "Phillips" , "Evans" , "Turner" , "Diaz" , "Parker" , "Cruz", "Edwards" , "Collins" , "Stewart" , "Morris" , "Morales" , "Murphy", "Cook", "Rogers" , "Ortiz" , "Morgan" , "Cooper" , "Peterson" , "Bailey" , "Reed" , "Kelly" , "Howard" , "Ramos" , "Cox" , "Richardson" , "Watson", "Brooks" , "Chavez" , "Bennett" , "Wood" , "Mendoza" , "Hughes", "Price", "Sanders" , "Myers" , "Long" , "Ross" , "Foster" , "Jimenez"]

#-----------------ALL OF THE FUNCTIONS IN THIS PROGRAM------------------------------------------------------------------------------------

#Make a popup for generating single usernames
def open_popup():
   top = Toplevel(window)
   top.geometry("400x100")
   top.title("Name Generator Popup")
   label = Label(top, text= "Thank you for generating a name. \nYour name is {}!".format(short.username), font = "bold") 
   label.place(x=65,y=20)

#Making a popup for mass generating names and telling you where they're stored
def open_popup1():
   top = Toplevel(window)
   top.geometry("500x100")
   top.title("Name Generator Popup")
   label = Label(top, text= "Thank you for generating names! \nThey're stored in a text file named 'names.txt'!" , font = "bold") 
   label.place(x=65,y=20)

#Creating the short function
def short():
 
    #Chooses a random prefix from the list
    prefix2 = random.choice(prefix1)

    #Chooses a random root from the list
    root2 = random.choice(root1)

    #Creates the username
    short.username = "%s%s" % (prefix2, root2)

    #Open a popup
    open_popup()  

 
#Creates a function to make the long names
def long():

    #Chooses a random prefix from the list
    prefix2 = random.choice(prefix1)

    #Chooses a random root from the list
    root2 = random.choice(root1)

    #Chooses a random suffix from the list
    suffix2 = random.choice(suffix1)

    #Sets the username to equal this
    short.username = ("%s%s%s" % (prefix2, root2, suffix2))

    #Open a popup
    open_popup() 

#Generating long real names
def realnamelong():
    
    #Picks a random first name from the list
    firstname2 = random.choice(firstname1)

    #Picks a random middle name from the list
    middlename2 = random.choice(middlename1)

    #Picks a random last name from the list
    lastname2 = random.choice(lastname1)
        
    #Creates the username
    short.username = "%s %s %s" % (firstname2, middlename2, lastname2)

    #Open a popup
    open_popup() 

#Generating short real names
def realnameshort():
    
    #Picks a random first name from the list
    firstname2 = random.choice(firstname1)

    #Picks a random last name from the list
    lastname2 = random.choice(lastname1)
        
    #Creates the username
    short.username = "%s %s" % (firstname2, lastname2)

    #Open a popup
    open_popup() 

#Mass generating short names
def massgenerateshort():

    #Creates a text file called names.txt if it doesn't exist already
    with open('names.txt', 'w') as file:
    
        #N is equal to the value from the textbox
        n1 = textbox.get(1.0, 'end')

        #Convert it to an integer
        n = int(n1)
          
        #Generates as many names as you want
        for i in range(n):
                
            #Chooses a random prefix from the list
            prefix2 = random.choice(prefix1)

            #Chooses a random root from the list
            root2 = random.choice(root1)
        
            #Creates the username
            short.username = "%s%s\n" % (prefix2, root2)

            #Writes to the names.txt file the randomly generated word
            file.write(short.username)
            file.close
        
        #Opening a popup
        open_popup1()

#Mass generating long names
def massgeneratelong():

    #Creates a text file called names.txt if it doesn't exist already
    with open('names.txt', 'w') as file:
    
        #N is equal to the value from the textbox
        n1 = textbox.get(1.0, 'end')

        #Convert it to an integer
        n = int(n1)
          
        #Generates as many names as you want
        for i in range(n):
                
            #Chooses a random prefix from the list
            prefix2 = random.choice(prefix1)

            #Chooses a random root from the list
            root2 = random.choice(root1)

            #Chooses a random suffix from the list
            suffix2 = random.choice(suffix1)

            #Sets the username to equal this
            short.username = ("%s%s%s\n" % (prefix2, root2, suffix2))

            #Writes to the names.txt file the randomly generated word
            file.write(short.username)
            file.close
        
        #Opening a popup
        open_popup1()

#Mass generating short real names
def massgeneratereal():

    #Creates a text file called names.txt if it doesn't exist already
    with open('names.txt', 'w') as file:
    
        #N is equal to the value from the textbox
        n1 = textbox.get(1.0, 'end')

        #Convert it to an integer
        n = int(n1)

        #Generates as many names as you want
        for i in range(n):
                
            #Picks a random first name from the list
            firstname2 = random.choice(firstname1)

            #Picks a random last name from the list
            lastname2 = random.choice(lastname1)
        
            #Creates the username
            short.username = "%s %s\n" % (firstname2, lastname2)

            #Writes to the names.txt file the randomly generated word
            file.write(short.username)
            file.close

        #Opening a popup
        open_popup1()

#Mass generate long real names
def massgeneratereallong():

    #Creates a text file called names.txt if it doesn't exist already
    with open('names.txt', 'w') as file:
    
        #N is equal to the value from the textbox
        n1 = textbox.get(1.0, 'end')

        #Convert it to an integer
        n = int(n1)
          
        #Generates as many names as you want
        for i in range(n):
                
            #Picks a random first name from the list
            firstname2 = random.choice(firstname1)

            #Picks a random middle name from the list
            middlename2 = random.choice(middlename1)

            #Picks a random last name from the list
            lastname2 = random.choice(lastname1)
        
            #Creates the username
            short.username = "%s %s %s\n" % (firstname2, middlename2, lastname2)

            #Writes to the names.txt file the randomly generated word
            file.write(short.username)
            file.close
        
        #Opening a popup
        open_popup1()


#--------------------------------------------------------------------------------------------------------------------------------

#Creating the window
window = Tk()

#Setting the title to Name Generator and making the dimensions 750 pixels by 500
window.title("Name Generator")
window.geometry("750x450")

#--------------------------GENERATING SINGLE USERNAMES / REAL NAMES------------------------------------------------------------------------------------------------------

#Making the text bold and green
label1 = Label(text= "Single usernames/real names", font = "bold", fg = "green")
label1.grid(row = 1, column = 4, padx= 50, pady= 10)

#Buttons for generating usernames
b1 = Button(window, text = "Generate a short username!" , command = short)
b2 = Button(window, text = "Generate a long username!", command = long)
b3 = Button(window, text = "Generate a short real name!" , command = realnameshort)
b4 = Button(window, text = "Generate a long real name!", command = realnamelong)
 
#Arranging button widgets
b1.grid(row = 4, column = 4, padx= 250, pady= 5,)
b2.grid(row = 5, column = 4, padx= 250, pady= 5,)
b3.grid(row = 6, column = 4, padx= 250, pady= 5,)
b4.grid(row = 7, column = 4, padx= 250, pady= 5,)

#---------------------------MASS GENERATING USERNAMES / REAL NAMES-----------------------------------------------------------------------------------------------------

#Making the text bold and green
label1 = Label(text= "Mass generate usernames/real names", font = "bold", fg = "green")
label1.grid(row = 9, column = 4, padx= 50, pady= 5)

#Textbox for determining how many names you want to generate
textbox = Text(window, height = 1, width = 17)
textbox.insert(INSERT, "Enter an integer")
textbox.grid(row = 10, column = 4, padx= 50, pady= 5)

#Buttons for generating usernames
b5 = Button(window, text = "Generate short usernames!" , command = massgenerateshort)
b6 = Button(window, text = "Generate long usernames!", command = massgeneratelong)
b7 = Button(window, text = "Generate short real names!" , command = massgeneratereal)
b8 = Button(window, text = "Generate long real names!", command = massgeneratereallong)

#Arranging button widgets
b5.grid(row = 11, column = 4, padx= 250, pady= 5)
b6.grid(row = 12, column = 4, padx= 250, pady= 5)
b7.grid(row = 13, column = 4, padx= 250, pady= 5)
b8.grid(row = 14, column = 4, padx= 250, pady= 5)
 
#---------------------------LOOPING THE WINDOW-----------------------------------------------------------------------------------------------------

#Looping the window
window.mainloop()