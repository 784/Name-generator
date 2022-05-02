#Imports the random module
import random

#Choosing your mode
mode = input("\nDo you want to use username mode or real name mode? 'U' for username, 'R' for real name: ")

#Username mode code
if mode == "U":
    
    #Asks if you want to mass generate names
    userinput1 = input("\nDo you want to mass generate names or do you only want a few? Type 'M' for mass generate, 'F' for a few: ")
    
    #Only a few names are generated if you decide to do this
    if userinput1 == "F":
    
        #Creates a function to make the short names
        def short():
    
            #List of prefixes
            prefix1 = ["a", "de" , "dis", "en" , "ex" , "extra" , "hetero" "hyper" , "inter" , "intra" , "macro" , "micro" , "mono" , "non" , "omni" , "post" , "sub" , "sym" , "tele" , "trans" , "tri" , "un" , "uni" , "up" , "ante" , "anti" , "auto" , "co" , "com" , "con" , "contra" , "contro" , "re"]

            #Chooses a random prefix from the list
            prefix2 = random.choice(prefix1)

            #List of roots
            root1 = ["act", "aqu" , "arch" , "aster" , "aud" , "bio" , "cad" , "chrome" , "chron" , "corp" , "duc" , "dynamo" , "fund", "gamy" , "geo" , "gen" , "gin" , "grad" , "her" , "hydro" , "jug" , "jud" , "kine" , "labor"  "lect" , "leg" , "liter" , "magna" , "mania" , "mis" , "mort" , "nat" , "ocle" , "pac" , "pass" , "path" , "ped" , "pod" , "pel" , "puls" , "pend" , "pens" , "pond" , "pet" , "phobia" , "phon" , "pict" , "plac" , "plic" , "plex" , "ply" , "polis" , "polit" , "poly" , "port" , "punct" , "pung" , "point" , "quer" , "quis" , "reg" , "rect" , "right" , "rog" , "scope" , "scrib" , "scrip" , "sens" , "sent" , "sequi" , "secut" , "suit" , "sid" , "sed" , "sess" , "sim" , "sign" , "sys" , "sol" , "son" , "solv" , "spir" , "sta" , "sist" , "sti" , "struct" , "tract" , "ten" , "tain" , "tin" , "tend" , "ter" , "therm" , "urb" , "vac" , "void" , "val" , "valu" , "ven" , "vent" , "vita" , "volu" , "vers"]

            #Chooses a random root from the list
            root2 = random.choice(root1)
    
            #Prints the prefix with the first letter uppercase + the root
            print(prefix2.title() + root2)
    
            #Asks if you want to add numbers
            numbers = input("\nWould you like to add numbers to the name? Type 'Y' for yes and 'N' for no: ")
    
            #If you say yes, a random number is chosen to be added
            if numbers == "Y":
        
            #Chooses a random number from the list
                numbers2 = random.randint(1,99)

                #Prints the prefix with the first letter uppercase, the root, the suffix, and numbers
                print(prefix2.title() + root2 + str(numbers2))

    
        #Creates a function to make the long names
        def long():
    
            #List of prefixes
            prefix1 = ["a", "de" , "dis", "en" , "ex" , "extra" , "hetero" "hyper" , "inter" , "intra" , "macro" , "micro" , "mono" , "non" , "omni" , "post" , "sub" , "sym" , "tele" , "trans" , "tri" , "un" , "uni" , "up" , "ante" , "anti" , "auto" , "co" , "com" , "con" , "contra" , "contro" , "re"]

            #Chooses a random prefix from the list
            prefix2 = random.choice(prefix1)

            #List of roots
            root1 = ["act", "aqu" , "arch" , "aster" , "aud" , "bio" , "cad" , "chrome" , "chron" , "corp" , "duc" , "dynamo" , "fund", "gamy" , "geo" , "gen" , "gin" , "grad" , "her" , "hydro" , "jug" , "jud" , "kine" , "labor"  "lect" , "leg" , "liter" , "magna" , "mania" , "mis" , "mort" , "nat" , "ocle" , "pac" , "pass" , "path" , "ped" , "pod" , "pel" , "puls" , "pend" , "pens" , "pond" , "pet" , "phobia" , "phon" , "pict" , "plac" , "plic" , "plex" , "ply" , "polis" , "polit" , "poly" , "port" , "punct" , "pung" , "point" , "quer" , "quis" , "reg" , "rect" , "right" , "rog" , "scope" , "scrib" , "scrip" , "sens" , "sent" , "sequi" , "secut" , "suit" , "sid" , "sed" , "sess" , "sim" , "sign" , "sys" , "sol" , "son" , "solv" , "spir" , "sta" , "sist" , "sti" , "struct" , "tract" , "ten" , "tain" , "tin" , "tend" , "ter" , "therm" , "urb" , "vac" , "void" , "val" , "valu" , "ven" , "vent" , "vita" , "volu" , "vers"]

            #Chooses a random root from the list
            root2 = random.choice(root1)
    
            #List of suffixes
            suffix1 = ["acy" , "al", "ance" , "dom" , "er" , "or" , "ism" , "ist", "ity" , "ment" , "ness" , "ship", "ate" , "en", "ify" , "ize" , "able" , "ful" , "esqe" , "less"]
    
            #Chooses a random suffix from the list
            suffix2 = random.choice(suffix1)

            #Prints the prefix with the first letter uppercase, the root, and then the suffix
            print(prefix2.title() + root2 + suffix2)

            #Asks if you want to add numbers to the name
            numbers = input("\nWould you like to add numbers to the name? Type 'Y' for yes and 'N' for no: ")
    
            #If you say yes, a random number is chosen 
            if numbers == "Y":
        
                #Chooses a random number
                numbers2 = random.randint(1,99)

                #Prints the prefix with the first letter uppercase, the root, the suffix, and numbers
                print(prefix2.title() + root2 + suffix2 + str(numbers2))

    

        #Sets satisfaction to false
        satisfaction = False

        #Until you're happy, it'll keep generating new names
        while satisfaction == False:
    
            #Asks if want a long or short name
            userinput1 = input("Do you want a short name or a long one? Type 'short' for a short one and 'long' for a long one: ")
    
            #Making it lowercase
            userinput = userinput1.lower()
        
            #If you choose short, this bit of code is executed
            if userinput == "short":
        
                #Calls the short function created earlier
                short()
        
                #Asks if you're satisfied
                satisfied = input("\nAre you satisfied? Type Y for yes and N for no: ")
        
                #If you're satisfied, the loop is completed
                if satisfied == "Y":
                    satisfaction = True
        
                #If you're not, the loop continues
                else:
                    satisfaction = False

        #If you choose a long name, this is executed
        if userinput == "long":
    
            #Calls the long function created earlier
            long()

            #Asks if you're satisfied
            satisfied = input("\nAre you satisfied? Type Y for yes and N for no: ")
    
            #If you're satisfied, the loop is completed
            if satisfied == "Y":
                satisfaction = True

            #If you're not, the loop continues   
            else:
                satisfaction = False

    #Mass generate mode for the usernames
    if userinput1 == "M":

        #Asks if want a long or short name
        userinput1 = input("\nDo you want short usernames or long ones? Type 'short' for short ones and 'long' for long ones: ")
        
        #Making it lowercase
        userinput = userinput1.lower()
        
        #If you choose short, this bit of code is executed
        if userinput == "short":
        
            #Creates a text file called names.txt if it doesn't exist already
            with open('names.txt', 'w') as file:

                #Asks how many you want to generate
                n=int(input("How many names would you like to generate: "))
        
                #Generates as many names as you want
                for i in range(n):
            
                    #List of prefixes
                    prefix1 = ["a", "de" , "dis", "en" , "ex" , "extra" , "hetero" "hyper" , "inter" , "intra" , "macro" , "micro" , "mono" , "non" , "omni" , "post" , "sub" , "sym" , "tele" , "trans" , "tri" , "un" , "uni" , "up" , "ante" , "anti" , "auto" , "co" , "com" , "con" , "contra" , "contro" , "re"]

                    #Chooses a random prefix from the list
                    prefix2 = random.choice(prefix1)

                    #List of roots
                    root1 = ["act", "aqu" , "arch" , "aster" , "aud" , "bio" , "cad" , "chrome" , "chron" , "corp" , "duc" , "dynamo" , "fund", "gamy" , "geo" , "gen" , "gin" , "grad" , "her" , "hydro" , "jug" , "jud" , "kine" , "labor"  "lect" , "leg" , "liter" , "magna" , "mania" , "mis" , "mort" , "nat" , "ocle" , "pac" , "pass" , "path" , "ped" , "pod" , "pel" , "puls" , "pend" , "pens" , "pond" , "pet" , "phobia" , "phon" , "pict" , "plac" , "plic" , "plex" , "ply" , "polis" , "polit" , "poly" , "port" , "punct" , "pung" , "point" , "quer" , "quis" , "reg" , "rect" , "right" , "rog" , "scope" , "scrib" , "scrip" , "sens" , "sent" , "sequi" , "secut" , "suit" , "sid" , "sed" , "sess" , "sim" , "sign" , "sys" , "sol" , "son" , "solv" , "spir" , "sta" , "sist" , "sti" , "struct" , "tract" , "ten" , "tain" , "tin" , "tend" , "ter" , "therm" , "urb" , "vac" , "void" , "val" , "valu" , "ven" , "vent" , "vita" , "volu" , "vers"]

                    #Chooses a random root from the list
                    root2 = random.choice(root1)
    
                    #Creates the username
                    username = "%s%s\n" % (prefix2, root2)

                    #Writes to the names.txt file the randomly generated word
                    file.write(username)
                    file.close

                print("\nYour names have been added to the 'names.txt' file!\n")
            
        #If you choose a long name, this is executed
        if userinput == "long":
    
            #Creates a text file called names.txt if it doesn't exist already
            with open('names.txt', 'w') as file:

                #Asks how many you want to generate
                n=int(input("How many names would you like to generate? "))
        
                #Generates as many names as you want
                for i in range(n):
           
                    #List of prefixes
                    prefix1 = ["a", "de" , "dis", "en" , "ex" , "extra" , "hetero" "hyper" , "inter" , "intra" , "macro" , "micro" , "mono" , "non" , "omni" , "post" , "sub" , "sym" , "tele" , "trans" , "tri" , "un" , "uni" , "up" , "ante" , "anti" , "auto" , "co" , "com" , "con" , "contra" , "contro" , "re"]

                    #Chooses a random prefix from the list
                    prefix2 = random.choice(prefix1)

                    #List of roots
                    root1 = ["act", "aqu" , "arch" , "aster" , "aud" , "bio" , "cad" , "chrome" , "chron" , "corp" , "duc" , "dynamo" , "fund", "gamy" , "geo" , "gen" , "gin" , "grad" , "her" , "hydro" , "jug" , "jud" , "kine" , "labor"  "lect" , "leg" , "liter" , "magna" , "mania" , "mis" , "mort" , "nat" , "ocle" , "pac" , "pass" , "path" , "ped" , "pod" , "pel" , "puls" , "pend" , "pens" , "pond" , "pet" , "phobia" , "phon" , "pict" , "plac" , "plic" , "plex" , "ply" , "polis" , "polit" , "poly" , "port" , "punct" , "pung" , "point" , "quer" , "quis" , "reg" , "rect" , "right" , "rog" , "scope" , "scrib" , "scrip" , "sens" , "sent" , "sequi" , "secut" , "suit" , "sid" , "sed" , "sess" , "sim" , "sign" , "sys" , "sol" , "son" , "solv" , "spir" , "sta" , "sist" , "sti" , "struct" , "tract" , "ten" , "tain" , "tin" , "tend" , "ter" , "therm" , "urb" , "vac" , "void" , "val" , "valu" , "ven" , "vent" , "vita" , "volu" , "vers"]

                    #Chooses a random root from the list
                    root2 = random.choice(root1)
    
                    #List of suffixes
                    suffix1 = ["acy" , "al", "ance" , "dom" , "er" , "or" , "ism" , "ist", "ity" , "ment" , "ness" , "ship", "ate" , "en", "ify" , "ize" , "able" , "ful" , "esqe" , "less"]
    
                    #Chooses a random suffix from the list
                    suffix2 = random.choice(suffix1)

                    #Generates the username
                    username = "%s%s%s\n" % (prefix2, root2 , suffix2)
    
                    #Writes the randomly generated word to the names.txt file
                    file.write(username)
                    file.close

                print("\nYour names have been added to the 'names.txt' file!\n")


#Real name mode
if mode == "R":

    #Choosing mass generate mode or few mode
    userinput1 = input("\nDo you want to mass generate names or do you only want a few? Type 'M' for mass generate, 'F' for a few: ")

    #Mass generate mode
    if userinput1 == "M":

        #Asks if want a long or short name
        userinput = input("\nDo you want short usernames or long ones? Type 'short' for short ones and 'long' for long ones: ")
    
        #If you choose short, this bit of code is executed
        if userinput == "short":
        
            #Creates a text file called names.txt if it doesn't exist already
            with open('names.txt', 'w') as file:

                #Asks how many you want to generate
                n=int(input("How many names would you like to generate? "))
        
                #Generates as many names as you want
                for i in range(n):
            
                    #List of first names 
                    firstname1 = ["Ava", "Amelia", "Abigail", "Alexander", "Aiden", "Anthony", "Emma", "Evelyn", "Emily", "Elijah", "Ethan", "Ezra", "James", "Robert", "John", "Michael", "William", "David", "Richard", "Joseph", "Thomas","Charles", "Christopher", "Matthew", "Donald", "Anthony", "Steven", "Paul","Joshua", "Kevin", "Brian", "George", "Edward", "Timothy", "Jason", "Jeffrey", "Ryan", "Jacob", "Gary", "Eric","Jonathan", "Stephen", "Larry", "Justin", "Scott", "Brandon", "Benjamin","Samuel", "Frank", "Alexander", "Raymond", "Patrick", "Jack", "Jerry", "Tyler", "Mary", "Patricia", "Jennifer", "Linda","Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen", "Nancy","Lisa", "Betty", "Margaret", "Sandra", "Ashley", "Kimberly", "Emily", "Donna", "Michelle", "Dorothy", "Carol", "Amanda","Melissa", "Deborah", "Stephanie", "Rebecca", "Sharon", "Laura", "Cynthia","Amy", "Angela", "Helen", "Anna", "Brenda", "Pamela", "Nicole", "Samantha", "Christine", "Debra", "Rachel", "Catherine","Carolyn", "Janet", "Ruth", "Maria", "Heather", "Diane" , "Will"]
    
                    #Picks a random first name from the list
                    firstname2 = random.choice(firstname1)

                    #List of last names
                    lastname1 = ["Smith", "Johnson" , "Williams" , "Brown" , "White" , "Jones" , "Garcia", "Miller", "Davis" , "Lopez" , "Gonzales" , "Wilson" , "Anderson" , "Thomas" , "Taylor" , "Moore" , "Jackson" , "Martin", "Lee" , "Thompson" , "Perez" , "Harris" , "Clark" , "Ramirez", "Lewis", "Robinson" , "Walker" , "Young" , "Allen" , "King" , "Wright" , "Scott" , "Torres" , "Nguyen" , "Hill", "Flores" , "Green" , "Adams" , "Nelson" , "Baker" , "Hall", "Rivera", "Campbell" , "Carter" , "Roberts" , "Gomez" , "Phillips" , "Evans" , "Turner" , "Diaz" , "Parker" , "Cruz", "Edwards" , "Collins" , "Stewart" , "Morris" , "Morales" , "Murphy", "Cook", "Rogers" , "Ortiz" , "Morgan" , "Cooper" , "Peterson" , "Bailey" , "Reed" , "Kelly" , "Howard" , "Ramos" , "Cox" , "Richardson" , "Watson", "Brooks" , "Chavez" , "Bennett" , "Wood" , "Mendoza" , "Hughes", "Price", "Sanders" , "Myers" , "Long" , "Ross" , "Foster" , "Jimenez"]

                    #Picks a random last name from the list
                    lastname2 = random.choice(lastname1)
    
                    #Creates the username
                    username = "%s %s\n" % (firstname2, lastname2)

                    #Writes to the names.txt file the randomly generated word
                    file.write(username)
                    file.close

                print("\nYour names have been added to the 'names.txt' file!\n")
            
        #If you choose a long name, this is executed
        if userinput == "long":
    
            #Creates a text file called names.txt if it doesn't exist already
            with open('names.txt', 'w') as file:

                #Asks how many you want to generate
                n=int(input("How many names would you like to generate? "))
        
                #Generates as many names as you want
                for i in range(n):
           
                    #List of first names 
                    firstname1 = ["Ava", "Amelia", "Abigail", "Alexander", "Aiden", "Anthony", "Emma", "Evelyn", "Emily", "Elijah", "Ethan", "Ezra", "James", "Robert", "John", "Michael", "William", "David", "Richard", "Joseph", "Thomas","Charles", "Christopher", "Matthew", "Donald", "Anthony", "Steven", "Paul","Joshua", "Kevin", "Brian", "George", "Edward", "Timothy", "Jason", "Jeffrey", "Ryan", "Jacob", "Gary", "Eric","Jonathan", "Stephen", "Larry", "Justin", "Scott", "Brandon", "Benjamin","Samuel", "Frank", "Alexander", "Raymond", "Patrick", "Jack", "Jerry", "Tyler", "Mary", "Patricia", "Jennifer", "Linda","Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen", "Nancy","Lisa", "Betty", "Margaret", "Sandra", "Ashley", "Kimberly", "Emily", "Donna", "Michelle", "Dorothy", "Carol", "Amanda","Melissa", "Deborah", "Stephanie", "Rebecca", "Sharon", "Laura", "Cynthia","Amy", "Angela", "Helen", "Anna", "Brenda", "Pamela", "Nicole", "Samantha", "Christine", "Debra", "Rachel", "Catherine","Carolyn", "Janet", "Ruth", "Maria", "Heather", "Diane"]
    
                    #Picks a random first name from the list
                    firstname2 = random.choice(firstname1)

                    #List of middle names
                    middlename1 = ["Penelope" , "Elizabeth" , "Grace" , "Hazel" , "Violet" , "Ivy" , "Anna" , "Sadie" , "Iris" , "Faith" , "Olive" , "Rosalie" , "Willa" , "Joy" , "Aurelia" , "Jane" , "Myra" , "Priscilla" , "Mina" , "Theo" , "Wesley" , "Harrison" , "Luke" , "David" , "Charles" , "Calvin" , "Timothy" , "Carlos" , "Finn" , "Alan" , "Leon" , "Grant" , "Jax" , "Chance" , "Kane" , "Hector" , "Dax" , "Bruce" , "Jeremiah" , "Clay" , "Wayne" , "Trent" , "Marc" , "Steve" , "Kent" , "Aris" , "Dan" , "Rush" , "Penn" , "Burke" , "Niles" , "Jai" , "Roan" , "Clint" , "Shai" , "Kolt" ]

                    #Picks a random middle name from the list
                    middlename2 = random.choice(middlename1)

                    #List of last names
                    lastname1 = ["Smith", "Johnson" , "Williams" , "Brown" , "White" , "Jones" , "Garcia", "Miller", "Davis" , "Lopez" , "Gonzales" , "Wilson" , "Anderson" , "Thomas" , "Taylor" , "Moore" , "Jackson" , "Martin", "Lee" , "Thompson" , "Perez" , "Harris" , "Clark" , "Ramirez", "Lewis", "Robinson" , "Walker" , "Young" , "Allen" , "King" , "Wright" , "Scott" , "Torres" , "Nguyen" , "Hill", "Flores" , "Green" , "Adams" , "Nelson" , "Baker" , "Hall", "Rivera", "Campbell" , "Carter" , "Roberts" , "Gomez" , "Phillips" , "Evans" , "Turner" , "Diaz" , "Parker" , "Cruz", "Edwards" , "Collins" , "Stewart" , "Morris" , "Morales" , "Murphy", "Cook", "Rogers" , "Ortiz" , "Morgan" , "Cooper" , "Peterson" , "Bailey" , "Reed" , "Kelly" , "Howard" , "Ramos" , "Cox" , "Richardson" , "Watson", "Brooks" , "Chavez" , "Bennett" , "Wood" , "Mendoza" , "Hughes", "Price", "Sanders" , "Myers" , "Long" , "Ross" , "Foster" , "Jimenez"]

                    #Picks a random last name from the list
                    lastname2 = random.choice(lastname1)
    
                    #Creates the username
                    username = "%s %s %s\n" % (firstname2, middlename2, lastname2)

                    #Writes the randomly generated word to the names.txt file
                    file.write(username)
                    file.close

                print("\nYour names have been added to the 'names.txt' file!\n")

    #If you choose few mode, this is executed
    if userinput1 == "F":

        #Sets satisfaction to false
        satisfaction = False

        #Until you're happy, it'll keep generating new names
        while satisfaction == False:
    
            #Asks if want a long or short name
            userinput = input("Do you want a short name or a long one? Type 'short' for a short one and 'long' for a long one: ")
    
            #If you choose short, this bit of code is executed
            if userinput == "short":
        
                #List of first names 
                firstname1 = ["Ava", "Amelia", "Abigail", "Alexander", "Aiden", "Anthony", "Emma", "Evelyn", "Emily", "Elijah", "Ethan", "Ezra", "James", "Robert", "John", "Michael", "William", "David", "Richard", "Joseph", "Thomas","Charles", "Christopher", "Matthew", "Donald", "Anthony", "Steven", "Paul","Joshua", "Kevin", "Brian", "George", "Edward", "Timothy", "Jason", "Jeffrey", "Ryan", "Jacob", "Gary", "Eric","Jonathan", "Stephen", "Larry", "Justin", "Scott", "Brandon", "Benjamin","Samuel", "Frank", "Alexander", "Raymond", "Patrick", "Jack", "Jerry", "Tyler", "Mary", "Patricia", "Jennifer", "Linda","Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen", "Nancy","Lisa", "Betty", "Margaret", "Sandra", "Ashley", "Kimberly", "Emily", "Donna", "Michelle", "Dorothy", "Carol", "Amanda","Melissa", "Deborah", "Stephanie", "Rebecca", "Sharon", "Laura", "Cynthia","Amy", "Angela", "Helen", "Anna", "Brenda", "Pamela", "Nicole", "Samantha", "Christine", "Debra", "Rachel", "Catherine","Carolyn", "Janet", "Ruth", "Maria", "Heather", "Diane" , "Will"]
    
                #Picks a random first name from the list
                firstname2 = random.choice(firstname1)

                #List of last names
                lastname1 = ["Smith", "Johnson" , "Williams" , "Brown" , "White" , "Jones" , "Garcia", "Miller", "Davis" , "Lopez" , "Gonzales" , "Wilson" , "Anderson" , "Thomas" , "Taylor" , "Moore" , "Jackson" , "Martin", "Lee" , "Thompson" , "Perez" , "Harris" , "Clark" , "Ramirez", "Lewis", "Robinson" , "Walker" , "Young" , "Allen" , "King" , "Wright" , "Scott" , "Torres" , "Nguyen" , "Hill", "Flores" , "Green" , "Adams" , "Nelson" , "Baker" , "Hall", "Rivera", "Campbell" , "Carter" , "Roberts" , "Gomez" , "Phillips" , "Evans" , "Turner" , "Diaz" , "Parker" , "Cruz", "Edwards" , "Collins" , "Stewart" , "Morris" , "Morales" , "Murphy", "Cook", "Rogers" , "Ortiz" , "Morgan" , "Cooper" , "Peterson" , "Bailey" , "Reed" , "Kelly" , "Howard" , "Ramos" , "Cox" , "Richardson" , "Watson", "Brooks" , "Chavez" , "Bennett" , "Wood" , "Mendoza" , "Hughes", "Price", "Sanders" , "Myers" , "Long" , "Ross" , "Foster" , "Jimenez"]

                #Picks a random last name from the list
                lastname2 = random.choice(lastname1)
    
                #Creates the username
                username = "%s %s" % (firstname2, lastname2)

                #Prints the name
                print(username)
        
                #Asks if you're satisfied
                satisfied = input("\nAre you satisfied? Type Y for yes and N for no: ")
        
                #If you're satisfied, the loop is completed
                if satisfied == "Y":
                    satisfaction = True
        
                #If you're not, the loop continues
                else:
                    satisfaction = False

            #If you choose a long name, this is executed
            if userinput == "long":
    
                #List of first names 
                firstname1 = ["Ava", "Amelia", "Abigail", "Alexander", "Aiden", "Anthony", "Emma", "Evelyn", "Emily", "Elijah", "Ethan", "Ezra", "James", "Robert", "John", "Michael", "William", "David", "Richard", "Joseph", "Thomas","Charles", "Christopher", "Matthew", "Donald", "Anthony", "Steven", "Paul","Joshua", "Kevin", "Brian", "George", "Edward", "Timothy", "Jason", "Jeffrey", "Ryan", "Jacob", "Gary", "Eric","Jonathan", "Stephen", "Larry", "Justin", "Scott", "Brandon", "Benjamin","Samuel", "Frank", "Alexander", "Raymond", "Patrick", "Jack", "Jerry", "Tyler", "Mary", "Patricia", "Jennifer", "Linda","Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen", "Nancy","Lisa", "Betty", "Margaret", "Sandra", "Ashley", "Kimberly", "Emily", "Donna", "Michelle", "Dorothy", "Carol", "Amanda","Melissa", "Deborah", "Stephanie", "Rebecca", "Sharon", "Laura", "Cynthia","Amy", "Angela", "Helen", "Anna", "Brenda", "Pamela", "Nicole", "Samantha", "Christine", "Debra", "Rachel", "Catherine","Carolyn", "Janet", "Ruth", "Maria", "Heather", "Diane"]
    
                #Picks a random first name from the list
                firstname2 = random.choice(firstname1)

                #List of middle names
                middlename1 = ["Penelope" , "Elizabeth" , "Grace" , "Hazel" , "Violet" , "Ivy" , "Anna" , "Sadie" , "Iris" , "Faith" , "Olive" , "Rosalie" , "Willa" , "Joy" , "Aurelia" , "Jane" , "Myra" , "Priscilla" , "Mina" , "Theo" , "Wesley" , "Harrison" , "Luke" , "David" , "Charles" , "Calvin" , "Timothy" , "Carlos" , "Finn" , "Alan" , "Leon" , "Grant" , "Jax" , "Chance" , "Kane" , "Hector" , "Dax" , "Bruce" , "Jeremiah" , "Clay" , "Wayne" , "Trent" , "Marc" , "Steve" , "Kent" , "Aris" , "Dan" , "Rush" , "Penn" , "Burke" , "Niles" , "Jai" , "Roan" , "Clint" , "Shai" , "Kolt" ]

                #Picks a random middle name from the list
                middlename2 = random.choice(middlename1)

                #List of last names
                lastname1 = ["Smith", "Johnson" , "Williams" , "Brown" , "White" , "Jones" , "Garcia", "Miller", "Davis" , "Lopez" , "Gonzales" , "Wilson" , "Anderson" , "Thomas" , "Taylor" , "Moore" , "Jackson" , "Martin", "Lee" , "Thompson" , "Perez" , "Harris" , "Clark" , "Ramirez", "Lewis", "Robinson" , "Walker" , "Young" , "Allen" , "King" , "Wright" , "Scott" , "Torres" , "Nguyen" , "Hill", "Flores" , "Green" , "Adams" , "Nelson" , "Baker" , "Hall", "Rivera", "Campbell" , "Carter" , "Roberts" , "Gomez" , "Phillips" , "Evans" , "Turner" , "Diaz" , "Parker" , "Cruz", "Edwards" , "Collins" , "Stewart" , "Morris" , "Morales" , "Murphy", "Cook", "Rogers" , "Ortiz" , "Morgan" , "Cooper" , "Peterson" , "Bailey" , "Reed" , "Kelly" , "Howard" , "Ramos" , "Cox" , "Richardson" , "Watson", "Brooks" , "Chavez" , "Bennett" , "Wood" , "Mendoza" , "Hughes", "Price", "Sanders" , "Myers" , "Long" , "Ross" , "Foster" , "Jimenez"]

                #Picks a random last name from the list
                lastname2 = random.choice(lastname1)
    
                #Creates the username
                username = "%s %s %s" % (firstname2, middlename2, lastname2)

                #Prints the username
                print(username)

                #Asks if you're satisfied
                satisfied = input("\nAre you satisfied? Type Y for yes and N for no: ")
    
                #If you're satisfied, the loop is completed
                if satisfied == "Y":
                    satisfaction = True

                #If you're not, the loop continues   
                else:
                    satisfaction = False

   

