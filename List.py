import time
from random import uniform
import random
import webbrowser

incorect = (0)

def slowprint(msg):
    for letter in msg:
        time.sleep(uniform(0.04, 0.06))
        print(letter,end="")
    print()
    
List = []
def plist(Var):
    j = 0
    for x in Var:
        j += 1
        slowprint(str(j) + ". " + x)
    
def slist(li):
    f = open("ListSave.txt","r+")
    f.truncate(0)
    for i in li:
        f.write(i+"\n")
    
def rlist():
    f = open("ListSave.txt","r+")
    f1 = f.readlines()
    ret = []
    for i in f1:
        ret.append(i.replace("\n",""))
    return ret

running = True
while running == True:
    List = rlist()
    slowprint("Do you want to add, remove, reset, save or quit?")
    q1 = input ("> ").lower()
    if q1 == "add" or q1 == "a":
        loop1 = True
        while loop1 == True:
            slowprint("What do you want to add? ")
            q2 = input ("> ")
            l = len(List) + 1
            List.append(q2)
            plist(List)
            slist(List)
            slowprint("The item " + str(q2) + " has been added!")
            slowprint("Would you like to add something else?")
            q4 = input("> ").lower()
            if q4 == "yes" or q4 == "ya" or q4 == "yeh":
                slowprint("Ok then")
            elif q4 == "no" or "na" or "nah":
                loop1 = False
    elif q1 == "remove" or q1 == "r":
        loop2 = True
        while loop2 == True:
            if List == []:
                slowprint("There isnt anything on the list ya doink")
                loop2 = False
            else:
                slowprint("Here is the list if you forgot it")
                time.sleep(0.5)
                plist(List)
                time.sleep(0.5)
                slowprint("Please type something on the list that you want to remove.")
                slowprint("Or you can type reset to delete the entire List.")
                q3 = input("> ").lower()
                if q3 in List:
                    slowprint("Removing")
                    time.sleep(0.3)
                    print(".")
                    time.sleep(0.3)
                    print(".")
                    time.sleep(0.3)
                    print(".")
                    time.sleep(0.3)
                    List.remove(q3)
                    time.sleep(0.5)
                    slowprint("The item " + str(q3) + " has been removed!")
                    plist(List)
                    slist(List)
                    slowprint("Do you want to remove something else?")
                    q6 = input("> ")
                    if q6 == "yes" or q6 == "yah" or q6 == "ya" or q6 == "yeh":
                        slowprint("Ok then")
                    elif q4 == "no" or q6 == "na" or q6 == "nah":
                        loop2 = False
    elif q1 == "save":
            slowprint("Your current list will be put in ListSave.txt")
            slowprint("Saving in 3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            slowprint ("Saving!")
            plist(List)
            slist(List)
            slowprint ("Save Completed")
    elif q1 == "reset" or "r":
        slowprint("Are you sure you want to reset your entire list?")
        time.sleep(0.65)
        slowprint("This action is irreversable")
        q7 = input("> ")
        if q7 == "yes" or "ya" or "yeh" or "yah":
            slowprint("You list will be reset in 3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            print("0")
            time.sleep(0.3)
            slowprint("Your list has been reset.")
            List = 0
            slist(List)
    elif q1 == "quit":
            running = False
    else:
            slowprint ("Please enter your input correctly")
            incorect = incorect + 1
            if incorect >= 3:
                slowprint("You have typed in something that this program cannot understand " + str(incorect) + " times")
                slowprint("If you are having problems please e-mail me at hbolingbroke@connnect.kellettschool.com or harry.bolingbroke@gmail.com")
                slowprint("Would you like me to take me to your G-Mail browser now?")
                q5 = input("> ").lower()
                if q5 == "yes" or q5 == "yah" or q5 == "ya" or q5 == "yeh":
                    webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=GTvVlcSBpgVhwlBpfXdcKKHqhxBRTWQxzfTMpsvjqwqCXfWgmStdbzKsdCgpVRXjrDvXhdmdrVbrQ")
                elif q5 == "no" or q5 == "na" or q5 == "nah" or q5 == "nope":
                    slowprint("Please enter your input correctly next time!")
            time.sleep (0.5123)