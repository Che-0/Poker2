import random

class Baraja:
    def __init__(self):
        self.cartas = [f"{valor} de {palo}" for valor in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
                        for palo in ['Corazones', 'Diamantes', 'Tréboles', 'Picas']]
    def barajar(self):
        random.shuffle(self.cartas)
    
    def pull(self):
        if self.cartas:
            return self.cartas.pop()
        else:
            return "No hay más cartas en la baraja."
    
    def ver_cartas(self):
        return self.cartas
    
if __name__ == "__main__":
    cartas = Baraja()
    cartas.barajar()
    a = cartas.pull()
    print(a)