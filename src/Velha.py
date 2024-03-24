from enum import Enum
class Jogadores(Enum):
    P1 = 1
    P2 = 2
    V  = 0

    def to_str(self) -> str:
        values = [
            "Velha",
            "Jogador 1",
            "Jogador 2"
        ]

        return values[self.value]

class Velha:
    tabuleiro = [[0 for _ in range(3)] for _ in range(3)]
    vez: Jogadores
    # Inicia tabuleiro zerado
    def Inicio(self):
        self.tabuleiro = [
            [Jogadores.V, Jogadores.V, Jogadores.V],
            [Jogadores.V, Jogadores.V, Jogadores.V],
            [Jogadores.V, Jogadores.V, Jogadores.V]
        ]
        
        self.vez = Jogadores.P1
        return

    # Recebe uma jogada de entrada
    def Jogada(self, jogada: tuple):
        # Verifica se a jogada é valida
        if(self.tabuleiro[ jogada[1] ] [jogada[0] ] != Jogadores.V): return

        # Atualiza a jogada
        self.tabuleiro[ jogada[1]] [jogada[0]] = self.vez

        # Alterna a vez dos jogadores
        self.vez = Jogadores.P1 if self.vez == Jogadores.P2 else Jogadores.P2
        return

    def __ChecaVencedor(self) -> Jogadores:
        pass
