from enum import Enum
from Combos import Combos

# Enum Jogadores
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
    jogadas: int

    jogadas_vencedoras: list
    fim_jogo: bool
    vencedor: Jogadores

    def Inicio(self):
        # Inicia tabuleiro zerado
        self.tabuleiro = [
            [Jogadores.V, Jogadores.V, Jogadores.V],
            [Jogadores.V, Jogadores.V, Jogadores.V],
            [Jogadores.V, Jogadores.V, Jogadores.V]
        ]
        
        # Reinicia numero de jogadas para o fim
        self.jogadas = 9

        # Jogo começa com o Jogador 1
        self.vez = Jogadores.P1

        self.jogadas_vencedoras = Combos.GenerateCombos()

        self.fim_jogo = False
        self.vencedor = None
        return

    # Recebe uma jogada de entrada
    def Jogada(self, jogada: tuple):
        # Verifica se a jogada é valida
        if(self.tabuleiro[ jogada[1] ] [jogada[0] ] != Jogadores.V): return

        # Atualiza a jogada
        self.tabuleiro[ jogada[1]] [jogada[0]] = self.vez
        self.jogadas -= 1

        # Verifica se o jogo acabou
        self.vencedor = self.__ChecaVencedor()

        self.fim_jogo = self.vencedor != None or self.jogadas == 0

        if(self.fim_jogo):
            return

        # Alterna a vez dos jogadores
        self.vez = Jogadores.P1 if self.vez == Jogadores.P2 else Jogadores.P2
        return

    # Verifica o fim de jogo
    def __ChecaVencedor(self) -> Jogadores:
        jogador: Jogadores = self.vez

        # Transforma o array 2D numa matriz unidimensional (????)
        jogadas = [0]*9
        tab = self.tabuleiro

        for r in range(3):
            for c in range(3):
                cell = tab[r][c]
                if(cell == jogador):
                    jogadas[r*3+c] = 1
        pass

        jogada: int = Combos.ComboToBin(jogadas)
        for j in self.jogadas_vencedoras:
            if(jogada & j == j):
                return jogador
            

        return None

    def __PrintMat(self, mat):
        for r in range(3):
            for c in range(3):
                print(mat[r*3+c], end="")
            print("", end=" ")
        return
