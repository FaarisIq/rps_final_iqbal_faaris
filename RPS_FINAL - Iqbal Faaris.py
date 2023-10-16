#  This file is created by Faaris Iqbal

#  The turtle module is a lightweight graphics library for teaching python
import turtle
# importing randomize
from turtle import *
from random import randint
# Creating a choices list and making a randomizer for the cpu choice
choices = ["rock", "paper", "scissors"]
cpuchoice = choices[randint(0,2)]
# The os module allows us to access the current directory in order to access assets
import os

# defining a function that allows me to use a writing tool.
def write_text(message, x, y):
    text = turtle.Turtle()
    text.hideturtle()
    text.color('black')
    text.penup()
    text.setpos(x,y)
    text.write(message, False, "center", ("Arial", 22, "bold"))


# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

# setting variables for image length and height for hitbox determination
rock_w = 154
rock_h = 170
paper_w = 241
paper_h = 157
scissors_w = 256
scissors_h = 170

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="white")

# setup all images using the os module
rock_image = os.path.join(images_folder, 'rock.gif')
cpu_rock = os.path.join(images_folder, 'cpu_rock.gif')

paper_image = os.path.join(images_folder, 'paper.gif')
cpu_paper = os.path.join(images_folder, 'cpu_paper.gif')

scissors_image = os.path.join(images_folder, 'scissors.gif')
cpu_scissors = os.path.join(images_folder, 'cpu_scissors.gif')
# instantiate (create an instance of) the Turtle class for all posibilities including cpu choices
rock_instance = turtle.Turtle()
cpu_rock_instance = turtle.Turtle()
cpu_rock_instance.hideturtle()
cpu_rock_instance.penup()

paper_instance = turtle.Turtle()
cpu_paper_instance = turtle.Turtle()
cpu_paper_instance.hideturtle()
cpu_paper_instance.penup()

scissors_instance = turtle.Turtle()
cpu_scissors_instance = turtle.Turtle()
cpu_scissors_instance.hideturtle()
cpu_scissors_instance.penup()

# adding shapes for the turtle
screen.addshape(rock_image)
screen.addshape(paper_image)
screen.addshape(scissors_image)
screen.addshape(cpu_rock)
screen.addshape(cpu_paper)
screen.addshape(cpu_scissors)

# setting variables for all choice positions and setting their pen up so it doesn't draw.
rock_pos_x = -300
rock_pos_y = 0
paper_pos_x = 0
paper_pos_y = 0
scissors_pos_x = 300
scissors_pos_y = 0
rock_instance.penup()
paper_instance.penup()
scissors_instance.penup()

# setting position for user choice instances
rock_instance.setpos(rock_pos_x,rock_pos_y)
paper_instance.setpos(paper_pos_x, paper_pos_y)
scissors_instance.setpos(scissors_pos_x, scissors_pos_y)

#setting all instances turtle shape to be the image
rock_instance.shape(rock_image)
cpu_rock_instance.shape(cpu_rock)

paper_instance.shape(paper_image)
cpu_paper_instance.shape(cpu_paper)

scissors_instance.shape(scissors_image)
cpu_scissors_instance.shape(cpu_scissors)

# writing text on screen
write_text("I think you know what to do..",  0, 125)


# function to determin collision
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

# "nothing" is set to user choice as a filler.
userchoice = "nothing"

# defining function where if image clicked on screen we send other images off screen and print a win/loss message
def mouse_pos(x, y):
    #checking for mouse + rock collision
    if collide(x,y,rock_instance,rock_w,rock_h):
        userchoice = "rock"
        paper_instance.setpos(paper_pos_x, -500)
        scissors_instance.setpos(scissors_pos_x, -500)
        #seeing if cpu chose paper and printing result
        if cpuchoice == "paper":
            cpu_paper_instance.showturtle()
            cpu_paper_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("You lost!", 0, 0)
        #seeing if cpu chose rock and printing result
        elif cpuchoice == "rock":
            cpu_rock_instance.showturtle()
            cpu_rock_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("You tied!", 0, 0)
        #seeing if cpu chose scissors and printing result
        elif cpuchoice == "scissors":
            cpu_scissors_instance.showturtle()
            cpu_scissors_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("You won!", 0, 0)
    #checking for mouse + paper collision
    elif collide(x,y,paper_instance,paper_w,paper_h):
        rock_instance.setpos(rock_pos_x, -500)
        scissors_instance.setpos(scissors_pos_x, -500)
        paper_instance.setpos(rock_pos_x, rock_pos_y)
        userchoice = "paper"
        #seeing if cpu chose paper and printing result
        if cpuchoice == "paper":
            cpu_paper_instance.showturtle()
            cpu_paper_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("You tied!", 0, 0)
        #seeing if cpu chose rock and printing result
        elif cpuchoice == "rock":
            cpu_rock_instance.showturtle()
            cpu_rock_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("You won!", 0, 0)
        #seeing if cpu chose scissors and printing result
        elif cpuchoice == "scissors":
            cpu_scissors_instance.showturtle()
            cpu_scissors_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("You lost!", 0, 0)
    #checking for mouse + scissors collision
    elif collide(x,y,scissors_instance,scissors_w,scissors_h):
        paper_instance.setpos(paper_pos_x, -500)
        rock_instance.setpos(rock_pos_x, -500)
        scissors_instance.setpos(rock_pos_x, rock_pos_y)
        userchoice = "scissors"
        #seeing if cpu chose paper and printing result
        if cpuchoice == "paper":
            cpu_paper_instance.showturtle()
            cpu_paper_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("You won!", 0, 0)
        #seeing if cpu chose rock and printing result
        elif cpuchoice == "rock":
            cpu_rock_instance.showturtle()
            cpu_rock_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("You lost!", 0, 0)
        #seeing if cpu chose scissors and printing result
        elif cpuchoice == "scissors":
            cpu_scissors_instance.showturtle()
            cpu_scissors_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("You tied!", 0, 0)
    else:
        userchoice = "nothing"

# calling game function
screen.onclick(mouse_pos)



# have the turtle module 'listen' for when keys are pressed
turtle.listen()

# when the turtle 'x' key is pressed then quit turtle
turtle.done()