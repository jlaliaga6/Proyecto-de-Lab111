import turtle
import time
import random

posponer = 0.1

#MARCADOR
score = 0
high_score = 0

#CONFIGURACION DE LA VENTANA
wn = turtle.Screen()
wn.title("juego de pong")
wn.bgcolor("black")
wn.tracer(0)


#CABEZA SERPIENTE
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"


#COMIDA
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)


#CUERPO SERPIENTE
segmentos = []


#TEXTO
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0          High Score: 0", align="center", font=("Courier", 18, "normal"))

#FUNCIONES
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"


def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#TECLADO
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")


while True:
    wn.update()

    #COLIDIONES BORDES
    if cabeza.xcor() > 280 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        #ESCONDER LOS SEGMENTOS
        for segmento in segmentos:
            segmento.goto(1000,1000)

        #LIMPIAR LISTA DE SEGMENTOS
        segmentos.clear()

        #RESETEAR MARCADOR
        score = 0
        texto.clear()
        texto.write("Score: {}      High Score: {}".format(score, high_score),
                    align="center", font=("Courier", 18, "normal"))


    #COLISIONES COMIDA
    if cabeza.distance(comida) < 20:

        #MOVER LA CABEZA A POSICION RANDOM
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        #AUMENTAR MARCADOR
        score += 10
        if score > high_score:
            high_score = score

        texto.clear()
        texto.write("Score: {}          High Score: {}".format(score, high_score),
                    align="center", font=("Courier", 18, "normal"))



    #MOVER EL CUERPO DE LA SERPIENTE
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index -1].xcor()
        y = segmentos[index -1].ycor()
        segmentos[index].goto(x,y)
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()

    #COLISIONES DE CUERPO
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            #ESCONDER LOS SEGMENTOS
            for segmento in segmentos:
                segmento.goto(1000,1000)

            #LIMPIAR LOS ELEMENTOS DE LA LISTA
            segmentos.clear()

            # RESETEAR MARCADOR
            score = 0
            texto.clear()
            texto.write("Score: {}      High Score: {}".format(score, high_score),
                        align="center", font=("Courier", 18, "normal"))

    time.sleep(posponer)
