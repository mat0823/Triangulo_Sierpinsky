 #Tarea01_2019.py
 	
import time
import turtle
import random

#

def main():
    iteracion = leeValor('Ingrese numero de la iteración (máx 6): ', 0, 6)
    eleccion = leeValor('Escoja Estilos: A la Chilena(0), Suave(1), Blanco(2), Aleatorio(3): ', 0, 3)
    eleccionBorde = leeValor('Escoja Color Borde: Negro(0), Rojo(1), Persian Green(2), Aleatorio(3): ', 0, 3)
    Lado = leeValor('Escoja la medida del lado del triangulo: Minimo (150), Maximo (400): ',150 , 400)
    colorBorde = EstilosBordes(eleccionBorde)
    Fondo = EstilosColores(eleccion) 
    t = turtle.Turtle()
    inicializaTortuga(t)
    vertices = [[-Lado,-Lado],[0,Lado],[Lado,-Lado]]
    sierpinski(vertices, iteracion, t, Fondo, colorBorde)
    turtle.done()
   
#ValidacionIteracion

def leeValor(texto, Min, Max):
	class Error(Exception):
		pass
	class Nada(Error):
		pass
	class Solo_Espacios(Error):
		pass
	class OutRange(Error):
		pass
		
	sigue = True
	while (sigue):
		try:
			valor = input(texto)
			if (len(valor) == 0):
				raise Nada
			elif (ValidaEspacios(valor)):
				raise Solo_Espacios
			else:
				n = int(valor)
				if (n < Min or n > Max):
					raise OutRange
			return n
		
		except (ValueError):
			print("Ingreso algo diferente a un entero.")
		except (Nada):
			print("No ingresó nada.")
		except (Solo_Espacios):
			print("Ingresó solo espacios en blanco.")
		except (OutRange):
			print("Ingresó un número fuera de rango.")

#ValidaEspacios

def ValidaEspacios(valor):
	cont = 0
	for i in range(len(valor)):
		if(valor[i] == ' '):
			cont += 1
	if(cont == len(valor)):
		return True
	else:
		return False

#OpcionesSetup

def inicializaTortuga(t):
    Resolucion = turtle.Screen()
    Resolucion.colormode(255)
    Resolucion.setup (width=1200, height=900, startx=0, starty=0)
    t.speed(100)
    
# OpcionesDeDibujo

def Define_style(vertices, colores, t, colorBorde):
    t.fillcolor(colores)
    t.pencolor(colorBorde)
    t.pensize(2)	
    t.up()
    t.goto(vertices[0][0],vertices[0][1])
    t.down()
    t.begin_fill()
    for i in range(1,4):
        t.goto(vertices[i%3][0],vertices[i%3][1])
        time.sleep(0.1)
    t.end_fill()

# Estilos Bordes

def EstilosBordes(Eleccion):
    x = random.randint(0,255)
    y = random.randint(0,255)
    z = random.randint(0,255)
    t = (x,y,z)
    if(Eleccion == 1):
        Color1 = (255,0,0)
        return Color1
    elif(Eleccion == 0):
        Color2 = (0,0,0)
        return Color2
    elif(Eleccion == 2):
        Color3 = (0,153,153)
        return Color3
    else:
        return t
 
#EstilosColores 
#	https://rgbcolorcode.com/

def EstilosColores(NumColor):
    Aleatorio = []
    for color in range(7):
        x = random.randint(0,255)
        y = random.randint(0,255)
        z = random.randint(0,255)
        t = (x,y,z)
        Aleatorio.append(t)
    if(NumColor == 1):
        Color1 = [(213,204,255),(204,255,238),
                    (221,255,204),(255,255,204),
                    (255,230,204),(255,204,204),(191,255,179)]
        return Color1
    elif(NumColor == 0):
        Color2 = [(255,255,255),(25,25,255),
                    (255,0,0),(255,255,255),
                    (25,25,255),(255,0,0),(25,25,255)] 
        return Color2
    elif(NumColor == 2):
        Color3 = [(255,255,255),(255,255,255),
                    (255,255,255),(255,255,255),
                    (255,255,255),(255,255,255),(255,255,255)]
        return Color3
    else:
        return Aleatorio
      
# GeneradorDeVertices

def Vertices(vertice1, vertice2):
    return [(vertice1[0] + vertice2[0])/2, (vertice1[1] + vertice2[1])/2]
      
      
# Generador de triangulos

def sierpinski(vertices, iteracion, t, Fondo,colorBorde):
    Define_style(vertices, Fondo[iteracion],t ,colorBorde)
    if(iteracion > 0):
        for i in range(3):
            sierpinski([vertices[i],
                Vertices(vertices[2%(i+1)], vertices[1]),
                Vertices(vertices[3%(i+1)], vertices[2])], iteracion - 1, t , Fondo, colorBorde)

#

main()
