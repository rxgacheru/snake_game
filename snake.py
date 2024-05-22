import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("dodger blue")
window.setup(width=600, height=600)
window.tracer(0)

snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("alice blue")
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "Stop"

food = turtle.Turtle()
food.speed(0)
shapes = random.choice(['square', 'triangle', 'circle'])
food.shape(shapes)
colors = random.choice(['green', 'blue', 'red','orange'])
food.color(colors)
food.penup()
food.goto(0, 100)

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color('white')
score_display.shape('square')
score_display.hideturtle()
score_display.goto(0, 250)
score_display.penup()
score_display.write("Score : 0  High Score : 0", align="center",
          font=("candara", 24,"bold"))

def move_up():
    if snake_head.direction != "Down":
        snake_head.direction = "Up"

def move_down():
    if snake_head.direction != "Up":
        snake_head.direction = "Down"

def move_left():
    if snake_head.direction != "Right":
        snake_head.direction = "Left"

def move_right():
    if snake_head.direction != "Left":
        snake_head.direction = "Right"

def move():
    if snake_head.direction == "Up":
        y = snake_head.ycor()
        snake_head.sety(y + 20)

    if snake_head.direction == "Down":
        y = snake_head.ycor()
        snake_head.sety(y - 20)

    if snake_head.direction == "Left":
        x = snake_head.xcor()
        snake_head.setx(x - 20)

    if snake_head.direction == "Right":
        x = snake_head.xcor()
        snake_head.setx(x + 20)



window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")

segments = []

while True:
    window.update()
    if snake_head.xcor()> 290 or snake_head.xcor() <-290 or snake_head.ycor()> 290 or snake_head.ycor() <-290:
        time.sleep(1)
        snake_head.goto(0, 0)
        snake_head.direction ="Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        score_display.clear()
        score_display.write("Score : {} High Score : {}".format(
            score, high_score), align="center", font=("candara", 24,"bold"))

    if snake_head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score> high_score:
            high_score = score
        score_display.clear()
        score_display.write("Score : {} High Score : {}".format(
            score, high_score), align="center", font=("candara", 24,"bold"))


    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments)> 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(snake_head) <20:
            time.sleep(1)
            snake_head.goto(0, 0)
            snake_head.direction ="stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
 
            score = 0
            delay = 0.1
            score_display.clear()
            score_display.write("Score : {} High Score : {}".format(
                score, high_score), align="center", font=("candara", 24,"bold"))
    time.sleep(delay)
 
