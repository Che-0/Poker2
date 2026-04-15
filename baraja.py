import random
from carta import Carta

class Baraja:
    def __init__(self):
        self.cartas_originales = [
            Carta(valor, palo)
            for valor in ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
            for palo in Carta.PALOS
        ]
        self.reset()

    def reset(self):
        self.cartas = self.cartas_originales[:]
        self.barajar()

    def barajar(self):
        random.shuffle(self.cartas)

    def repartir(self):
        if not self.cartas:
            raise ValueError("No hay más cartas en la baraja.")
        return self.cartas.pop()

    def cartas_restantes(self):
        return len(self.cartas)

    def __str__(self):
        return f"Baraja ({self.cartas_restantes()} cartas restantes)"