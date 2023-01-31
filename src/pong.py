#################################################################################
# Authored By: Markus Walker
# Inspired By: https://github.com/srimani-programmer/Ping-Pong-Game
# Date Modified: 1/31/23
#
# Descrption: Simple Ping Pong game developed in Python using the 
# turtle module. Bring a friend and settle once and for all who is
# the alpha Pong player. Player 1 uses controls 'w' and 's', while
# Player 2 uses controls Up and Down.
#################################################################################

import turtle, os, time
from tkinter import *

player_1_score = 0
player_2_score = 0

HBORDER = 360
VBORDER = 250
VBORDER2 = 350
COLLISION1 = 340
COLLISION2 = 350
SHIFT = 40
FINAL_SCORE = 10

def startGame():
    print("Welcome to Python Ping-Pong!")
    startGame.player1 = input("Player 1, enter your name: ")
    startGame.player2 = input("Player 2, enter your name: ")
    print("Let's play Python Ping-Pong!")

    splashScreen()

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

def splashScreen():
    splash_screen = Tk()
    splash_screen.title("Welcome to Python Ping-Pong!")
    splash_screen.overrideredirect(True)

    picture = PhotoImage(file="splash-screen.png") 
    splash_label = Label(splash_screen, image=picture, bg="white")       
    splash_label.pack()

    width = splash_screen.winfo_reqwidth()
    height = splash_screen.winfo_reqheight()
    
    pos_up = int(splash_screen.winfo_screenwidth()/2 - width/2)
    pos_down = int(splash_screen.winfo_screenheight()/2 - height/2)
    splash_screen.geometry("+{}+{}".format(pos_up, pos_down))

    splash_screen.after(5000,splash_screen.destroy)
    splash_screen.mainloop()

def leftPaddle():
    leftPaddle.left_paddle = turtle.Turtle()
    leftPaddle.left_paddle.speed(0)
    leftPaddle.left_paddle.shape("square")
    leftPaddle.left_paddle.color("green")
    leftPaddle.left_paddle.shapesize(stretch_wid=4,stretch_len=1)
    leftPaddle.left_paddle.penup()
    leftPaddle.left_paddle.goto(-350,0)

def left_paddle_up():
    y = leftPaddle.left_paddle.ycor()
    y += 50
    leftPaddle.left_paddle.sety(y)

def left_paddle_down():
    y = leftPaddle.left_paddle.ycor()
    y -= 50
    leftPaddle.left_paddle.sety(y)

def rightPaddle():
    rightPaddle.right_paddle = turtle.Turtle()
    rightPaddle.right_paddle.speed(0)
    rightPaddle.right_paddle.shape("square")
    rightPaddle.right_paddle.shapesize(stretch_wid=4,stretch_len=1)
    rightPaddle.right_paddle.color("red")
    rightPaddle.right_paddle.penup()
    rightPaddle.right_paddle.goto(350,0)

def right_paddle_up():
    y = rightPaddle.right_paddle.ycor()
    y += 50
    rightPaddle.right_paddle.sety(y)

def right_paddle_down():
    y = rightPaddle.right_paddle.ycor()
    y -= 50
    rightPaddle.right_paddle.sety(y)

def makeBall():
    makeBall.ball = turtle.Turtle()
    makeBall.ball.speed(0)
    makeBall.ball.shape("circle")
    makeBall.ball.color("black")
    makeBall.ball.penup()
    makeBall.ball.goto(0,0)
    makeBall.ball_dx = 0.5
    makeBall.ball_dy = 0.5

def score():
    score.pen = turtle.Turtle()
    score.pen.speed(0)
    score.pen.color("blue")
    score.pen.penup()
    score.pen.hideturtle()
    score.pen.goto(0,260)
    score.pen.write("SCOREBOARD\n\n\n", align="center", font=("Arial", 24, "bold"))
    score.pen.write(startGame.player1.upper() + ": 0                    " + startGame.player2.upper() + ": 0 ",align="center",font=("Arial", 24, "bold"))

def vertLineOne():
    vert_line = turtle.Turtle()
    vert_line.speed(0)
    vert_line.shape("square")
    vert_line.shapesize(stretch_wid=52,stretch_len=1)
    vert_line.color("black")
    vert_line.penup()
    vert_line.goto(0,-200)

def vertLineTwo():
    vert2_line = turtle.Turtle()
    vert2_line.speed(0)
    vert2_line.shape("square")
    vert2_line.shapesize(stretch_wid=52,stretch_len=1)
    vert2_line.color("black")
    vert2_line.penup()
    vert2_line.goto(540,-200)

def vertLineThree():
    vert3_line = turtle.Turtle()
    vert3_line.speed(0)
    vert3_line.shape("square")
    vert3_line.shapesize(stretch_wid=52,stretch_len=1)
    vert3_line.color("black")
    vert3_line.penup()
    vert3_line.goto(-500,-200)

def horizLineOne():
    horiz_line = turtle.Turtle()
    horiz_line.speed(0)
    horiz_line.shape("square")
    horiz_line.shapesize(stretch_wid=1,stretch_len=52)
    horiz_line.color("black")
    horiz_line.penup()
    horiz_line.goto(30,310)

def horizLineTwo():
    horiz2_line = turtle.Turtle()
    horiz2_line.speed(0)
    horiz2_line.shape("square")
    horiz2_line.shapesize(stretch_wid=1,stretch_len=52)
    horiz2_line.color("black")
    horiz2_line.penup()
    horiz2_line.goto(30,-380)

def pingPong():
    while True:
        startGame.window.update()

        makeBall.ball.setx(makeBall.ball.xcor() + makeBall.ball_dx)
        makeBall.ball.sety(makeBall.ball.ycor() + makeBall.ball_dy)

        if ((leftPaddle.left_paddle.ycor() > VBORDER)):
            leftPaddle.left_paddle.sety(VBORDER)

        elif ((leftPaddle.left_paddle.ycor() < -VBORDER)):
            leftPaddle.left_paddle.sety(-VBORDER)

        if ((rightPaddle.right_paddle.ycor() > VBORDER)):
            rightPaddle.right_paddle.sety(VBORDER)

        elif ((rightPaddle.right_paddle.ycor() < -VBORDER)):
            rightPaddle.right_paddle.sety(-VBORDER)

        if (makeBall.ball.ycor() > VBORDER):
            makeBall.ball.sety(VBORDER)
            makeBall.ball_dy *= -1
        
        elif (makeBall.ball.ycor() < -VBORDER2):
            makeBall.ball.sety(-VBORDER2)
            makeBall.ball_dy *= -1
            
        if (makeBall.ball.xcor() > HBORDER):   
            makeBall.ball.goto(0,0)
            makeBall.ball_dx *= -1
            global player_1_score, player_2_score
            player_1_score += 1

            score.pen.clear()
            score.pen.write("SCOREBOARD\n\n\n", align="center", font=("Arial", 24, "bold"))
            score.pen.write(startGame.player1.upper() + ": " + str(player_1_score) + "                  " + startGame.player2.upper() + ": " + str(player_2_score) + " ".format(player_1_score, player_2_score), align="center", font=('Arial',24,"bold"))

        if (makeBall.ball.xcor()) < -HBORDER:
            makeBall.ball.goto(0,0)
            makeBall.ball_dx *= -1
            player_2_score += 1

            score.pen.clear()
            score.pen.write("SCOREBOARD\n\n\n", align="center", font=("Arial", 24, "bold"))
            score.pen.write(startGame.player1.upper() + ": " + str(player_1_score) + "                  " + startGame.player2.upper() + ": " + str(player_2_score) + " ".format(player_1_score, player_2_score), align="center", font=('Arial',24,"bold"))

        if (makeBall.ball.xcor() > COLLISION1) and (makeBall.ball.xcor() < COLLISION2) and (makeBall.ball.ycor() < rightPaddle.right_paddle.ycor() + SHIFT and makeBall.ball.ycor() > rightPaddle.right_paddle.ycor() - SHIFT):
            makeBall.ball.setx(COLLISION1)
            makeBall.ball_dx *= -1

        elif (makeBall.ball.xcor() < -COLLISION1) and (makeBall.ball.xcor() > -COLLISION2) and (makeBall.ball.ycor() < leftPaddle.left_paddle.ycor() + SHIFT and makeBall.ball.ycor() > leftPaddle.left_paddle.ycor() - SHIFT):
            makeBall.ball.setx(-COLLISION1)
            makeBall.ball_dx *= -1
        
        if (player_1_score < FINAL_SCORE and player_2_score < FINAL_SCORE):
            continue
        elif (player_1_score == FINAL_SCORE and player_2_score != FINAL_SCORE):
            makeBall.ball_dx = 0
            score.pen.clear()
            score.pen.write(startGame.player1.upper() + " WINS!\n\n\n", align="center", font=("Arial",24,"bold"))

            time.sleep(5)
            break
        elif (player_2_score == FINAL_SCORE and player_1_score != FINAL_SCORE):
            makeBall.ball_dx = 0
            score.pen.clear()
            score.pen.write(startGame.player2.upper() + " WINS!\n\n\n", align="center", font=("Arial",24,"bold"))

            time.sleep(5)
            break

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

if __name__ == "__main__":
    main()