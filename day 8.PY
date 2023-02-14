# def greet():
#     print("Hello")
#     print("How are you?")
#     print("How's the weather?")

# greet()


# ----FUNCTION THAT ALLOWS FOR INPUT------

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How are you {name}?")

# greet_with_name("Balwant")


# ----FUNCTION THAT ALLOWS FOR MORE THAN 1 INPUT------

# def greet_with(name, location):
#     print(f"Hello {name}.")
#     print(f"What it is like in {location}?")
 
# greet_with("Bittu", "Delhi")    

# -----FUNCTIONS WITH KEYWORD ARGUMENTS-------

# def greet_with(name, location):
#     print(f"Hello {name}.")
#     print(f"What it is like in {location}?")

# greet_with(name="Bittu", location="Delhi")

#  ------AREA CALCULATOR----------------
import math
def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"you will need {num_of_cans} cans to paint")

test_h = int(input("Height of he wall: "))
test_w = int(input("Width of he wall: "))

coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)




