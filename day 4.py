# import random

# random_int = random.randint(0, 10)
# print(random_int)

# random_float = random.random()
# print(random_float)

# random_float = random.random() * 5
# print(random_float)


# random_float1 = random.uniform(3,5)
# print(random_float1)


# ---------VIRTUAL COIN TOSS EXERCISE-------

# import random
# random_side = random.randint(0, 1)
# if random_side == 0:
#     print ("Tails")
# else:
#     print("Heads")    



# ------------------LIST------------

# states_of_america = [
#   "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", 
#   "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", 
#   "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", 
#   "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", 
#   "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", 
#   "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", 
#   "New Mexico", "Arizona", "Alaska", "Hawaii"
# ]

# print(states_of_america)  # print all states

# print(states_of_america[2])  # print New Jersey  # Positive Indexing

# print(states_of_america[-1])  # print Hawaii  # Negative Indexing

# print(states_of_america[-2])  # print Alaska

# states_of_america[1] = "Pencilvania"  # update that element

# states_of_america.append("Angelaland")  
# # append function adds another single item to the end of the list

# states_of_america.extend(["Angelaland", "Jack Bauer land"]) 
# # extend function adds more then one items to the list

# ----BANKER ROULETTE WHO WILL PAY THE BILL----

# names_string = input("Give me everybody's name seperated by a comma.")
# names = names_string.split(", ")
# print(names)
# import random
# random_name = random.choice(names)
# print(f"{random_name} will pay the bill")


# -----------------------//INDEX ERROR///---------------------

# states_of_america = [
#   "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", 
#   "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", 
#   "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", 
#   "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", 
#   "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", 
#   "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", 
#   "New Mexico", "Arizona", "Alaska", "Hawaii"
# ]

# print(len(states_of_america))
# num_of_states= len(states_of_america)
# # print(states_of_america[num_of_states]) #will give index error

# print(states_of_america[num_of_states - 1])

# --------NESTED LISTS--------LISTS WITHIN A LIST----

# fruits = ["apple", "mango", "Strawberry", "Bananna", "cherry", "Orange"]
# vegetables  = ["Spinach", "Tomato", "Potato", "Peas", "Onion"]

# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)

# -------------------------------------------
# Treasure Map

# You are going to write a program which will mark a spot with an X.
# Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
# The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:
# https://cdn.fs.teachablecdn.com/2vnboIYTFFruvl9FJ2w5
# First your program must take the user input and convert it to a usable format.
# Next, you need to use it to update your nested list with an "x".

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")
horizontal = int(position[0])  #2
vertical = int(position[1])  #3

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")




