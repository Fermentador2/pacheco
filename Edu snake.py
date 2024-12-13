import turtle 
import time
import random 

#variables basicas<--- notas
# aclaracion de que esto son variables  
delay = 0.1
score=0
high_score=0

#configurar ventana
wn= turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#la serpiente
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color("white")
head.penup()
head.goto(0,0)
head.direction="Stop"

#la comida
food=turtle.Turtle()
colors = random.choice(['red','blue','green'])
shapes= random.choice(['square','circle','triangle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0,100)

#el texto del score
segments=[]
pen=turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score : 0 High Score: 0", align="center",font=("arial",24,"bold"))

#2 clase. Funciones, los mecanismos que hacen que funcione el juego
def goup():
    if head.direction !="down":
        head.direction = "up"
def godown():
    if head.direction != "up":
       head.direction = "down" 
def goleft():
    if head.direction != "right":
       head.direction = "left"
def goright():
    if head.direction != "left":
       head.direction = "right"

def move():
     if head.direction == "up":
         y=head.ycor()
         head.sety(y+20)

     if head.direction == "down":
         y=head.ycor()
         head.sety(y-20)

     if head.direction == "left":
         x=head.xcor()
         head.setx(x-20)

     if head.direction == "right":
         x=head.xcor()
         head.setx(x+20)

         
wn.listen()
wn.onkeypress(goup,"w")
wn.onkeypress(godown,"s")
wn.onkeypress(goleft,"a")  
wn.onkeypress(goright,"d")

#3 Clase. Funcionamiento principal del programa (main gameloop) C&P

while True:
    wn.update()
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(0.3)    
        head.goto(0,0)
        head.direction = "stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])

        for segments in segments:
            segments.goto(10000,10000)
        segments.clear()    

        score = 0
        delay=0.1
        pen.clear()
        pen.write("Score : {} High Score: {}", format(score, high_score), align="center",font=("arial",24,"bold"))

    if head.distance(food)<20:
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        food.goto(x,y)

        score += 10
        if score > high_score:
            high_score = score
            pen.clear()
            pen.write("Score : {} High Score: {}".format(score, high_score), align="center",font=("arial",24,"bold"))

        new_segments = turtle.Turtle()
        new_segments.speed(0)
        new_segments.shape("square") 
        new_segments.color("blue")
        new_segments.penup()
        segments.append(new_segments)
        delay -=0.001
    
    for index in range(len(segments)-1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x,y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
 
    move()
    for segment in segments: 
        if segment.distance(head)<20: 
            time.sleep(1)
            head.goto(0.0)
            head.direction= "stop"
            colors = random.choice(["red", "blue", "green"])
            shapes = random.choice(["square","circle"])
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score=0
            delay=0.1
            pen.clear()
            pen.write("Score : {} High Score: {}".format(score, high_score), align="center",font=("arial",24,"bold"))
  
    
    time.sleep(delay)