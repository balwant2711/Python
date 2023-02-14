print("Welcome to treasure island")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go ? type "left" or "right"').lower()

if choice1 == "left":
    choice2 = input('You\'ve come across at a river, type "Wait" to wait for the boat or type "swim" to swim across the river.' ).lower()
    if choice2 == "wait":
        choice3 = input("you are at the island house, there are three doors One red, One Blue and one yellow. Please select one door.").lower()
        if choice3 == "yellow":
            print ("You win")
        elif choice3 == "blue":
            print("Game over")
        elif choice3 == "red":
            print("Game over")
    else: 
        print("You choose the wrong option. Game Over")
else:
    print("Game Over")




