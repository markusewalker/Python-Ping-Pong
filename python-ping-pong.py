#################################################################################
# Authored By: Markus Walker
# Inspired By: https://github.com/srimani-programmer/Ping-Pong-Game
# Licensed By: Open Source
# Date Modified: 1/9/22
#
# Descrption: Simple Ping Pong game developed in Python using the 
# turte module. Bring a friend and settle once and for all who is
# the alpha Pong player. Player 1 uses controls 'w' and 's', while
# Player 2 uses controls Up and Down.
#################################################################################

import turtle, os, time

#################################################################################
# GLOBAL VARIABLES
#################################################################################
player_1_score = 0
player_2_score = 0
HBORDER = 360
VBORDER = 250
COLLISION1 = 340
COLLISION2 = 350
SHIFT = 40
FINAL_SCORE = 10

#################################################################################
# Function to start the game. Prompts for both player's names, initializes 
# the separate window and tracks player's movements.
#################################################################################
def startGame():
    print("Welcome to Python Ping-Pong!")
    startGame.player1 = input("Player 1, enter your name: ")
    startGame.player2 = input("Player 2, enter your name: ")
    print("Let's play Python Ping-Pong!")

    startGame.window = turtle.Screen() 
    startGame.window.title("Python Ping-Pong") 
    startGame.window.bgcolor("white")    
    startGame.window.bgpic("board-pic.png") 
    startGame.window.setup(width=1000,height=1000)
    startGame.window.tracer(0)

    startGame.window.listen()
    startGame.window.onkeypress(left_paddle_up, "w")
    startGame.window.onkeypress(left_paddle_down, "s")
    startGame.window.onkeypress(right_paddle_up, "Up")
    startGame.window.onkeypress(right_paddle_down, "Down")

#################################################################################
# Function to create left paddle.
#################################################################################
def leftPaddle():
    leftPaddle.left_paddle = turtle.Turtle()
    leftPaddle.left_paddle.speed(0)
    leftPaddle.left_paddle.shape("square")
    leftPaddle.left_paddle.color("green")
    leftPaddle.left_paddle.shapesize(stretch_wid=4,stretch_len=1)
    leftPaddle.left_paddle.penup()
    leftPaddle.left_paddle.goto(-350,0)

#################################################################################
# Function to move the left paddle up.
#################################################################################
def left_paddle_up():
    y = leftPaddle.left_paddle.ycor()
    y += 50                         # Adjust the speed going up for the left paddle.
    leftPaddle.left_paddle.sety(y)

#################################################################################
# Function to move the left paddle down.
#################################################################################
def left_paddle_down():
    y = leftPaddle.left_paddle.ycor()
    y -= 50                         # Adjust the speed going down for the left paddle.
    leftPaddle.left_paddle.sety(y)

#################################################################################
# Function to create right paddle.
#################################################################################
def rightPaddle():
    rightPaddle.right_paddle = turtle.Turtle()
    rightPaddle.right_paddle.speed(0)
    rightPaddle.right_paddle.shape("square")
    rightPaddle.right_paddle.shapesize(stretch_wid=4,stretch_len=1)
    rightPaddle.right_paddle.color("red")
    rightPaddle.right_paddle.penup()
    rightPaddle.right_paddle.goto(350,0)

#################################################################################
# Function to move the right paddle up.
#################################################################################
def right_paddle_up():
    y = rightPaddle.right_paddle.ycor()
    y += 50                          # Adjust the speed going up for the right paddle.
    rightPaddle.right_paddle.sety(y)

#################################################################################
# Function to move the right paddle down.
#################################################################################
def right_paddle_down():
    y = rightPaddle.right_paddle.ycor()
    y -= 50                         # Adjust the speed going down for the left paddle.
    rightPaddle.right_paddle.sety(y)

#################################################################################
# Function to create the Ping Pong ball.
#################################################################################
def makeBall():
    makeBall.ball = turtle.Turtle()
    makeBall.ball.speed(0)
    makeBall.ball.shape("circle")
    makeBall.ball.color("black")
    makeBall.ball.penup()
    makeBall.ball.goto(0,0)
    makeBall.ball_dx = 0.5   # Change ball_dx and ball_dy to adjust the Pong ball's speed...
    makeBall.ball_dy = 0.5

#################################################################################
# Function to create a pen that will keep track of the current score.
#################################################################################
def score():
    score.pen = turtle.Turtle()
    score.pen.speed(0)
    score.pen.color("blue")
    score.pen.penup()
    score.pen.hideturtle()
    score.pen.goto(0,260)
    score.pen.write("SCOREBOARD\n\n", align="center", font=("Arial", 24, "bold"))
    score.pen.write(startGame.player1.upper() + ": 0                    " + startGame.player2.upper() + ": 0 ",align="center",font=("Arial", 24, "bold"))

#################################################################################
# Function to create a pen that will draw a vertical line.
#################################################################################
def vertLineOne():
    vert_line = turtle.Turtle()
    vert_line.speed(0)
    vert_line.shape("square")
    vert_line.shapesize(stretch_wid=52,stretch_len=1)
    vert_line.color("black")
    vert_line.penup()
    vert_line.goto(0,-200)

#################################################################################
# Function to create a pen that will draw a second vertical line.
#################################################################################
def vertLineTwo():
    vert2_line = turtle.Turtle()
    vert2_line.speed(0)
    vert2_line.shape("square")
    vert2_line.shapesize(stretch_wid=52,stretch_len=1)
    vert2_line.color("black")
    vert2_line.penup()
    vert2_line.goto(540,-200)

#################################################################################
# Function to create a pen that will draw a third vertical line.
#################################################################################
def vertLineThree():
    vert3_line = turtle.Turtle()
    vert3_line.speed(0)
    vert3_line.shape("square")
    vert3_line.shapesize(stretch_wid=52,stretch_len=1)
    vert3_line.color("black")
    vert3_line.penup()
    vert3_line.goto(-500,-200)

#################################################################################
# Function to create a pen that will draw a horizontal line.
#################################################################################
def horizLineOne():
    horiz_line = turtle.Turtle()
    horiz_line.speed(0)
    horiz_line.shape("square")
    horiz_line.shapesize(stretch_wid=1,stretch_len=52)
    horiz_line.color("black")
    horiz_line.penup()
    horiz_line.goto(30,310)

#################################################################################
# Function to create a pen that will draw a second horizontal line.
#################################################################################
def horizLineTwo():
    horiz2_line = turtle.Turtle()
    horiz2_line.speed(0)
    horiz2_line.shape("square")
    horiz2_line.shapesize(stretch_wid=1,stretch_len=52)
    horiz2_line.color("black")
    horiz2_line.penup()
    horiz2_line.goto(30,-380)

#################################################################################
# Function that actually handles the Ping Pong game. Handles the game's
# boundaries, collisions and when the game will end.
#################################################################################
def pingPong():
    # While loop to handle the actual game, including paddle boundaries, Pong ball boundaries and ending the game.
    while True:
        startGame.window.update()

        # Moving the ball horiztionally and vertically.
        makeBall.ball.setx(makeBall.ball.xcor() + makeBall.ball_dx)
        makeBall.ball.sety(makeBall.ball.ycor() + makeBall.ball_dy)

        # Setting up the vertical borders for the left paddle.
        if ((leftPaddle.left_paddle.ycor() > VBORDER)):
            leftPaddle.left_paddle.sety(VBORDER)

        # Setting up the vertical borders for the left paddle.
        elif ((leftPaddle.left_paddle.ycor() < -VBORDER)):
            leftPaddle.left_paddle.sety(-VBORDER)

        # Setting up the vertical borders for the right paddle.
        if ((rightPaddle.right_paddle.ycor() > VBORDER)):
            rightPaddle.right_paddle.sety(VBORDER)

        # Setting up the vertical borders for the right paddle.
        elif ((rightPaddle.right_paddle.ycor() < -VBORDER)):
            rightPaddle.right_paddle.sety(-VBORDER)

        # Setting up the vertical borders for the Pong ball.
        if (makeBall.ball.ycor() > VBORDER):
            makeBall.ball.sety(VBORDER)
            makeBall.ball_dy *= -1
        
        elif (makeBall.ball.ycor() < -VBORDER):
            makeBall.ball.sety(-VBORDER)
            makeBall.ball_dy *= -1
            
        # Setting up the horizontal borders for the Pong ball.
        if (makeBall.ball.xcor() > HBORDER):   
            makeBall.ball.goto(0,0)
            makeBall.ball_dx *= -1
            global player_1_score, player_2_score
            player_1_score += 1

            score.pen.clear()
            score.pen.write("SCOREBOARD\n\n", align="center", font=("Arial", 24, "bold"))
            score.pen.write(startGame.player1.upper() + ": " + str(player_1_score) + "                  " + startGame.player2.upper() + ": " + str(player_2_score) + " ".format(player_1_score, player_2_score), align="center", font=('Arial',24,"bold"))
            #os.system("afplay wall-hit-sound.wav&")   # TODO: Uncomment if you're on Linux or macOS to hear sound.

        if (makeBall.ball.xcor()) < -HBORDER:
            makeBall.ball.goto(0,0)
            makeBall.ball_dx *= -1
            player_2_score += 1

            score.pen.clear()
            score.pen.write("SCOREBOARD\n\n", align="center", font=("Arial", 24, "bold"))
            score.pen.write(startGame.player1.upper() + ": " + str(player_1_score) + "                  " + startGame.player2.upper() + ": " + str(player_2_score) + " ".format(player_1_score, player_2_score), align="center", font=('Arial',24,"bold"))
            #os.system("afplay wall-hit-sound.wav&")   # TODO: Uncomment if you're on Linux or macOS to hear sound.

        # Handling the collisions with paddles.
        if (makeBall.ball.xcor() > COLLISION1) and (makeBall.ball.xcor() < COLLISION2) and (makeBall.ball.ycor() < rightPaddle.right_paddle.ycor() + SHIFT and makeBall.ball.ycor() > rightPaddle.right_paddle.ycor() - SHIFT):
            makeBall.ball.setx(COLLISION1)
            makeBall.ball_dx *= -1
            #os.system("afplay paddle-sound.wav&")    #TODO: Uncomment if you're on Linux or macOS to hear sound.

        elif (makeBall.ball.xcor() < -COLLISION1) and (makeBall.ball.xcor() > -COLLISION2) and (makeBall.ball.ycor() < leftPaddle.left_paddle.ycor() + SHIFT and makeBall.ball.ycor() > leftPaddle.left_paddle.ycor() - SHIFT):
            makeBall.ball.setx(-COLLISION1)
            makeBall.ball_dx *= -1
            #os.system("afplay paddle-sound.wav&")    # TODO: Uncomment if you're on Linux or macOS to hear sound.
        
        # Ends the game once the score has been reached.
        if (player_1_score < FINAL_SCORE and player_2_score < FINAL_SCORE):
            continue
        elif (player_1_score == FINAL_SCORE and player_2_score != FINAL_SCORE):
            makeBall.ball_dx = 0
            score.pen.clear()
            score.pen.write(startGame.player1 + " wins!", align="center",font=("Arial",24,"bold"))

            time.sleep(5)
            break
        elif (player_2_score == FINAL_SCORE and player_1_score != FINAL_SCORE):
            makeBall.ball_dx = 0
            score.pen.clear()
            score.pen.write(startGame.player2 + " wins!", align="center",font=("Arial",24,"bold"))

            time.sleep(5)
            break

#################################################################################
# Main function for the game.
#################################################################################
def main():
    startGame()
    leftPaddle()
    rightPaddle()
    makeBall()
    score()
    vertLineOne()
    vertLineTwo()
    vertLineThree()    
    horizLineOne()
    horizLineTwo()
    pingPong()

# Allow interpreter to recognize what to run in a "Pythonic" way.
if __name__ == "__main__":
    main()