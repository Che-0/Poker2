class Carta:
    
    VALORES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
               '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    
    PALOS = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    SIMBOLOS = {'Corazones': '♥', 'Diamantes': '♦', 'Tréboles': '♣', 'Picas': '♠'}

    def __init__(self, valor: str, palo: str):
        self.valor_str = valor
        self.palo = palo
        self.valor = self.VALORES[valor]

    def __str__(self):
        return f"{self.valor_str}{self.SIMBOLOS[self.palo]}"

    def __repr__(self):
        return self.__str__()