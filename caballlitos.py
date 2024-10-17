import random
import time

numeros = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
palos = ['Corazones rojos', 'Treboles', 'Diamantes', 'Corazones negros']
mazo = []
camino = []

class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

    def __str__(self):
        return f'{self.numero} de {self.palo}'

class CartaCamino(Carta):
    def __init__(self, numero, palo, estado=False):
        super().__init__(numero, palo)
        self.estado = estado

    def __str__(self):
        return f'En el camino sale {self.numero} de {self.palo}'

for x in numeros:
    for y in palos:
        carta = Carta(x, y)
        mazo.append(carta)

i = 1
while i <= 10:
    idea = random.choice(mazo)
    if idea not in camino: 
        carta_camino = CartaCamino(idea.numero, idea.palo, estado=False)
        camino.append(carta_camino)
        i += 1

for carta in camino:
    print(carta)

time.sleep(1)

numJugadores = 0  
while numJugadores < 2 or numJugadores > 5:
    try:
        numJugadores = int(input('¿Cuántos jugadores?\n'))
    except ValueError:
        print("Por favor ingrese un número válido entre 2 y 5.")

print(str(numJugadores) + ' jugadores')

if numJugadores == 2:
    jugador1 = input('Ingrese el nombre del jugador que va a tomar palos rojos: ')
    jugador2 = input('Ingrese el nombre del jugador que va a tomar palos negros: ')
    j1 = 0
    j2 = 0
    posCamino = 0
    print(f'{jugador1} vs. {jugador2}')
    time.sleep(1)

    while any(carta.estado == False for carta in camino):
        print("Sacando una carta del mazo...")
        time.sleep(2)
        
        propuesto = random.choice(mazo)
        print(f'Del mazo sale {propuesto}')
        time.sleep(1)

        if 'rojos' in propuesto.palo or 'Diamantes' in propuesto.palo:
            j1 += 1
            print(f'{jugador1} tiene {j1} puntos.')
            time.sleep(1)

            if camino[posCamino].estado == False and (j1 > posCamino or j2 > posCamino):
                print(f'{jugador1} avanza en el camino...')
                time.sleep(2)
                print(camino[posCamino])
                camino[posCamino].estado = True
                    
                if 'rojos' in camino[posCamino].palo or 'Diamantes' in camino[posCamino].palo:
                    if j1 > 0:
                         j1 -= 1
                    print(f'{jugador1} pierde 1 punto. Ahora tiene {j1} puntos.')
                else:
                    if j2 > 0:
                        j2 -= 1
                    print(f'{jugador2} pierde 1 punto. Ahora tiene {j2} puntos.')
                posCamino += 1
        
        else:
            j2 += 1
            print(f'{jugador2} tiene {j2} puntos.')
            time.sleep(1)

            if camino[posCamino].estado == False and (j1 > posCamino or j2 > posCamino):
                print(f'{jugador2} avanza en el camino...')
                time.sleep(2)
                print(camino[posCamino])
                camino[posCamino].estado = True

                if 'rojos' in camino[posCamino].palo or 'Diamantes' in camino[posCamino].palo:
                    if j1 > 0:
                         j1 -= 1
                    print(f'{jugador1} pierde 1 punto. Ahora tiene {j1} puntos.')
                else:
                    if j2 > 0:
                        j2 -= 1
                    print(f'{jugador2} pierde 1 punto. Ahora tiene {j2} puntos.')
                posCamino += 1

        mazo.remove(propuesto)

        if j1 == 10:
            print(f'{jugador1} ha ganado el juego.')
            break
        elif j2 == 10:
            print(f'{jugador2} ha ganado el juego.')
            break

        time.sleep(1)  

if numJugadores == 3:
    jugadores = []
    paloOmitido = ''
    while paloOmitido not in palos:
        print('Ingrese el palo que no va a jugar:')
        paloOmitido = input('Las opciones son Corazones rojos, Treboles, Diamantes, Corazones negros\n')
    
    palos.remove(paloOmitido)  

    for i in range(3):
        nombre = input(f'Ingrese el nombre del jugador que va a tomar el palo {palos[i]}\n')
        jugadores.append({"nombre": nombre, "palo": palos[i], "puntos": 0})

    posCamino = 0
    print(f'{jugadores[0]["nombre"]} vs. {jugadores[1]["nombre"]} vs. {jugadores[2]["nombre"]}')
    time.sleep(1)

    while any(carta.estado == False for carta in camino):
        print("Sacando una carta del mazo...")
        time.sleep(2)
        
        propuesto = random.choice(mazo)
        print(f'Del mazo sale {propuesto}')
        mazo.remove(propuesto)  
        time.sleep(1)

        for jugador in jugadores:
            if propuesto.palo == jugador['palo']:
                jugador['puntos'] += 1
                print(f'{jugador["nombre"]} tiene {jugador["puntos"]} puntos.')
                time.sleep(1)

                if camino[posCamino].estado == False and jugador['puntos'] > posCamino:
                    print(f'{jugador["nombre"]} avanza en el camino...')
                    time.sleep(2)
                    print(camino[posCamino])
                    camino[posCamino].estado = True

                    for jugador_camino  in jugadores:
                        if camino[posCamino].palo == jugador_camino ['palo']:
                            if jugador_camino ['puntos'] > 0:
                                jugador_camino ['puntos'] -= 1
                            print(f'{jugador_camino ["nombre"]} pierde 1 punto. Ahora tiene {jugador_camino ["puntos"]} puntos.')

                    posCamino += 1
                break

        for jugador in jugadores:
            if jugador['puntos'] == 10:
                print(f'{jugador["nombre"]} ha ganado el juego.')                
        time.sleep(1)
if numJugadores == 4:
    jugadores = []

    for i in range(4):
        nombre = input(f'Ingrese el nombre del jugador que va a tomar el palo {palos[i]}\n')
        jugadores.append({"nombre": nombre, "palo": palos[i], "puntos": 0})

    posCamino = 0
    print(f'{jugadores[0]["nombre"]} vs. {jugadores[1]["nombre"]} vs. {jugadores[2]["nombre"]} vs. {jugadores[3]["nombre"]}')
    time.sleep(1)

    while any(carta.estado == False for carta in camino):
        print("Sacando una carta del mazo...")
        time.sleep(2)
        
        propuesto = random.choice(mazo)
        print(f'Del mazo sale {propuesto}')
        mazo.remove(propuesto)  
        time.sleep(1)

        for jugador in jugadores:
            if propuesto.palo == jugador['palo']:
                jugador['puntos'] += 1
                print(f'{jugador["nombre"]} tiene {jugador["puntos"]} puntos.')
                time.sleep(1)

                if camino[posCamino].estado == False and jugador['puntos'] > posCamino:
                    print(f'{jugador["nombre"]} avanza en el camino...')
                    time.sleep(2)
                    print(camino[posCamino])
                    camino[posCamino].estado = True

                    for jugador_camino  in jugadores:
                        print (camino[posCamino].palo, jugador_camino ['palo'])
                        if camino[posCamino].palo == jugador_camino ['palo']:
                            if jugador_camino ['puntos'] > 0:
                                jugador_camino ['puntos'] -= 1
                            print(f'{jugador_camino ["nombre"]} pierde 1 punto. Ahora tiene {jugador_camino ["puntos"]} puntos.')

                    posCamino += 1
                break

        for jugador in jugadores:
            if jugador['puntos'] == 10:
                print(f'{jugador["nombre"]} ha ganado el juego.')
        time.sleep(1)

