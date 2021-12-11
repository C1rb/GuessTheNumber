#GuessTheNumber

print("GuessTheNumber Version 1.2")

#Main Code(Main loop, Main Game, Scoring system, Quiting interface, About section, Text Interface)
list1 = []

while True:
    element = str(input(" Enter any key to start the program :"))
    list1.append(element)
    choice = input(" Enter 's' to start the game and 'q' to quit GuessTheNumber :")
    if choice == "s":
        print("------------------------------------------------------------------------------")
        print("Enter any number from 0 to 100, if you guess the number you win, if not the game would tell you if the number must be smaller or bigger.")
        print("SCORING SYSTEM: If your score is higher the lower your points are while if the score is lower the higher score you have.")
        print("------------------------------------------------------------------------------")
        from random import randrange
        n = randrange(100)
        score = 0
        while True:
            v = int(input())
            if n == v:
                print("You win!")
                print("Your final score is : " + str(score))
                break
            print("Smaller" if (n < v) else "Bigger")
            if n < v or n > v:
                score = score + 1
            print("Your current score is :" + str(score))

    elif choice == "q":
        element = str(input(" Enter any key to end the program :"))
        list1.append(element)
        choice = input(" Are you sure to quit, enter any key if yes or 'a' for about : ")
        if choice == "a":
            print("------------------------------------------------------------------------------")
            print("ABOUT: GuessTheNumber is a simple game made in python, it has simple mechanics that would make the game a little bit more fun than usual.")
            print("Created by C1rb as an open source python game, Feel free to use the code and improve my code, Cheers-C1rb")
            print("------------------------------------------------------------------------------")

        else:
            print("Closing Program")
            break
    
    else:
        print("Please enter s or q only")
