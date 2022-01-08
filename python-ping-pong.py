# Authored By: Markus Walker
# Inspired By: https://github.com/srimani-programmer/Ping-Pong-Game
# Licensed By: Open Source
# Date Modified: 1/7/22
#
# Descrption: Simple Ping Pong game developed in Python using the 
# turte module. Bring a friend and settle once and for all who is
# the alpha Pong player. Player 1 uses controls 'w' and 's', while
# Player 2 uses controls Up and Down.

import turtle, os, time

# Function to move the left paddle up.
def left_paddle_up():
    y = main.left_paddle.ycor()
    y += 50                         # Adjust the speed going up for the left paddle.
    main.left_paddle.sety(y)

# Function to move the left paddle down.
def left_paddle_down():
    y = main.left_paddle.ycor()
    y -= 50                         # Adjust the speed going down for the left paddle.
    main.left_paddle.sety(y)

# Function to move the right paddle up.
def right_paddle_up():
    y = main.right_paddle.ycor()
    y += 50                          # Adjust the speed going up for the right paddle.
    main.right_paddle.sety(y)

# Function to move the right paddle down.
def right_paddle_down():
    y = main.right_paddle.ycor()
    y -= 50                         # Adjust the speed going down for the left paddle.
    main.right_paddle.sety(y)

# Main function for the game.
def main():
    player_1_score = 0
    player_2_score = 0

    # Constant variables.
    HBORDER = 390
    VBORDER = 290
    COLLISION1 = 340
    COLLISION2 = 350
    SHIFT = 40
    FINAL_SCORE = 10

    print("Welcome to Python Ping-Pong!")
    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")
    print("Let's play Python Ping-Pong!")

    window = turtle.Screen() 
    window.title("Python Ping-Pong") 
    window.bgcolor("white")    
    window.bgpic("sonic.png")       # Background photo of Sonic the Hedgehog because you gotta go fast....
    window.setup(width=1000,height=1000)
    window.tracer(0)

    # Create left paddle and allow it to be referenced in other functions.
    main.left_paddle = turtle.Turtle()
    main.left_paddle.speed(0)
    main.left_paddle.shape("square")
    main.left_paddle.color("green")
    main.left_paddle.shapesize(stretch_wid=5,stretch_len=1)
    main.left_paddle.penup()
    main.left_paddle.goto(-350,0)

    # Create right paddle and allow it to be referenced in other functions.
    main.right_paddle = turtle.Turtle()
    main.right_paddle.speed(0)
    main.right_paddle.shape("square")
    main.right_paddle.shapesize(stretch_wid=5,stretch_len=1)
    main.right_paddle.color("red")
    main.right_paddle.penup()
    main.right_paddle.goto(350,0)

    # Create the actual Pong ball.
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("black")
    ball.penup()
    ball.goto(0,0)
    ball_dx = 0.5   # Change ball_dx and ball_dy to adjust the Pong ball's speed...
    ball_dy = 0.5

    # Create a pen that will keep track of the current score.
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("blue")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write(player1 + ": 0                    " + player2 + ": 0 ",align="center",font=('Arial', 24, "bold"))

    # Keyboard binding needed to track actual player movement.
    window.listen()
    window.onkeypress(left_paddle_up, "w")
    window.onkeypress(left_paddle_down, "s")
    window.onkeypress(right_paddle_up, "Up")
    window.onkeypress(right_paddle_down, "Down")

    while True:
        window.update()

        # Moving the ball horiztionally and vertically.
        ball.setx(ball.xcor() + ball_dx)
        ball.sety(ball.ycor() + ball_dy)

        # Setting up the vertical borders.
        if (ball.ycor() > VBORDER):
            ball.sety(VBORDER)
            ball_dy *= -1
        
        elif (ball.ycor() < -VBORDER):
            ball.sety(-VBORDER)
            ball_dy *= -1
            
        # Setting up the horizontal borders.
        if (ball.xcor() > HBORDER):   
            ball.goto(0,0)
            ball_dx *= -1
            player_1_score += 1
            pen.clear()
            pen.write(player1 + ": " + str(player_1_score) + "                  " + player2 + ": " + str(player_2_score) + " ".format(player_1_score, player_2_score), align="center", font=('Arial',24,"bold"))
            #os.system("afplay wallhit.wav&")   # TODO: Uncomment if you're on Linux or macOS to hear sound.

        if (ball.xcor()) < -HBORDER:
            ball.goto(0,0)
            ball_dx = ball_dx * -1
            player_2_score += 1
            pen.clear()
            pen.write(player1 + ": " + str(player_1_score) + "                  " + player2 + ": " + str(player_2_score) + " ".format(player_1_score, player_2_score), align="center", font=('Arial',24,"bold"))
            #os.system("afplay wallhit.wav&")   # TODO: Uncomment if you're on Linux or macOS to hear sound.

        # Handling the collisions with paddles.
        if (ball.xcor() > COLLISION1) and (ball.xcor() < COLLISION2) and (ball.ycor() < main.right_paddle.ycor() + SHIFT and ball.ycor() > main.right_paddle.ycor() - SHIFT):
            ball.setx(340)
            ball_dx *= -1
            #os.system("afplay paddle.wav&")    #TODO: Uncomment if you're on Linux or macOS to hear sound.

        elif (ball.xcor() < -COLLISION1) and (ball.xcor() > -COLLISION2) and (ball.ycor() < main.left_paddle.ycor() + SHIFT and ball.ycor() > main.left_paddle.ycor() - SHIFT):
            ball.setx(-340)
            ball_dx *= -1
            #os.system("afplay paddle.wav&")    # TODO: Uncomment if you're on Linux or macOS to hear sound.
        
        # Ends the game once the score has been reached.
        if (player_1_score < FINAL_SCORE and player_2_score < FINAL_SCORE):
            continue
        elif (player_1_score == FINAL_SCORE and player_2_score != FINAL_SCORE):
            ball_dx = 0
            pen.clear()
            pen.write(player1 + " wins!", align="center",font=("Arial",24,"bold"))
            time.sleep(5)
            break
        elif (player_2_score == FINAL_SCORE and player_1_score != FINAL_SCORE):
            ball_dx = 0
            pen.clear()
            pen.write(player2 + " wins!", align="center",font=("Arial",24,"bold"))
            time.sleep(5)
            break

if __name__ == "__main__":
    main()
