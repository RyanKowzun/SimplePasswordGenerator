#Generate a strong password

#Import the random library
import random

start = 0

while True:
    if start != 1:
        #Ask the user how long their strong password should be
        pw_length = int(input("How many characters do you want in your strong password?  "))

    #Check to see if the entry is below 10 or over 50
    if pw_length < 10:
        print("Strong passwords should be at least 10 characters!")
        pw_length = 10
    elif pw_length > 50:
        print("That's a bit long, let's go with 50")
        pw_length = 50
   
    #start with a blank password
    password = ""

    #Create the possibilities to choose from
    lowercase="abcdefghijklmnopqrstuvwxyz"
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    specialChars = "1234567890~!@$#%^&+()_[{]}"

    #Build the password
    for i in range(pw_length):
        randchar = random.choice(lowercase + uppercase + specialChars)
        password = password + randchar

    print("Your password:  ", password)

    #Loop to restart or end 
    do_run = input("Restart? y/n: ")
    if do_run == 'y':
        pass
    elif do_run == 'n':
        break
    else:
        print ("Invalid Input")
        break
