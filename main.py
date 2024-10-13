import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import pygame  

pygame.mixer.init()
game_over_sound = pygame.mixer.Sound("game_over.mp3")

screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Pong Game')

paddle_r = Paddle(350)
paddle_l = Paddle(-350)
ball = Ball()
score = ScoreBoard()

# Set up keyboard controls for the right paddle
screen.listen()
screen.onkey(paddle_r.move_paddle_up, 'Up')
screen.onkey(paddle_r.move_paddle_down, 'Down')

loss_count = 0
max_lives = 3

# Create heart turtles (lives for the player)
hearts = []
for i in range(max_lives):
    heart = Turtle()
    heart.color("red")
    heart.shape("turtle")  # Use the turtle shape for the heart
    heart.penup()
    heart.goto(350 - (i * 30), 250)  # Position them in the top right corner
    hearts.append(heart)


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # AI logic: Move left paddle based on ball's y-position
    if paddle_l.ycor() < ball.ycor() and abs(paddle_l.ycor() - ball.ycor()) > 10:
        paddle_l.move_paddle_up()
    elif paddle_l.ycor() > ball.ycor() and abs(paddle_l.ycor() - ball.ycor()) > 10:
        paddle_l.move_paddle_down()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(paddle_r) < 30 and ball.xcor() > 330:
        ball.bounce_paddle()

    if ball.distance(paddle_l) < 30 and ball.xcor() < -330:
        ball.bounce_paddle()

    if ball.xcor() > 380:
        ball.reset()
        score.l_point()
        loss_count += 1  # Increment loss count

        if loss_count <= max_lives:
            hearts[max_lives - loss_count].hideturtle()  # Hide the corresponding heart

    if ball.xcor() < -380:
        ball.reset()
        score.r_point()

    # Check if the player has lost all lives
    if loss_count >= max_lives:
        game_over_sound.play()
        # Display 'GAME OVER' message
        game_over_turtle = Turtle()
        game_over_turtle.color("red")
        game_over_turtle.hideturtle()
        game_over_turtle.penup()
        game_over_turtle.goto(0, 0)  # Center the message on the screen
        game_over_turtle.write("GAME OVER.", align="center", font=("Courier", 24, "bold"))

        screen.update()  # Update screen to show the message and sound effect
        time.sleep(3)  # Wait for 3 seconds to let the sound play
        game_on = False  # End the game

screen.exitonclick()
