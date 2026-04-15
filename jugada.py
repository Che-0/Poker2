#comparar las manos de los jugadores y determinar el ganador
class Jugada:
    def __init__(self, jugador, cartas_comunitarias):
        self.jugador = jugador
        self.cartas = cartas_comunitarias + jugador.cartas
    
    def evaluar_mano(self):
        # Aquí se implementaría la lógica para evaluar la mano del jugador
        # y determinar su valor en el juego de poker.
        pass
    
    def comparar_manos(self, otra_jugada):
        # Aquí se implementaría la lógica para comparar esta jugada con otra jugada
        # y determinar cuál es la mejor mano.
        pass
    
    def __str__(self):
        return f"{self.jugador.nombre} tiene las cartas: {', '.join(self.cartas)}"