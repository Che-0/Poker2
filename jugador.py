from typing import List
from carta import Carta

class Jugador:
    def __init__(self, nombre: str, fondos: int):
        self.nombre = nombre.strip()
        self.fondos = max(0, int(fondos)) # Asegurarse de que los fondos sean un entero no negativo
        self.cartas: List[Carta] = []
        self.ciega = False
        self.estado = True   # True = activo en la mano

    def sumar_fondos(self, cantidad: int):
        if cantidad > 0:
            self.fondos += cantidad

    def restar_fondos(self, cantidad: int) -> bool:
        if cantidad <= 0:
            return False
        if cantidad <= self.fondos:
            self.fondos -= cantidad
            return True
        print(f"{self.nombre} no tiene suficientes fondos.")
        return False

    def __str__(self):
        estado = "Activo" if self.estado else "Retirado"
        ciega = " (Ciega)" if self.ciega else ""
        cartas_str = " ".join(str(c) for c in self.cartas) if self.cartas else "Sin cartas"
        return f"{self.nombre}{ciega} | Fondos: ${self.fondos:,} | Cartas: {cartas_str} | {estado}"