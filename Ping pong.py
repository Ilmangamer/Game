
# I am going to code a ping pong game in python.
# I will use turtle module.
# I will first start by importing the module.
# Then I will make the screen.
# Then I will make one paddle.
# Then the other paddle.
# Then I will make the ball and the pen.
# Then i want to make an introductory text.
# I also want to track the score.
# I want to track the movements of the paddle.
# I also want python to notice when I press keybinds.
# I want the main game loop to update. 
# I need to see movements on the ball, and stop the ball and stop the ball when it hits the border.
# I also want to write a score for each player.



import turtle


wn = turtle.Screen()
wn.title("Black Mamba")
wn.bgcolor("dark blue")
wn.setup( width=800,  height=600)
wn.tracer(0)

# A Paddle (nbhkabb aojq)

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)



# Paddle B


paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy =-0.25

# Pen -
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Welcome to my Black Mamba Game." 

"You are Player A and Player B",
 align="center", font=("Courier", 14, "normal"))

# Score
score_a = 0
score_b = 0




# Movements - Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)



def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)



def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)



def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)



# keyboard bindings

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop 
while True:
    
    wn.update()
    

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
# Border checking
    if ball.ycor() > 290:
       ball.sety(290)
       ball.dy *= -1 
       
       

       


      

       

    if ball.ycor() < -290:
          ball.sety(-290)
          ball.dy *= -1 
          fname = "C:\\VS Code\\Python\\bounce.wav"
          
         


    if ball.xcor() > 390: 
        ball.goto(0, 0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}". format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390: 
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}". format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
      
      
# paddle and collisons
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1



    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1


# Errors and bugs.
# I had some issues.
# With my plan, the ball kept going through my paddle.
# I had to make some codes to fix this bug.
# The code i made was under paddle and collisons.
# I had error such as IndentationError and Nameerrors.
    










    



turtle.mainloop()
