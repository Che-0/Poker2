import jugador as jg
import baraja
import apuesta

def main():
    print("Bienvenido al juego de cartas")
    num_jugadores = 3
    nombres =[]
    
    #num_jugadores = int(input("Ingrese el número de jugadores: "))
    #
    #for i in range(num_jugadores):
    #    nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
    #    
    #    # comprobar que el jugador ingrese un número válido para los fondos
    #    while True:            
    #        try:
    #            fondos = int(input(f"Ingrese los fondos iniciales para {nombre}: "))
    #            if fondos < 0:
    #                print("Los fondos no pueden ser negativos. Por favor, ingrese un número válido.")
    #            else:                   
    #                break
    #        except ValueError:
    #            print("Entrada no válida. Por favor, ingrese un número entero para los fondos.")
#
    #    jugadori = jugador.Jugador(nombre, fondos, [])
    #    nombres.append(jugador1)
    #    print(jugador1)

    #generar jugadores de prueba
    jugador1 = jg.Jugador("Alice", 100, [])
    jugador2 = jg.Jugador("Bob", 150, [])
    jugador3 = jg.Jugador("Charlie", 200, [])

    nombres.append(jugador1)
    nombres.append(jugador2)
    nombres.append(jugador3)
    

    
    print(f"""
Jugadores generados:
{jugador1}
{jugador2}
{jugador3}
          """)
    
    #bucle para juego
    
    contadorCiega=0
    ciegasChica =nombres[contadorCiega]
    ciegasChica.ciega = True
    print(f"{ciegasChica.nombre} es la ciega chica.")
    
    
    
    print("Iniciando ronda de apuestas...")
    apuestaAdmin = apuesta.Apuesta()
    for jugador in nombres:
        print(jugador)
        
        print("quieres apostar, igualar o retirarte? (1_apostar/2_igualar/3_retirarse)")
        accion = int(input("Ingrese el número de la acción que desea realizar: "))
        match accion:
            case 1:
                if jugador.ciega:
                    apuestaAdmin.rise(10, jugador)  # Ciega chica apuesta 10
                    
                else:
                    apuestaAdmin.rise(20, jugador)  # Apostar 20
                    
            case 2:
                apuestaAdmin.call(20, jugador)  # Igualar la apuesta de 20
            case 3:
                apuestaAdmin.fold()  # Retirarse de la mano
                jugador.estado = False  # Cambiar el estado del jugador a retirado
            case _:
                print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
    
    print("Creando baraja y barajando...")
    baraja1 = baraja.Baraja()
    baraja1.barajar()
    print("Baraja barajada. Repartiendo cartas a los jugadores...")
    
    #Aqui va la lógica para repartir cartas a los jugadores y manejar las apuestas
    
    for i in nombres:
        print(i)
    
#    apuestaAdmin = apuesta.Apuesta()
    
    
    
    for i in range(2):  # Repartir 2 cartas a cada jugador
        jugador1.cartas.append(baraja1.pull())
        jugador2.cartas.append(baraja1.pull())
        jugador3.cartas.append(baraja1.pull())
        
    print(f"""Jugadores después de repartir cartas:
{jugador1}
{jugador2}
{jugador3}
          """)
    print("Quemando la primera carta ...")
    baraja1.pull()  # Quemar la primera carta            
    
    #sacamos el flop
    print("flop: ")
    cartas_comunitarias = []
    for i in range(3):
        cartas_comunitarias.append(baraja1.pull())
    print(cartas_comunitarias)

    

if __name__ == "__main__":
    main()