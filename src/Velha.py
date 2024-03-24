from enum import Enum
class Jogadores(Enum):
    P1 = 1
    P2 = 2
    V  = 0

class Velha:
    tabuleiro = [[0 for _ in range(3)] for _ in range(3)]
    vez: Jogadores
    # Inicia tabuleiro zerado
    def Inicio(self):
        self.tabuleiro = [
            [Jogadores.V, Jogadores.P1, Jogadores.V],
            [Jogadores.P2, Jogadores.P2, Jogadores.V],
            [Jogadores.P1, Jogadores.P1, Jogadores.V]
        ]
        
        self.vez = Jogadores.P1
        return

    # Recebe uma jogada de entrada
    def Jogada(self):
        print("Agora é a vez do jogador "+str(self.vez))
        self.vez = Jogadores.P1 if self.vez == Jogadores.P2 else Jogadores.P2
        return

    def __ChecaVencedor(self) -> Jogadores:
        pass

    def __ValidaJogada(self) -> bool:
        pass
