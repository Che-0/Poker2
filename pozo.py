class Pozo:
    def __init__(self):
        self.total = 0
        self.apuestas_ronda = []

    def agregar(self, cantidad: int, jugador) -> bool:
        if jugador.restar_fondos(cantidad):
            self.total += cantidad
            self.apuestas_ronda.append((jugador.nombre, cantidad))
            print(f"→ {jugador.nombre} pone ${cantidad} | Pozo: ${self.total}")
            return True
        return False

    def reset(self):
        self.total = 0
        self.apuestas_ronda.clear()

    def __str__(self):
        return f"Pozo actual: ${self.total}"