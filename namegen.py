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
    
    print(prefix2.title() + root2)
    
    #Asks if you want to add numbers
    numbers = input("Would you like to add numbers to the name? Type Y for yes and N for no: ")
    
    #If you say yes, a random number is chosen to be added
    if numbers == "Y":
        numbers1 = [1 , 2, 3, 4, 5 , 6 ,7 ,8 ,9 ,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30 ,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]
        numbers2 = random.choice(numbers1)
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

    print(prefix2.title() + root2 + suffix2)

    numbers = input("Would you like to add numbers to the name? Type Y for yes and N for no: ")
    if numbers == "Y":
        numbers1 = [1 , 2, 3, 4, 5 , 6 ,7 ,8 ,9 ,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30 ,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]
        numbers2 = random.choice(numbers1)
        print(prefix2.title() + root2 + str(numbers2))

    



#Sets satisfaction to false
satisfaction = False

#Until you're happy, it'll keep generating new names
while satisfaction == False:
    
    #Asks if want a long or short name
    userinput = input("Do you want a short name or a long one? Type short for a short one and long for a long one: ")
    userinput1 = userinput.upper()
    
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


