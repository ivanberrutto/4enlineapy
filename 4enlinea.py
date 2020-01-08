import numpy

cantidadfilas=6
cantidadcol=7
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

def movimientoganador(tablero,turno):
	#Movimientos horizontales

	#Hay que restarle 3 a la cantidad de columnas porque no puede comenzar un horizontal ganador en las ultimas 3 columnas
	for c in range(cantidadcol-3):
		for r in range(cantidadfilas):
			if tablero[r][c] == turno and tablero[r][c+1] == turno and tablero[r][c+2] == turno and tablero[r][c+3] == turno:
				return True




tablero = creartablero()
#print(tablero)

findeljuego = False
turno = 1
dibujartablero(tablero)
while not findeljuego:
	#if turno==1:
	col = int(input("Haz tu jugada Jugador "+str(turno)+" (0-6):"))
	print(col)
	if (col>cantidadfilas):
		print("Tienes que elegir una columna del 0 al 6")
		continue
	if(posicionvalida(tablero,col)):
		fila = proximafila(tablero,col)
		ponerficha(tablero,fila,col,turno)
		dibujartablero(tablero)
		if movimientoganador(tablero,turno):
			print("Gano el jugador "+str(turno)+"!")
			findeljuego=True

	"""else:
		col = int(input("Haz tu jugada Jugador 2 (0-6):"))
		if (col>cantidadfilas):
			print("Tienes que elegir una columna del 0 al 6")
			continue
		if(posicionvalida(tablero,col)):
			fila = proximafila(tablero,col)
			ponerficha(tablero,fila,col,turno)
			dibujartablero(tablero)"""

	turno=1 if turno==2 else 2
