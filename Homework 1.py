#Homework 1


#Question 1
chairs = 15
#chairs = '15' #string format not integer
nails = 4

total_nails = chairs * nails

#message = "I need to buy{}nails." format(total_nails)

message = "I need to buy {} nails".format(total_nails)

print(message)

print("You need to buy {} nails".format(total_nails))

#Question 2
#my_name = Penelope #string not assigned to variable
my_name = "Penelope"
my_age = 29

message = "My name is {} and I am {} years old".format(my_name, my_age)

print(message)

#Question 3
box_of_egg = 6
total_boxes_of_egg = 6
total_eggs = box_of_egg * total_boxes_of_egg
omelette = 4
total_omelettes = total_eggs/omelette

#print(total_eggs)
#print(total_omelettes)

message = "You can make {} omelettes with {} boxes of egges". format(total_omelettes, total_boxes_of_egg)

print(message)
