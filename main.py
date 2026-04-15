from jugador import Jugador
from baraja import Baraja
from pozo import Pozo
from carta import Carta
from collections import Counter

# ====================== EVALUACIÓN DE MANOS ======================
def evaluar_mano(cartas_jugador, cartas_comunitarias):
    todas = cartas_jugador + cartas_comunitarias
    todas_sorted = sorted(todas, key=lambda c: c.valor, reverse=True)
    valores = [c.valor for c in todas_sorted]
    palos = [c.palo for c in todas_sorted]

    conteo_valores = Counter(valores)
    conteo_palos = Counter(palos)

    es_color = max(conteo_palos.values()) >= 5
    es_escalera = False
    for i in range(len(valores) - 4):
        if valores[i] - valores[i + 4] == 4:
            es_escalera = True
            break
    if set([14, 5, 4, 3, 2]).issubset(set(valores)):
        es_escalera = True

    if es_color and es_escalera:
        return 9, "Escalera de color"
    if 4 in conteo_valores.values():
        return 8, "Poker"
    if sorted(conteo_valores.values(), reverse=True)[:2] == [3, 2]:
        return 7, "Full House"
    if es_color:
        return 6, "Color"
    if es_escalera:
        return 5, "Escalera"
    if 3 in conteo_valores.values():
        return 4, "Trío"
    if sorted(conteo_valores.values(), reverse=True)[:2] == [2, 2]:
        return 3, "Dos pares"
    if 2 in conteo_valores.values():
        return 2, "Pareja"
    return 1, "Carta alta"


def determinar_ganador(jugadores, cartas_comunitarias):
    candidatos = []
    for j in jugadores:
        if j.estado and len(j.cartas) == 2:
            rank, nombre = evaluar_mano(j.cartas, cartas_comunitarias)
            candidatos.append((rank, nombre, j))

    if not candidatos:
        return None, "Sin jugadores"

    candidatos.sort(key=lambda x: x[0], reverse=True)
    max_rank = candidatos[0][0]
    ganadores = [c for c in candidatos if c[0] == max_rank]

    if len(ganadores) == 1:
        return ganadores[0][2], ganadores[0][1]
    else:
        return ganadores[0][2], f"{ganadores[0][1]} (empate)"


# ====================== RONDA DE APUESTAS (VERSIÓN CORREGIDA) ======================
def ronda_apuestas(jugadores, pozo, cartas_comunitarias, nombre_ronda="Preflop", apuesta_actual=0):
    print(f"\n--- Ronda de {nombre_ronda} ---")
    
    apuesta_a_igualar = apuesta_actual if nombre_ronda != "Preflop" else 20
    print(f"Pozo actual: ${pozo.total} | Apuesta a igualar: ${apuesta_a_igualar}\n")

    for jugador in jugadores:
        # Saltar jugadores retirados o que ya están All-in (fondos = 0)
        if not jugador.estado or jugador.fondos <= 0:
            continue

        print(f"Turno de → {jugador.nombre} | Fondos: ${jugador.fondos}")
        print(f"Cartas: {' '.join(map(str, jugador.cartas))}")
        if cartas_comunitarias:
            print(f"Comunitarias: {' '.join(map(str, cartas_comunitarias))}")

        while True:
            puede_igualar = jugador.fondos >= apuesta_a_igualar
            puede_subir = jugador.fondos > apuesta_a_igualar

            print("\nOpciones disponibles:")
            print("1. Fold (Retirarse)")

            if apuesta_a_igualar == 0 or puede_igualar:
                print("2. Check / Call")
            else:
                print(f"2. All-in (${jugador.fondos})")

            if puede_subir:
                min_raise = apuesta_a_igualar + 20
                print(f"3. Raise - Mínimo ${min_raise}")

            try:
                opcion = int(input("\nElige una opción: "))
            except ValueError:
                print("Ingresa un número válido.")
                continue

            # 1. Fold
            if opcion == 1:
                jugador.estado = False
                print(f"{jugador.nombre} se retiró (Fold).")
                break

            # 2. Call / Check / All-in
            elif opcion == 2:
                if apuesta_a_igualar == 0:   # Check
                    print(f"{jugador.nombre} hace Check.")
                    break
                
                # Pagar lo que se pueda (All-in si no alcanza)
                cantidad_a_pagar = min(apuesta_a_igualar, jugador.fondos)
                if pozo.agregar(cantidad_a_pagar, jugador):
                    if cantidad_a_pagar < apuesta_a_igualar:
                        print(f"{jugador.nombre} hace All-in con ${cantidad_a_pagar}.")
                    else:
                        print(f"{jugador.nombre} iguala con ${cantidad_a_pagar}.")
                    break
                else:
                    print("Error al agregar al pozo.")
                    continue

            # 3. Raise
            elif opcion == 3 and puede_subir:
                min_raise = apuesta_a_igualar + 20
                while True:
                    try:
                        total_apuesta = int(input(f"¿Cuánto quieres apostar en total? (mínimo ${min_raise}): "))
                        
                        if total_apuesta < min_raise:
                            print(f"Mínimo para subir es ${min_raise}.")
                            continue
                        if total_apuesta > jugador.fondos:
                            print(f"No tienes fondos suficientes. Máximo ${jugador.fondos}")
                            continue

                        if pozo.agregar(total_apuesta, jugador):
                            apuesta_a_igualar = total_apuesta
                            print(f"{jugador.nombre} sube la apuesta a ${total_apuesta}.")
                            break
                        else:
                            print("No se pudo realizar la subida.")
                            continue
                            
                    except ValueError:
                        print("Ingresa un número válido.")
                break

            else:
                print("Opción no válida o no disponible.")

    return apuesta_a_igualar


# ====================== MAIN ======================
def main():
    print("=== Poker Texas Hold'em - Con Apuestas Interactivas ===\n")

    jugadores = [
        Jugador("Alice", 1000),
        Jugador("Bob", 1500),
        Jugador("Charlie", 800)
    ]

    pozo = Pozo()
    baraja = Baraja()
    dealer_idx = 0

    print("Jugadores en la mesa:")
    for j in jugadores:
        print("  " + str(j))

    # === Nueva Mano ===
    print(f"\n--- Nueva Mano (Dealer: {jugadores[dealer_idx].nombre}) ---")

    pozo.reset()
    baraja.reset()
    for j in jugadores:
        j.cartas.clear()
        j.estado = True
        j.ciega = False

    # Ciegas
    ciega_chica_idx = (dealer_idx + 1) % len(jugadores)
    ciega_grande_idx = (dealer_idx + 2) % len(jugadores)

    ciega_chica = jugadores[ciega_chica_idx]
    ciega_grande = jugadores[ciega_grande_idx]

    ciega_chica.ciega = True
    ciega_grande.ciega = True

    print(f"Ciega chica → {ciega_chica.nombre} pone $10")
    pozo.agregar(10, ciega_chica)

    print(f"Ciega grande → {ciega_grande.nombre} pone $20")
    pozo.agregar(20, ciega_grande)

    # Repartir cartas privadas
    for _ in range(2):
        for j in jugadores:
            if j.estado:
                j.cartas.append(baraja.repartir())

    print("\nCartas repartidas:")
    for j in jugadores:
        print(f"  {j.nombre}: {' '.join(map(str, j.cartas))}")

    # Rondas de apuestas
    ultima_apuesta = 20   # La ciega grande marca la apuesta inicial

    ultima_apuesta = ronda_apuestas(jugadores, pozo, [], "Preflop", ultima_apuesta)

    # Flop
    baraja.repartir()  # quemar
    flop = [baraja.repartir() for _ in range(3)]
    print(f"\nFlop → {' '.join(map(str, flop))}")
    ultima_apuesta = ronda_apuestas(jugadores, pozo, flop, "Flop", ultima_apuesta)

    # Turn
    baraja.repartir()  # quemar
    turn = baraja.repartir()
    print(f"\nTurn → {turn}")
    ultima_apuesta = ronda_apuestas(jugadores, pozo, flop + [turn], "Turn", ultima_apuesta)

    # River
    baraja.repartir()  # quemar
    river = baraja.repartir()
    print(f"\nRiver → {river}")
    ultima_apuesta = ronda_apuestas(jugadores, pozo, flop + [turn, river], "River", ultima_apuesta)

    # Resultado final
    print("\n=== Fin de la mano ===")
    cartas_comunitarias = flop + [turn, river]
    
    ganador, mano_nombre = determinar_ganador(jugadores, cartas_comunitarias)

    if ganador:
        print(f"¡GANADOR: {ganador.nombre} con {mano_nombre}!")
        print(f"Pozo ganado: ${pozo.total}")
        ganador.sumar_fondos(pozo.total)
        print(f"{ganador.nombre} ahora tiene ${ganador.fondos:,}")
    else:
        print("No hay ganador.")

    print("\nEstado final de los jugadores:")
    for j in jugadores:
        print(j)


if __name__ == "__main__":
    main()