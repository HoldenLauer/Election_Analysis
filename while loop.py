# Initial variable to track game play



user_play = "y"

# While we are still playing...
while user_play == "y":
    # Ask the user how many numbers to loop through
    user_choice = int(input("How many numbers do you want to loop through?"))
     
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for x in range(user_choice):
        print(x)

        # Print each number in the range
    user_play = input("Continue: (y)es or (n)o? ")
