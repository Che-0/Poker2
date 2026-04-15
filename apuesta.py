class Apuesta:
    total = 0
        
    def rise(self, cantidad, jugador):
        if cantidad <= jugador.fondos:
            jugador.restar_fondos(cantidad)
            Apuesta.total += cantidad
            print(f"{jugador.nombre} ha apostado ${cantidad}. Total en el pozo: ${Apuesta.total}")
        else:
            print("No tienes suficientes fondos para realizar esta apuesta.")
    
    def fold(self):
        print(f"{self.jugador.nombre} se ha retirado de la mano.")
 
    def call(self, cantidad, jugador):
        if cantidad <= jugador.fondos:
            jugador.restar_fondos(cantidad)
            Apuesta.total += cantidad
            print(f"{jugador.nombre} ha igualado la apuesta con ${cantidad}. Total en el pozo: ${Apuesta.total}")
        else:
            print("No tienes suficientes fondos para igualar esta apuesta.")
    def retirar():
        return Apuesta.total       
    
    
    
    
    def __str__(self):
        return f"{self.jugador.nombre} ha apostado ${self.cantidad}. Total en el pozo: ${Apuesta.total}"