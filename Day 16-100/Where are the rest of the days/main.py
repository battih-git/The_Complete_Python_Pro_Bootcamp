# import turtle
# from turtle import Turtle, Screen
#
# timmy = Turtle() # Create an object. () constructs the object.
# my_screen = Screen()
# # print(timmy) # It prints an object
#
# # Attributes can be accessed of a class follower by '.'
# print(my_screen.canvheight)
#
# # Functions are methods inside the class, something which object can performed
# turtle.shape('turtle')
# turtle.color('coral')
# turtle.forward(100)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable() # Constructing an object
table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = 'c'
print(table)