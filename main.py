# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('blue')
t.hideturtle()
t.goto(0, -10)

t.pensize(3)
t.color('red')
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
##t.setheading(60)
##t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()
# Press the green button in the gutter to run the script.
t.penup()
t.goto(-90,130)
t.pendown()
t.color('white')
t.write("Happy Birthday", font=("Verdana",15,"bold"))

t.penup()
t.goto(-35,-180)
t.pendown()
t.color('white')
t.write("2022", font=("Verdana",15,"bold"))
t.penup()
t.goto(-200,-200)
t.pendown()
t.color('white')
t.write("I wish you all the best for this year ", font=("Verdana",15,"bold"))

t.penup()
t.goto(-200,-210)
t.pendown()
t.color('white')
t.write("By Eddylian", font=("Verdana",5,"bold"))
turtle.done()

