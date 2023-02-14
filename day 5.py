# fruits =["Apple", "Orange", "Mango"]
# for fruit in fruits:
#     # print(fruit)
#     print(fruit + " Pie")   

# ----------AVERAGE HEIGHT -------

student_heights = input("Input a list of student heights ").split()
for n in range (0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
print(len(student_heights))

# total_height = 0
# for height in student_heights:
#     total_height += height
# print(total_height)

# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
# print(number_of_students)    

# OR
# total_height =  sum(student_heights)
# number_of_students = len(student_heights)

# average_height = round(total_height / number_of_students)
# print(average_height)



#  ------  High Score ---------

# student_scores = input("Input a list of student scores ").split()
# for n in range (0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)    

# # ---OR--
# # print(max(student_scores))
# # ptint(min(student_scores))

# high_score = 0
# for  score in student_scores:
#     if score > high_score:
#         high_score = score
   
# print(f"The heighest score in the class is: {high_score} ")    

# --------FOR LOOP WITH RANGE------

# for n in range (1, 10):
#     print(n)


# for n in range (1, 11):
#     print(n)


# for n in range (1, 11, 3):
#     print(n)


# total = 0
# for number in range(1, 101):
#     total += number
# print (total)   

# ------ ADDING EVEN NUMBER ----

# total = 0
# for n in range(2, 101, 2):
#     total += n
# print(total)
# # OR---
# total2 = 0
# for n in range (1, 101):
#     if n % 2 == 0:
#         total2 += n
# print(total2)   


# for n in range (1, 101):
#     if (n % 3 == 0) and (n % 5 == 0):
#         print ("FizzBuzz")
#     elif n % 3 == 0:
#         print ("Fizz")
     
#     elif n % 5 == 0: 
#         print("Buzz")   
#     else:
#         print (n)    

      



