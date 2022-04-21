#Imports the random module
import random

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
    numbers = input("Would you like to add numbers to the name? Type Y for yes and N for no: ")
    
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
    numbers = input("Would you like to add numbers to the name? Type Y for yes and N for no: ")
    
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
    userinput = input("Do you want a short name or a long one? Type short for a short one and long for a long one: ")
    
    #If you choose short, this bit of code is executed
    if userinput == "short":
        
        #Calls the short function created earlier
        short()
        
        satisfied = input("Are you satisfied? Type Y for yes and N for no: ")
        
        if satisfied == "Y":
            satisfaction = True
        
        else:
            satisfaction = False

    #If you choose a long name, this is executed
    if userinput == "long":
    
        #Calls the long function created earlier
        long()

        #Asks if you're satisfied
        satisfied = input("Are you satisfied? Type Y for yes and N for no: ")
    
        #If you're satisfied, the loop is completed
        if satisfied == "Y":
            satisfaction = True

        #If you're not, the loop continues   
        else:
            satisfaction = False


