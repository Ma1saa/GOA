from turtle import *
#we want to pant house


# step 1 draw a square

width(6)

color("red")

forward(200)
left(90)

forward(200)
left(90)
forward(200)
left(90)
forward(200)
backward(200)
begin_fill()

right(60)
backward(115)
right(60)
backward(115)
end_fill()
left(120)
forward(200)
right(90)
forward(160)
begin_fill()
color("purple")
right(90)
forward(95)
right(90)
forward(65)
right(90)
forward(95)
end_fill()
penup()
goto(115, 115)
pendown()

color("purple")
left(90)
forward(60)

left(90)
forward(60)

left(90)
forward(60)
left(90)
forward(60)

left(90)
forward(30)

left(90)
forward(60)

penup()
goto(115, 145)
pendown()

right(90)
forward(60)


exitonclick()
