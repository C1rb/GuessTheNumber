#GuessTheNumber

print("GuessTheNumber Version 1.0")

#Main Code(Main loop, Main Game)
list1 = []

while True:
    element = str(input(" Enter any key to start the program :"))
    list1.append(element)
    choice = input(" Enter s to start the game and q to quit GuessTheNumber :")
    if choice == "s":
        print("Enter any number from 0 to 100, if you guess the number you win, if not the game would tell you if the number must be smaller or bigger.")
        from random import randrange
        n = randrange(100)
        while True:
            v = int(input())
            if n == v:
                print("You win!")
                break
            print("Smaller" if (n < v) else "Bigger")
            
    elif choice == "q":
        print("Closing Program")
        break;

    else:
        print("Please enter s or q only")
