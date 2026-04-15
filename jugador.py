class Jugador:
    def __init__(self, nombre,fondos,cartas, ciega=False, estado=True):
        self.nombre = nombre
        self.fondos = fondos
        self.cartas = cartas
        self.ciega = ciega
        self.estado = estado

    def sumar_fondos(self, fondos):
        self.fondos += fondos
        
    def restar_fondos(self, fondos):
        if fondos <= self.fondos:
            self.fondos -= fondos
        else:
            print("No tienes suficientes fondos para realizar esta acción.")

    def __str__(self):
        return f"{self.nombre} - Fondos: ${self.fondos} - Cartas: {self.cartas} - Ciega: {self.ciega} - Estado: {'Activo' if self.estado else 'Retirado'}"
    
if __name__ == "__main__":
    jugador1 = Jugador("Alice", 100, [])
    print(jugador1)