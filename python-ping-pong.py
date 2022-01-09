# Authored By: Markus Walker
# Inspired By: https://github.com/srimani-programmer/Ping-Pong-Game
# Licensed By: Open Source
# Date Modified: 1/8/22
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
    HBORDER = 360
    VBORDER = 250
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
    main.left_paddle.shapesize(stretch_wid=4,stretch_len=1)
    main.left_paddle.penup()
    main.left_paddle.goto(-350,0)

    # Create right paddle and allow it to be referenced in other functions.
    main.right_paddle = turtle.Turtle()
    main.right_paddle.speed(0)
    main.right_paddle.shape("square")
    main.right_paddle.shapesize(stretch_wid=4,stretch_len=1)
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
    ball_dx = 5.5   # Change ball_dx and ball_dy to adjust the Pong ball's speed...
    ball_dy = 5.5

    # Create a pen that will keep track of the current score.
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("blue")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("SCOREBOARD\n\n", align="center", font=("Arial", 24, "bold"))
    pen.write(player1.upper() + ": 0                    " + player2.upper() + ": 0 ",align="center",font=("Arial", 24, "bold"))

    # Create a pen that will draw a vertical line, making the center line.
    vert_line = turtle.Turtle()
    vert_line.speed(0)
    vert_line.shape("square")
    vert_line.shapesize(stretch_wid=52,stretch_len=1)
    vert_line.color("black")
    vert_line.penup()
    vert_line.goto(0,-200)

    # Create a pen that will draw a second vertical line, making the left border.
    vert2_line = turtle.Turtle()
    vert2_line.speed(0)
    vert2_line.shape("square")
    vert2_line.shapesize(stretch_wid=52,stretch_len=1)
    vert2_line.color("black")
    vert2_line.penup()
    vert2_line.goto(540,-200)

    # Create a pen that will draw a third vertical line, making the right border.
    vert3_line = turtle.Turtle()
    vert3_line.speed(0)
    vert3_line.shape("square")
    vert3_line.shapesize(stretch_wid=52,stretch_len=1)
    vert3_line.color("black")
    vert3_line.penup()
    vert3_line.goto(-500,-200)

    # Create a pen that will draw a horizontal line, making the top center border.
    horiz_line = turtle.Turtle()
    horiz_line.speed(0)
    horiz_line.shape("square")
    horiz_line.shapesize(stretch_wid=1,stretch_len=52)
    horiz_line.color("black")
    horiz_line.penup()
    horiz_line.goto(30,310)

    # Create a pen that will draw a second horizontal line, making the bottom center border.
    horiz2_line = turtle.Turtle()
    horiz2_line.speed(0)
    horiz2_line.shape("square")
    horiz2_line.shapesize(stretch_wid=1,stretch_len=52)
    horiz2_line.color("black")
    horiz2_line.penup()
    horiz2_line.goto(30,-380)

    # Keyboard binding needed to track actual player movement.
    window.listen()
    window.onkeypress(left_paddle_up, "w")
    window.onkeypress(left_paddle_down, "s")
    window.onkeypress(right_paddle_up, "Up")
    window.onkeypress(right_paddle_down, "Down")

    # While loop to handle the actual game, including paddle boundaries, Pong ball boundaries and ending the game.
    while True:
        window.update()

        # Moving the ball horiztionally and vertically.
        ball.setx(ball.xcor() + ball_dx)
        ball.sety(ball.ycor() + ball_dy)

        # Setting up the vertical borders for the left paddle.
        if ((main.left_paddle.ycor() > VBORDER)):
            main.left_paddle.sety(VBORDER)

        # Setting up the vertical borders for the left paddle.
        elif ((main.left_paddle.ycor() < -VBORDER)):
            main.left_paddle.sety(-VBORDER)

        # Setting up the vertical borders for the right paddle.
        if ((main.right_paddle.ycor() > VBORDER)):
            main.right_paddle.sety(VBORDER)

        # Setting up the vertical borders for the right paddle.
        elif ((main.right_paddle.ycor() < -VBORDER)):
            main.right_paddle.sety(-VBORDER)

        # Setting up the vertical borders for the Pong ball.
        if (ball.ycor() > VBORDER):
            ball.sety(VBORDER)
            ball_dy *= -1
        
        elif (ball.ycor() < -VBORDER):
            ball.sety(-VBORDER)
            ball_dy *= -1
            
        # Setting up the horizontal borders for the Pong ball.
        if (ball.xcor() > HBORDER):   
            ball.goto(0,0)
            ball_dx *= -1
            player_1_score += 1
            pen.clear()
            pen.write("SCOREBOARD\n\n", align="center", font=("Arial", 24, "bold"))
            pen.write(player1.upper() + ": " + str(player_1_score) + "                  " + player2.upper() + ": " + str(player_2_score) + " ".format(player_1_score, player_2_score), align="center", font=('Arial',24,"bold"))
            #os.system("afplay wall-hit-sound.wav&")   # TODO: Uncomment if you're on Linux or macOS to hear sound.

        if (ball.xcor()) < -HBORDER:
            ball.goto(0,0)
            ball_dx = ball_dx * -1
            player_2_score += 1
            pen.clear()
            pen.write("SCOREBOARD\n\n", align="center", font=("Arial", 24, "bold"))
            pen.write(player1.upper() + ": " + str(player_1_score) + "                  " + player2.upper() + ": " + str(player_2_score) + " ".format(player_1_score, player_2_score), align="center", font=('Arial',24,"bold"))
            #os.system("afplay wall-hit-sound.wav&")   # TODO: Uncomment if you're on Linux or macOS to hear sound.

        # Handling the collisions with paddles.
        if (ball.xcor() > COLLISION1) and (ball.xcor() < COLLISION2) and (ball.ycor() < main.right_paddle.ycor() + SHIFT and ball.ycor() > main.right_paddle.ycor() - SHIFT):
            ball.setx(COLLISION1)
            ball_dx *= -1
            #os.system("afplay paddle-sound.wav&")    #TODO: Uncomment if you're on Linux or macOS to hear sound.

        elif (ball.xcor() < -COLLISION1) and (ball.xcor() > -COLLISION2) and (ball.ycor() < main.left_paddle.ycor() + SHIFT and ball.ycor() > main.left_paddle.ycor() - SHIFT):
            ball.setx(-COLLISION1)
            ball_dx *= -1
            #os.system("afplay paddle-sound.wav&")    # TODO: Uncomment if you're on Linux or macOS to hear sound.
        
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
