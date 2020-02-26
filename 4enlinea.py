import numpy
import pygame
import sys
import math

#Inicia la libreria de pygame
pygame.init()
def main():



	cantidadjugadores=2
	cantidadfilas=6
	cantidadcol=7

	azul=(0,0,255)
	amarillo= (255,255,0)
	rojo=(255,0,0)
	negro=(0,0,0)
	verde=(0,143,57)
	blanco=(255,255,255)
	rosa = (234,137,154)
	violeta = (76,40,130)
	celeste = (81,209,246)
	marron = (78,59,0)
	naranja = (255,128,0)
	gris = (156,156,156)

	colorjugadores = []
	pantmenu = pygame.display.set_mode((800,600))
	pygame.display.set_caption('4 en Linea')
	pygame.display.set_icon(pygame.image.load("icono.png"))
	class boton():
	    def __init__(self, color, x,y,ancho,alto, texto='', colordeltexto=negro):
	        self.color = color
	        self.x = x
	        self.y = y
	        self.ancho = ancho
	        self.alto = alto
	        self.texto = texto
	        self.colordeltexto = colordeltexto

	    def imprimir(self,pant,outline=None):
	        #Este metodo dibuja el boton
	        if outline:
	            pygame.draw.rect(pant, outline, (self.x-2,self.y-2,self.ancho+4,self.alto+4),0)
	            
	        pygame.draw.rect(pant, self.color, (self.x,self.y,self.ancho,self.alto),0)
	        
	        if self.texto != '':
	            font = pygame.font.SysFont('comicsans', 30)
	            texto = font.render(self.texto, 1, self.colordeltexto)
	            pant.blit(texto, (self.x + (self.ancho/2 - texto.get_width()/2), self.y + (self.alto/2 - texto.get_height()/2)))

	    def isOver(self, pos):
	        #Detecta si el mouse esta sobre el boton
	        if pos[0] > self.x and pos[0] < self.x + self.ancho:
	            if pos[1] > self.y and pos[1] < self.y + self.alto:
	                return True
	            
	        return False

	botonjugar = boton(rojo,300,10,200,100,"Jugar")

	botontutorial = boton(rojo,300,160,200,100,"Tutorial")

	botonconfiguracion = boton(rojo,300,310,200,100,"Colores")

	botonsalir = boton(rojo,300,460,200,100,"Salir")
	#pygame.draw.rect(pantmenu,rojo,(100,100,100,100))
	#label = myfont.render("Jugar",1,(255,255,255))
	#pantmenu.blit(label,(100,100))
	pygame.display.update()

	def imprimirbotones():
		pantmenu.fill(blanco)
		botonjugar.imprimir(pantmenu,negro)
		botontutorial.imprimir(pantmenu,negro)
		botonsalir.imprimir(pantmenu,negro)
		botonconfiguracion.imprimir(pantmenu,negro)
		pygame.display.update()


	comienzodeljuego=False
	while not comienzodeljuego:
		imprimirbotones()
		for event in pygame.event.get():
			pos = pygame.mouse.get_pos()

			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_j:
					comienzodeljuego=True
			if event.type == pygame.MOUSEMOTION:
				if botonjugar.isOver(pos):
					botonjugar.color=verde
				else:
					botonjugar.color=rojo

				if botontutorial.isOver(pos):
					botontutorial.color=verde
				else:
					botontutorial.color=rojo

				if botonsalir.isOver(pos):
					botonsalir.color=verde
				else:
					botonsalir.color=rojo

				if botonconfiguracion.isOver(pos):
					botonconfiguracion.color=verde
				else:
					botonconfiguracion.color=rojo

			if event.type == pygame.MOUSEBUTTONDOWN:
				if botonjugar.isOver(pos):
					comienzodeljuego=True

				if botontutorial.isOver(pos):
					pantmenu.fill(blanco)
					pantmenu.blit(pygame.image.load("tutorial.jpg"), (0,0))
					botonvolver = boton(rojo,10,10,100,50,"Volver")
					botonvolver.imprimir(pantmenu,negro)
					pygame.display.update()
					volver=False
					while not volver:
						for event in pygame.event.get():
							pos = pygame.mouse.get_pos()
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_ESCAPE:
									volver=True
							if event.type == pygame.QUIT:
								sys.exit()
							if event.type == pygame.MOUSEBUTTONDOWN:
								if botonvolver.isOver(pos):
									volver=True


				if botonsalir.isOver(pos):
					sys.exit()
				if botonconfiguracion.isOver(pos):
					pantmenu.fill(blanco)
					configfont = pygame.font.SysFont("monospace",20)
					label = configfont.render("Elegir color",1,negro)
					pantmenu.blit(label,(300,20))
					botonvolver = boton(rojo,10,10,100,50,"Volver")
					botonvolver.imprimir(pantmenu,negro)
					pygame.display.update()
					volver=False
					'''
					botonverde=[]
					botonamarillo=[]
					botonazul=[]
					botonrosa=[]
					botonblanco=[]
					botonvioleta=[]

					'''
					botonescolores=[]
					botonverde= boton(verde,10,200,100,100,"verde")
					botonverde.imprimir(pantmenu,negro)
					botonescolores.append(botonverde)
					botonamarillo=boton(amarillo,150,200,100,100,"amarillo")
					botonamarillo.imprimir(pantmenu,negro)
					botonescolores.append(botonamarillo)
					botonazul=boton(azul,300,200,100,100,"azul")
					botonazul.imprimir(pantmenu,negro)
					botonescolores.append(botonazul)
					botonrosa=boton(rosa,450,200,100,100,"rosa")
					botonrosa.imprimir(pantmenu,negro)
					botonescolores.append(botonrosa)
					botonvioleta=boton(violeta,600,200,100,100,"violeta")
					botonvioleta.imprimir(pantmenu,negro)
					botonescolores.append(botonvioleta)

					botonceleste=boton(celeste,10,400,100,100,"celeste")
					botonceleste.imprimir(pantmenu,negro)
					botonescolores.append(botonceleste)
					botonmarron=boton(marron,150,400,100,100,"marron")
					botonmarron.imprimir(pantmenu,negro)
					botonescolores.append(botonmarron)
					botonblanco=boton(blanco,300,400,100,100,"blanco")
					botonblanco.imprimir(pantmenu,negro)
					botonescolores.append(botonblanco)	
					botonnaranja=boton(naranja,450,400,100,100,"naranja")
					botonnaranja.imprimir(pantmenu,negro)
					botonescolores.append(botonnaranja)	
					botongris=boton(gris,600,400,100,100,"gris")
					botongris.imprimir(pantmenu,negro)
					botonescolores.append(botongris)			
					pygame.display.update()

					colorjugadores.clear()
					x=0
					while x<cantidadjugadores:
						pygame.draw.rect(pantmenu,blanco,(50,150,600,40))
						label = configfont.render("Elegi color Jugador "+str(x+1),1,negro)
						pantmenu.blit(label,(300,150))
						pygame.display.update()
						for event in pygame.event.get():
							pos = pygame.mouse.get_pos()
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_ESCAPE:
									x=9999
									continue
							if event.type == pygame.QUIT:
								sys.exit()
							if event.type == pygame.MOUSEBUTTONDOWN:
								if botonvolver.isOver(pos):
									x=9999
									continue
								for y in range(len(botonescolores)):
									if botonescolores[y].isOver(pos):
										colordelboton=botonescolores[y].color
										if colordelboton in colorjugadores:
											#pygame.draw.rect(pantmenu,blanco,(50,450,600,40))
											label= configfont.render("Ese color ya esta seleccionado",1,rojo)
											pantmenu.blit(label,(200,335))
											continue

										botonescolores[y].imprimir(pantmenu,rojo)
										colordelboton=botonescolores[y].color
										print(colordelboton)
										colorjugadores.append(colordelboton)
										x+=1


	if len(colorjugadores)==0:
		colorjugadores=[azul,amarillo]
	if len(colorjugadores)==1:
		colorjugadores.append(amarillo)
	puntuacionjugadores = [0,0]
	def reiniciarjuego():
		tablero = numpy.zeros((cantidadfilas,cantidadcol))
		turno = 1
		for c in range(cantidadcol):
			for r in range(cantidadfilas):
				pygame.draw.rect(pant,rojo,(c*tamañocasilla,r*tamañocasilla+tamañocasilla,tamañocasilla,tamañocasilla))
				pygame.draw.circle(pant,negro,(int(c*tamañocasilla+tamañocasilla/2),int(r*tamañocasilla+tamañocasilla+tamañocasilla/2)),radio)
		pygame.draw.rect(pant,negro,(0,0,ancho,tamañocasilla))
		pos = pos = pygame.mouse.get_pos()[0]
		for x in range(len(puntuacionjugadores)):
			label = puntfont.render("Jug "+str(x+1)+": "+str(puntuacionjugadores[x]),1,colorjugadores[x])
			pant.blit(label,(0,15*x+15))						
		pygame.draw.circle(pant, colorjugadores[turno-1], (pos,int(tamañocasilla/2)),radio)
		pygame.display.update()
		return (tablero,turno)


	def graficartablero(tablero,turno):
		for c in range(cantidadcol):
			for r in range(cantidadfilas):
				pygame.draw.rect(pant,rojo,(c*tamañocasilla,r*tamañocasilla+tamañocasilla,tamañocasilla,tamañocasilla))
				pygame.draw.circle(pant,negro,(int(c*tamañocasilla+tamañocasilla/2),int(r*tamañocasilla+tamañocasilla+tamañocasilla/2)),radio)

		#for c in range(cantidadcol):
		#	for r in range(cantidadfilas):
		#		if tablero[r][c] == turno:
		#			pygame.draw.circle(pant,colorjugadores[turno],(int(c*tamañocasilla+tamañocasilla/2),alto-int(r*tamañocasilla+tamañocasilla/2)),radio)


	def graficarjugada(tablero,fila,col,turno):
		pygame.draw.circle(pant,colorjugadores[turno-1],(int(col*tamañocasilla+tamañocasilla/2),alto-int(fila*tamañocasilla+tamañocasilla/2)),radio)



	#Verifica si se puede poner ficha en esa columna, entrega True si se puede(0)
	def posicionvalida(tablero, col):
		return tablero[cantidadfilas-1][col] == 0

	#Hace un for que busca la primera fila de la columna elegida que tenga un 0 ( no tenga ficha )
	def proximafila(tablero, col):
		for r in range(cantidadfilas):
			if tablero[r][col] == 0:
				return r

	def ponerficha(tablero,fila,col,turno):
		tablero[fila][col] = turno

	def creartablero():
		#Crea un array de 6 filas y 7 columnas con todos valores de 0
		tablero = numpy.zeros((cantidadfilas,cantidadcol))
		return tablero

	#Da vuelta el tablero para que sea entendible
	def dibujartablero(tablero):
		print(numpy.flip(tablero,0))


	"""def movimientoganador(tablero,fila,col,turno):
		#Movimientos horizontales

		#Hay que restarle 3 a la cantidad de columnas porque no puede comenzar un horizontal ganador en las ultimas 3 columnas
		for c in range(cantidadcol-3):
			for r in range(cantidadfilas):
				if tablero[r][c] == turno and tablero[r][c+1] == turno and tablero[r][c+2] == turno and tablero[r][c+3] == turno:
					return True


		#Movimientos verticales
		for c in range(cantidadcol):
			# Hay que restarle 3 a la cantidad de filas porque no puede comenzar un vertical ganador en las ultimas 3 filas
			for r in range(cantidadfilas-3):
				if tablero[r][c] == turno and tablero[r+1][c] == turno and tablero[r+2][c] == turno and tablero[r+3][c] == turno:
					return True

		#Diagonal positiva
		for c in range(cantidadcol-3):
			for r in range(cantidadfilas-3):
				if tablero[r][c] == turno and tablero[r+1][c+1] == turno and tablero[r+2][c+2] == turno and tablero[r+3][c+3] == turno:
					return True
		#Diagonal negativa
		for c in range(cantidadcol-3):
			for r in range(cantidadfilas):
				if tablero[r][c] == turno and tablero[r-1][c+1] == turno and tablero[r-2][c+2] == turno and tablero[r-3][c+3] == turno:
					return True
	"""

	def movimientoganador(tablero,fila,col,turno):	
		#Horizontal
		contador=0
		for c in range(cantidadcol):
			if tablero[fila][c] == turno:
				contador+=1
			else:
				contador=0
			if contador==4:
				return True
		#Vertical
		contador=0

		for r in range(cantidadfilas):
			if tablero[r][col] == turno:
				contador+=1
			else:
				contador=0
			if contador==4:
				return True

		x=1
		while x:
			if fila-x<0:
				x-=1
				break
			if col-x<0:
				x-=1
				break
			x+=1

		#print(str(fila-x)+","+str(col-x))
		contador=0
		filaf=fila-x
		colc=col-x
		y=0
		while True:
			if(colc+y) >= cantidadcol or filaf+y >= cantidadfilas:
				break
			if tablero[filaf+y][colc+y] == turno:
				contador+=1
			#add
			else:
				contador=0
			if contador==4:
				return True
			y+=1
		
		#Diagonal positiva
		z=1
		while True:
			if fila+z>=cantidadfilas:
				#print("quebro f")
				break
			if col-z<0:
				#print("quebro c")
				break
			z+=1
		#print(str(fila+z-1)+","+str(col-z+1))
		filaz= fila+z-1
		colz= col-z+1

		#Diagonal negativa
		contador=0
		n=0
		while True:
			if(colz+n) >= cantidadcol or (filaz-n) < 0:
				break
			if tablero[filaz-n][colz+n] == turno:
				contador+=1
			#add
			else:
				contador=0
			if contador==4:
				return True
			n+=1






	tablero = creartablero()
	#print(tablero)



	tamañocasilla= 100
	radio= int((tamañocasilla/2.1))
	alto = (cantidadfilas+1) * tamañocasilla
	ancho= cantidadcol * tamañocasilla

	tamañodeljuego=(ancho,alto)
	print(tamañodeljuego)
	pant = pygame.display.set_mode(tamañodeljuego)






	findeljuego = False
	turno = 1
	graficartablero(tablero,turno)
	pygame.display.update()
	dibujartablero(tablero)

	puntfont = pygame.font.SysFont("comicsans",20)
	label = puntfont.render("Jug "+str(turno)+": "+str(puntuacionjugadores[turno-1]),1,colorjugadores[turno-1])
	pant.blit(label,(20,20))	
	pygame.display.update()



	cartelfont = pygame.font.SysFont("monospace",50)
	while not findeljuego:

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					main()
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEMOTION:
				pygame.draw.rect(pant,negro,(0,0,ancho,tamañocasilla))
				pos = event.pos[0]
				for x in range(len(puntuacionjugadores)):
					label = puntfont.render("Jug "+str(x+1)+": "+str(puntuacionjugadores[x]),1,colorjugadores[x])
					pant.blit(label,(0,15*x+15))						
				pygame.draw.circle(pant, colorjugadores[turno-1], (pos,int(tamañocasilla/2)),radio)
				pygame.display.update()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					tablero,turno = reiniciarjuego()


			if event.type == pygame.MOUSEBUTTONDOWN:
				print(event.pos)

				#if turno==1:

				pos = event.pos[0]
				#Redondea para abajo
				col =  int(math.floor(pos/tamañocasilla))
				#col = int(input("Haz tu jugada Jugador "+str(turno)+" (0-6):"))
				print(col)
				if (col>cantidadfilas):
					print("Tienes que elegir una columna del 0 al 6")
					continue
				if not(posicionvalida(tablero,col)):
					continue
				fila = proximafila(tablero,col)
				ponerficha(tablero,fila,col,turno)
				dibujartablero(tablero)
				graficarjugada(tablero,fila,col,turno)
				pygame.display.update()
				if movimientoganador(tablero,fila,col,turno):
					pygame.draw.rect(pant,negro,(0,0,ancho,tamañocasilla))
					label = cartelfont.render("Gano el jugador "+str(turno),1,colorjugadores[turno-1])
					pant.blit(label,(40,20))
					print("Gano el jugador "+str(turno)+"!")
					pygame.display.update()
					puntuacionjugadores[turno-1]+=1
					accion=False
					while not accion:
						for event in pygame.event.get():
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_ESCAPE:
									main()
							if event.type == pygame.QUIT:
								sys.exit()
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_r:
									tablero,turno = reiniciarjuego()
									accion = True
					continue
					#pygame.time.wait(10000)
					#findeljuego=True
				if not 0 in tablero:
					label = cartelfont.render("¡Hubo un empate!",1,rojo)
					pant.blit(label,(40,20))
					pygame.display.update()
					pygame.time.wait(1000)
					tablero,turno = reiniciarjuego()
					continue



				#else:
					#col = int(input("Haz tu jugada Jugador 2 (0-6):"))
					#if (col>cantidadfilas):
					#	print("Tienes que elegir una columna del 0 al 6")
					#	continue
					#if(posicionvalida(tablero,col)):
					#	fila = proximafila(tablero,col)
					#	ponerficha(tablero,fila,col,turno)
					#	dibujartablero(tablero)

				turno=1 if turno==2 else 2
				pygame.draw.circle(pant, colorjugadores[turno-1], (pos,int(tamañocasilla/2)),radio)
				pygame.display.update()
main()