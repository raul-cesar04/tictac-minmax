from Combos import Combos
from Ai import Ai, Jogadores

class Velha:
    tabuleiro = [[0 for _ in range(3)] for _ in range(3)]
    vez: Jogadores
    jogadas: int
    cpu: Ai

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
        if(self.tabuleiro[ jogada[0] ] [jogada[1] ] != Jogadores.V): return

        # Atualiza a jogada
        self.tabuleiro[ jogada[0]] [jogada[1]] = self.vez
        self.jogadas -= 1
        self.cpu = Ai(self)

        # Verifica se o jogo acabou
        self.vencedor = self.ChecaVencedor(self.tabuleiro)

        self.fim_jogo = self.vencedor != None or self.jogadas == 0

        if(self.fim_jogo):
            return

        # Alterna a vez dos jogadores
        self.vez = Jogadores.P1 if self.vez == Jogadores.P2 else Jogadores.P2
        return

    # Verifica o fim de jogo
    def ChecaVencedor(self, tab: list) -> Jogadores:
        jogador: Jogadores = self.vez

        # Transforma o array 2D numa matriz unidimensional (????)
        jogadas = [0]*9

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

    def Cpu(self)->tuple:
        act: tuple = self.cpu.best_action(self.tabuleiro, self.vez)
        print(act)
        return act
    def __PrintMat(self, mat):
        for r in range(3):
            for c in range(3):
                print(mat[r*3+c], end="")
            print("", end=" ")
        return
