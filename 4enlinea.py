import numpy


def creartablero():
	#Crea un array de 6 filas y 7 columnas con todos valores de 0
	tablero = numpy.zeros((6,7))
	return tablero



tablero = creartablero()
#print(tablero)

findeljuego = False
turno = 0

while not findeljuego:
	if turno==0:
		jugada = int(input("Haz tu jugada Jugador 1 (0-6)"))
		print(jugada)
		print(type(jugada))

	else:
		jugada = int(input("Haz tu jugada Jugador 2 (0-6)"))

	turno=0 if turno==1 else 1
