#snake game

import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width = 600 , height = 600)
wn.tracer(0)

#Snake head

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("#8331FF")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0 , 260)
pen.write("Score:0 High Score:0", align = "center",font=("Courier" , 24 , "normal"))




#Functions
def go_up():
	if head.direction != "down":
		head.direction = "up"

def go_down():
	if head.direction != "up":
		head.direction = "down"

def go_right():
	if head.direction != "left":
		head.direction = "right"

def go_left():
	if head.direction != "right":
		head.direction = "left"	

def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y + 20)

	if head.direction == "down":
		y = head.ycor()
		head.sety(y - 20)

	if head.direction == "left":
		x = head.xcor()
		head.setx(x - 20)

	if head.direction == "right":
		x = head.xcor()
		head.setx(x + 20)			

#Keyboard bindings
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_right,"Right")
wn.onkeypress(go_left,"Left")



#Main game loop
while True:
	wn.update()

	if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
		time.sleep(0.1)
		head.goto(0,0)
		head.direction = "stop"

		for segement in segments:
			segement.goto(1000,1000)

		segments.clear()

		delay = 0.1
		#Reset the score
		score = 0

		pen.clear()	

		pen.write(f"Score: {score} High Score: {high_score}",align = "center" , font = ("Courier" , 24, "normal"))	



	if head.distance(food) < 20:
		x = random.randint(-290,290)
		y = random.randint(-290,290)
		food.goto(x,y)

		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("blue")
		new_segment.penup()
		segments.append(new_segment)

		#Increase the score 
		score += 10

		#Decrease delay

		delay -= 0.001

		if score > high_score:
			high_score = score

		pen.clear()	

		pen.write(f"Score: {score} High Score: {high_score}",align = "center" , font = ("Courier" , 24, "normal"))	

	for index in range(len(segments)-1,0,-1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x,y)

	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x,y)		


	move()

	#Check for head collision with body segment
	for segment in segments:
		if segment.distance(head) < 20:
			time.sleep(0.1)
			head.goto(0,0)
			head.direction = "stop"

			#Hide the segments
			for segment in segments:
				segment.goto(1000,1000)

			segments.clear()

			delay = 0.1

			score = 0
			pen.clear()	

			pen.write(f"Score: {score} High Score: {high_score}",align = "center" , font = ("Courier" , 24, "normal"))		

		    




	time.sleep(delay)

wn.mainloop()