print("Welcome to computer quiz game !")

y = input("Do you want to play game?: ").lower()
print("Ok ! Lets play :) ")

if y != "yes":
    quit()

if y == "yes":
    print("Choose any subject from menu")
    print("1. C programming")
    print("2. python programming")
    print("3. Java programming")
score = 0
e = int(input("Enter your choice number: "))
if e == 1:
    answer = input("Who is father of c language?: ").lower()
    if answer == "dennis ritchie":
        print("congratulations your answer is correct")
        score+=1
    else:
        print("Your answer is Incorrect")
    answer = input("Keyword for conditional branching?: ").lower()
    if answer == "if":
        print("congratulations your answer is correct")
        score+=1
    else:
        print("Your answer is Incorrect")
    answer = input("Function to print output in C?: ").lower()
    if answer == "printf":
        print("congratulations your answer is correct")
        score+=1
    else:
        print("Your answer is Incorrect")
    print("Your score is :",score,"Points")
    print("---------Game is Over---------")

elif e == 2:
    answer = input("Keyword for defining a function?: ").lower()
    if answer == "def":
        print("congratulations your answer is correct")
        score+=1
    else:
        print("Your answer is Incorrect")
    answer = input("Built-in function to get input?: ").lower()
    if answer == "input()":
        print("congratulations your answer is correct")
        score+=1
    else:
        print("Your answer is Incorrect")
    answer = input("operator for power of number?: ").lower()
    if answer == "**":
        print("congratulations your answer is correct")
        score+=1
    else:
        print("Your answer is Incorrect")
    print("Your score is :",score,"Points")
    print("---------Game is Over---------")
elif e == 3:
    answer = input("Keyword for defining a class?: ").lower()
    if answer == "class":
        print("congratulations your answer is correct")
        score+=1
    else:
        print("Your answer is Incorrect")
    answer = input("Method to print output?: ").lower()
    if answer == "println":
        print("congratulations your answer is correct")
        score+=1
    else:
        print("Your answer is Incorrect")
    answer = input("Method to read input?: ").lower()
    if answer == "next":
        print("congratulations your answer is correct")
        score+=1
    else:
        print("Your answer is Incorrect")
    print("Your score is :",score,"Points")
    print("---------Game is Over---------")
else:
    print("Please enter the correct choice from above subjects.")
