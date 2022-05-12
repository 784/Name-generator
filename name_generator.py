#Importing the random module (it's needed for generating random integers and choosing random strings from arrays)
import random

#Importing the time module (it's needed for allowing time between messages so that you're able to see the error messages if there are any)
import time

#Sets satisfaction to false
global satisfaction
satisfaction = False

#------------------LIST OF ALL OF THE PREFIXES, ROOTS, AND SUFFIXES-----------------------------------------------------------------------------------------------------------------------
#List of prefixes
global prefix1 
prefix1 = ["A", "De" , "Dis", "En" , "Ex" , "Extra" , "Hetero" "Hyper" , "Inter" , "Intra" , "Macro" , "Micro" , "Mono" , "Non" , "Omni" , "Post" , "Sub" , "Sym" , "Tele" , "Trans" , "Tri" , "Un" , "Uni" , "Up" , "Ante" , "Anti" , "Auto" , "Co" , "Com" , "Con" , "Contra" , "Contro" , "Re"]

#List of roots
global root1
root1 = ["act", "aqu" , "arch" , "aster" , "aud" , "bio" , "cad" , "chrome" , "chron" , "corp" , "duc" , "dynamo" , "fund", "gamy" , "geo" , "gen" , "gin" , "grad" , "her" , "hydro" , "jug" , "jud" , "kine" , "labor"  "lect" , "leg" , "liter" , "magna" , "mania" , "mis" , "mort" , "nat" , "ocle" , "pac" , "pass" , "path" , "ped" , "pod" , "pel" , "puls" , "pend" , "pens" , "pond" , "pet" , "phobia" , "phon" , "pict" , "plac" , "plic" , "plex" , "ply" , "polis" , "polit" , "poly" , "port" , "punct" , "pung" , "point" , "quer" , "quis" , "reg" , "rect" , "right" , "rog" , "scope" , "scrib" , "scrip" , "sens" , "sent" , "sequi" , "secut" , "suit" , "sid" , "sed" , "sess" , "sim" , "sign" , "sys" , "sol" , "son" , "solv" , "spir" , "sta" , "sist" , "sti" , "struct" , "tract" , "ten" , "tain" , "tin" , "tend" , "ter" , "therm" , "urb" , "vac" , "void" , "val" , "valu" , "ven" , "vent" , "vita" , "volu" , "vers"]

#List of suffixes
global suffix1
suffix1 = ["acy" , "al", "ance" , "dom" , "er" , "or" , "ism" , "ist", "ity" , "ment" , "ness" , "ship", "ate" , "en", "ify" , "ize" , "able" , "ful" , "esqe" , "less" "s"]

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
#Creating the short function
def short():
 
    #Chooses a random prefix from the list
    prefix2 = random.choice(prefix1)

    #Chooses a random root from the list
    root2 = random.choice(root1)

    #Creates the username
    username = "%s%s\n" % (prefix2, root2)

    #Prints the prefix with the first letter uppercase + the root
    print(username)

    #Asks if you want to add numbers
    numbers1 = input("\nWould you like to add numbers to the name? Type 'Y' for yes and 'N' for no: ")

    #Making it uppercase incase you make the Y lowercase
    numbers = numbers1.upper()

    #If you say yes, a random number is chosen to be added
    if numbers == "Y":

        #Chooses a random number from the list
        numbers2 = random.randint(1,99)

        #Converts the integer into a string so it can be added to the username
        numbers2 = str(numbers1)

        #Prints the prefix with the first letter uppercase, the root, the suffix, and numbers
        print("%s %s %s\n" % (prefix2, root2, numbers2))
    
    #If you say no, this is printed
    elif numbers == "N":
        print("Awww, ok!")

    #Gives you an error message if you don't choose Y or N
    else:
        print("\nPlease choose 'Y' or 'N'!\n")
        time.sleep(2)
    
#Creates a function to make the long names
def long():

    #Chooses a random prefix from the list
    prefix2 = random.choice(prefix1)

    #Chooses a random root from the list
    root2 = random.choice(root1)

    #Chooses a random suffix from the list
    suffix2 = random.choice(suffix1)

    #Prints the prefix with the first letter uppercase, the root, and then the suffix
    print("%s %s %s\n" % (prefix2, root2, suffix2))


    #Asks if you want to add numbers to the name
    numbers = input("\nWould you like to add numbers to the name? Type 'Y' for yes and 'N' for no: ")

    #If you say yes, a random number is chosen 
    if numbers == "Y":

        #Chooses a random number
        numbers1 = random.randint(1,99)

        #Converts the integer into a string so it can be added to the username
        numbers2 = str(numbers1)

        #Prints the prefix with the first letter uppercase, the root, the suffix, and numbers
        print("%s %s %s %s\n" % (prefix2, root2, suffix2, numbers2))


    #If you say no, this is printed
    elif numbers == "N":
        print("Awww, ok!")

    #Gives you an error message if you don't choose Y or N
    else:
        print("\nPlease choose 'Y' or 'N'!\n")
        time.sleep(2)

#Generating long real names
def realnamelong():
    
    #Picks a random first name from the list
    firstname2 = random.choice(firstname1)

    #Picks a random middle name from the list
    middlename2 = random.choice(middlename1)

    #Picks a random last name from the list
    lastname2 = random.choice(lastname1)
        
    #Creates the username
    long.username = "%s %s %s\n" % (firstname2, middlename2, lastname2)

    #Prints the name
    print(long.username)

#Generating short real names
def realnameshort():
    
    #Picks a random first name from the list
    firstname2 = random.choice(firstname1)

    #Picks a random last name from the list
    lastname2 = random.choice(lastname1)
        
    #Creates the username
    short.username = "%s %s\n" % (firstname2, lastname2)

    print(short.username)


#Asking if you're satisfied with your username
def satisfaction1():

    #Making satisfaction a global variable
    global satisfaction

    #Asks if you're satisfied
    satisfied1 = input("Are you satisfied? Type 'Y' for yes and 'N' for no: ")

    #Making it uppercase incase you type Y or N in lowercase
    satisfied = satisfied1.upper()

    #If you're satisfied, the loop is completed
    if satisfied == "Y":
        satisfaction = True

    #If you're not, the loop continues   
    elif satisfied == "N":
        satisfaction = False

    #If you accidentally mess up and press something other than Y or N, this is executed  
    else:
        print("\nPlease choose 'Y' or 'N'!\n")
        time.sleep(2)
        satisfaction = False

#--------------------------CHOOSING YOUR MODE---------------------------------------------------------------------------
#Choosing your mode
mode1 = input("\nDo you want to use username mode or real name mode? 'U' for username, 'R' for real name: ")

#Making it uppercase in case you accidentally type U or R in lowercase
mode = mode1.upper()
#-----------------------------------------------------------------------------------------------------------------------


#-------------------------USERNAME MODE----------------------------------------------------------------------------------------------
#Username mode code
if mode == "U":
    
    #Restart function
    def restart():
    
        #Asks if you want to mass generate names
        userinput = input("\nDo you want to mass generate names or do you only want a few? Type 'M' for mass generate, 'F' for few: ")

        #Making it uppercase in case you accidentally type M or F in lowercase
        userinput1 = userinput.upper()

        #Only a few names are generated if you decide to do this
        if userinput1 == "F":
        
            #Until you're happy, it'll keep generating new names
            while satisfaction == False:
    
                #Asks if want a long or short name
                userinput = input("Do you want a short name or a long one? Type 'short' for a short one and 'long' for a long one: ")
    
                #If you choose short, this bit of code is executed
                if userinput == "short":
        
                    #Calling the short function
                    short()

                    #Calling the satisfaction function to see if you're satisfied
                    satisfaction1()

                #If you choose a long name, this is executed
                elif userinput == "long":
    
                    #Calls the long function 
                    long()

                    #Calling the satisfaction function to see if you're satisfied
                    satisfaction1()

                #Gives you an error message if you don't choose short or long
                else:
                    print("\nPlease choose 'short' or 'long'!\n")
                    time.sleep(2)

        #Mass generate mode for the usernames
        elif userinput1 == "M":
            
            #Asks if want a long or short name
            userinput = input("\nDo you want short usernames or long ones? Type 'short' for short ones and 'long' for long ones: ")
        
            #If you choose short, this bit of code is executed
            if userinput == "short":
            
                #Creates a text file called names.txt if it doesn't exist already
                with open('names.txt', 'w') as file:

                    #Asks how many you want to generate
                    n=int(input("How many names would you like to generate: "))
                    
                    #Generates as many names as you want
                    for i in range(n):
                
                        #Chooses a random prefix from the list
                        prefix2 = random.choice(prefix1)

                        #Chooses a random root from the list
                        root2 = random.choice(root1)
        
                        #Creates the username
                        username = "%s%s\n" % (prefix2, root2)

                        #Writes to the names.txt file the randomly generated word
                        file.write(username)
                        file.close

                    print("\nYour names have been added to the 'names.txt' file!\n")
                
            #If you choose a long name, this is executed
            elif userinput == "long":
        
                #Creates a text file called names.txt if it doesn't exist already
                with open('names.txt', 'w') as file:

                    #Asks how many you want to generate
                    n=int(input("How many names would you like to generate: "))
            
                    #Generates as many names as you want
                    for i in range(n):
            
                        #Chooses a random prefix from the list
                        prefix2 = random.choice(prefix1)

                        #Chooses a random root from the list
                        root2 = random.choice(root1)
        
                        #Chooses a random suffix from the list
                        suffix2 = random.choice(suffix1)

                        #Generates the username
                        username = "%s%s%s\n" % (prefix2, root2 , suffix2)
        
                        #Writes the randomly generated word to the names.txt file
                        file.write(username)
                        file.close

                    print("\nYour names have been added to the 'names.txt' file!\n")

            #Gives you an error message if you don't choose short or long
            else:
                print("\nPlease choose 'short' or 'long'!")
                time.sleep(2)
                    
            
        #Gives you an error and restarts the program
        else:
            print("\nPlease choose 'M' or 'F'!")
            time.sleep(2)
            restart()

    #Starts this part of the program
    restart()

#---------------------REAL NAME MODE--------------------------------------------------------------------------------
#Real name mode
if mode == "R":

    #Restart function
    def restart1():

        #Choosing mass generate mode or few mode
        userinput1 = input("\nDo you want to mass generate names or do you only want a few? Type 'M' for mass generate, 'F' for few: ")

        #Mass generate mode
        if userinput1 == "M":

            #Creates a function to restart if I need to
            def restart3():
                
                #Asks if want a long or short name
                userinput2 = input("\nDo you want short usernames or long ones? Type short for 'short' ones and 'long' for long ones: ")

                #Making it all lowercase incase you accidentally type it in uppercase
                userinput = userinput2.lower()

                #If you choose short, this bit of code is executed
                if userinput == "short":
                
                    #Creates a text file called names.txt if it doesn't exist already
                    with open('names.txt', 'w') as file:

                        #Asks how many you want to generate
                        n=int(input("How many names would you like to generate: "))
                
                        #Generates as many names as you want
                        for i in range(n):
                    
                            #Creates the short real anme
                            realnameshort()

                            #Writes to the names.txt file the randomly generated word
                            file.write(short.username)
                            file.close

                        print("\nYour names have been added to the 'names.txt' file!\n")
                    
                #If you choose a long name, this is executed
                elif userinput == "long":
            
                    #Creates a text file called names.txt if it doesn't exist already
                    with open('names.txt', 'w') as file:

                        #Asks how many you want to generate
                        n=int(input("How many names would you like to generate: "))
                
                        #Generates as many names as you want
                        for i in range(n):
                
                            #Generating the username
                            realnamelong()

                            #Writes the randomly generated word to the names.txt file
                            file.write(long.username)
                            file.close

                            print("\nYour names have been added to the 'names.txt' file!\n")

                #If you don't choose short or long, this part of the program is restarted
                else:
                    print("\nPlease choose 'short' or 'long'!\n")
                    time.sleep(2)
                    restart3()

            #Calling this function so this part of the program runs   
            restart3()

        #If you choose few mode, this is executed
        elif userinput1 == "F":

            #Until you're happy, it'll keep generating new names
            while satisfaction == False:
        
                #Asks if want a long or short name
                userinput = input("Do you want a short name or a long one? Type 'short' for a short one and 'long' for a long one: ")
        
                #If you choose short, this bit of code is executed
                if userinput == "short":
            
                    #Generates the username
                    realnameshort()

                    #Asking if you're satisfied
                    satisfaction1()

                #If you choose a long name, this is executed
                elif userinput == "long":
        
                    #Creating the username
                    realnamelong()

                    #Prints the username
                    print(long.username)

                    #Asking if you're satisfied
                    satisfaction1()

                #Gives you an error message if you spell short or long wrong
                else:
                    print("\nPlease choose 'short' or 'long'!\n")
                    time.sleep(2)
            

        #Restarting it if you make an error
        else:
            print("\nPlease choose 'M' or 'F'!")
            time.sleep(2)
            restart1()

    #Calling the function so this section of code is ran
    restart1()