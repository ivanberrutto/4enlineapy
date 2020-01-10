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
			#print("dou")
			contador+=1
		if contador==4:
			return True
		n+=1

	if not 0 in tablero:
		print("¡Hubo un empate!")





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
	if not(posicionvalida(tablero,col)):
		continue
	fila = proximafila(tablero,col)
	ponerficha(tablero,fila,col,turno)
	dibujartablero(tablero)
	if movimientoganador(tablero,fila,col,turno):
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
