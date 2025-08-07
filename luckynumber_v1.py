import random
import time
import pyttsx3
import pygame
pygame.init()
engine=pyttsx3.init()
engine.setProperty('rate',110)
statements = [
    "Sharpening the dice",
    "Finding your lucky number",
    "Rolling the magic",
    "Summoning the luck gods",
    "Giving fate a little nudge",
    "Whispering secrets to the numbers",
    "Rolling destiny into motion",
    "Letting the universe decide",
    "Shaking up the probability pool",
    "Spinning the wheel of fortune",
    "Unlocking the mystery digits",
    "Tossing the cosmic dice",
    "Calling upon the randomness spirits",
    "Flipping fate’s coin",
    "Channeling the power of unpredictability"
]
pointscore=0
highscore=0

def rules():
    time.sleep(1)
    print("             RULES")
    print("You have to guess the number to win","Attempts are limited",sep="\n")
    engine.say("You have to guess the number to win")
    engine.runAndWait()
    engine.say("Attempts are limited")
    engine.runAndWait()
    print("\nHARD -> 3","MEDIUM -> 4","EASY ->5","Or you can create a random level",sep="\n")
    time.sleep(1)
    engine.say("For Hard level you will get 3 attempts and for medium level you will get 4 attempts and for easy you will get 5 attempts")
    engine.runAndWait()
    engine.say("You can also design a custom level as per your choice")
    engine.runAndWait()
    print("There are HINTS available for your help\n")
    engine.say("There are HINTS available for your help")
    engine.runAndWait()
    print('"CLOSE" means: Number is 3 numbers ahead or back','"VERY CLOSE" means: Number is just 1 number ahead or back','"Very Far" and "Behind" means: Number is atleast 5-10 numbers ahead or back.',sep="\n")
    time.sleep(1)
    engine.say('"CLOSE" means: Number is 3 numbers ahead or back')
    engine.runAndWait()
    engine.say('"VERY CLOSE" means: Number is just 1 number ahead or back')
    engine.runAndWait()
    engine.say('"Very Far" and Behind means: Number is atleast 5-10 numbers ahead or back.')
    engine.runAndWait()
    print("\nPOINT SYSTEM")
    print("WIN -> 50","EVERY ATTEMPT REMAINING x 10",sep="\n")
    time.sleep(1)
    engine.say("Point system")
    engine.runAndWait()
    engine.say("For every win you will recieve 50 points and your remaining attempts will be multiplied by 10 and be added to your score.")
    engine.runAndWait()
    input("\nPress enter to return back.")
    main()

def levels():
    time.sleep(1)
    print("\nCHOOSE YOUR LEVEL.\n")
    print("HARD -> 1-100","MEDIUM -> 1-30","EASY -> 1-10",sep="\n")
    time.sleep(4)
    print("\nPress 1 for HARD","Press 2 for MEDIUM","Press 3 for EASY","Press 4 for Custom LEVEL",sep="\n")
    time.sleep(2.3)
    try:
        levelchoice=int(input("Your choice :"))
    except:
        print("Invalid input! Please enter a number.")
    return levelchoice
    
def levelmaker():
    levelchoice=levels() #Using the choice input given by the user
    if levelchoice == 1:
        num = list(range(1, 101))   # hard
        attempts=31
    elif levelchoice == 2:
        num = list(range(1, 31))    # medium
        attempts=4
    elif levelchoice == 3:
        num = list(range(1, 11))    # easy
        attempts=5
    elif levelchoice == 4:
        print("\tCUSTOM LEVEL")
        userchoicenum=int(input('Enter the number limit "HIGHER END" :'))
        num = list(range(1,userchoicenum+1))
        attempts=int(input("Enter the number of ATTEMPTS :"))
    else:
        print("Wrong choice! Defaulting to EASY mode.")
        num = list(range(1, 11))
        attempts=5
    gameplay(num,attempts)

def display_highscore():
    global pointscore,highscore
    with open("luckynumber.txt","r") as file:
        currenthighscore=file.read()
    print(f"The current Highscore is ={currenthighscore}")
    input("\nPress enter to return back.")
    main()
    
def update_highscore():
    global pointscore,highscore
    with open("luckynumber.txt","r+") as file:
            try:
                file.seek(0) #make the cursor move to the 1st index of the file.
                highscore=int(file.read())
            except:
                highscore=0
    if(pointscore>highscore):
        highscore=pointscore
        with open("luckynumber.txt","r+") as file:
            file.seek(0)
            file.truncate(0) #Removes all the content of the file.
            file.write(str(highscore)) 
            file.flush() #Make sure the content is properly written in file. 
    
def gameplay(num,attempts):
    global pointscore,highscore
    s=pygame.mixer.Sound(r'E:\lucknumber VOICE,SOUND DATA\suspense-sound-effect-287450.mp3')
    s.play()
    print(random.choice(statements),end="")
    for i in range(7):
        print(".",end="",flush=True)
        time.sleep(1)
    print("\n")
    lucky_number=random.choice(num)
    time.sleep(2)
    s=pygame.mixer.Sound(r'E:\lucknumber VOICE,SOUND DATA\drone-high-tension-and-suspense-background-162365.mp3')
    channel1=s.play()  #created a channel to control music play
    while attempts!=0:
        try:
            userchoice=int(input("Enter the number: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        differnce=abs(userchoice-lucky_number)
        if userchoice==lucky_number:
            # channel1.stop()
            s=pygame.mixer.Sound(r'E:\lucknumber VOICE,SOUND DATA\level-win-6416.mp3')
            s.play()
            time.sleep(2)
            print("You did it","YOU WON",sep="\n")
            attempts=attempts-1
            pointscore=pointscore+50
            pointscore=pointscore+attempts*10
            break
        elif userchoice>lucky_number:
            time.sleep(2)
            # channel1.stop()
            s=pygame.mixer.Sound(r"E:\lucknumber VOICE,SOUND DATA\fail-234710.mp3")
            s.play()
            if differnce<=1:
                print("WRONG ANSWER","-> HINT: VERY CLOSE",sep=" ")
            elif differnce<=3:
                print("WRONG ANSWER","-> HINT: CLOSE",sep=" ")
            else:
                print("WRONG ANSWER","-> HINT: VERY FAR",sep=" ")
            attempts=attempts-1
            print(f"Attempts remaining :{attempts}")
            time.sleep(2)
        elif userchoice<lucky_number:
            time.sleep(2)
            # channel1.stop()
            s=pygame.mixer.Sound(r"E:\lucknumber VOICE,SOUND DATA\fail-234710.mp3")
            channel2=s.play()
            if differnce<=1:
                print("WRONG ANSWER","-> HINT: VERY CLOSE",sep=" ")
            elif differnce<=3:
                print("WRONG ANSWER","-> HINT: CLOSE",sep=" ")
            else:
                print("WRONG ANSWER","-> HINT: VERY BEHIND",sep=" ") 
            attempts=attempts-1  
            print(f"Attempts remaining :{attempts}") 
            time.sleep(2)
    else:
        s=pygame.mixer.Sound(r'E:\lucknumber VOICE,SOUND DATA\game-over-deep-male-voice-clip-352695.mp3')
        s.play()
        print(f"You lost! Better luck next time. The lucky number was {lucky_number}.")
    play_again()

def play_again():
    time.sleep(1)
    print("Do you wish to play again or EXIT")
    print("Enter 1 to Continue.", "Enter 2 for EXIT","Enter 3 to go back to main menu",sep="\n")
    time.sleep(1)
    des = int(input())
    if des == 1:
        levelmaker() # Restart's the game
    elif des == 3:
        main()
    else:
        print(f"Your current score is {pointscore}",f"Highest score is {highscore}")
        time.sleep(1)
        print("Thanks for playing!") #End's the living
    
def main():
    print("Press 1 to view RULES","Press 2 to continue to Gameplay","Press 3 to view current HIGHSCORE","Press 4 to Quit",sep="\n")
    choice=int(input("Your Response : "))
    match choice:
        case 1:
            rules()
        case 2:
            levelmaker()
        case 3:
            display_highscore()
        case 4:                                          #have to fix this end issue
            print("THANKS FOR PLAYING")
    update_highscore()
s=pygame.mixer.Sound(r'E:\lucknumber VOICE,SOUND DATA\gamestart-272829.mp3')
s.play()
print("Welcome to LUCKY NUMBER Game! 🎲")
engine.say("Welcome to LUCKY NUMBER Game!")
engine.runAndWait()
main()
play_again()
