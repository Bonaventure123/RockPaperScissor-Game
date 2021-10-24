import random
def userInput():
    print("""
Options - 
1. Rock
2. Paper
3. Scissor""")
    Option1 = int(input("choice: "))

    result(Option1-1)

def result(userOption):
    pchoice = random.randint(0, 2)
    print("user's choce :", choices[userOption])
    print("pc choice: ", choices[pchoice] )


    if userOption == pchoice:
        print("its a draw")
    elif userOption == 0:
        if pchoice == 1:
            print("pc wins")
        else:
            print("user wins")
    elif userOption == 1:
        if pchoice == 2:
            print("pc wins")
        else:
            print("user wins")
    elif userOption == 2:
        if pchoice == 0:
            print("pc wins")
        else:
            print("user wins")

    continueRUN = input("\nDo you want to continue? Y or N: ").lower()
    if continueRUN == "y":
        userInput()
    else:
        exit(1)



if __name__ == "__main__":
    choices = ['Rock', 'paper', 'Scissor']
    print("Hello..")
    userInput()
