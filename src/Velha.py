from Combos import Combos
from Ai import Ai, Jogadores

# ===========
#   Classe onde é definido o funcinamento do jogo da velha
class Velha:
    tabuleiro = [[0 for _ in range(3)] for _ in range(3)]
    vez: Jogadores
    jogadas: int
    cpu: Ai

    jogadas_vencedoras: list
    fim_jogo: bool
    vencedor: Jogadores

    # O Inicio de uma partida
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
        self.cpu = Ai(self)

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

        # Verifica se o jogo acabou
        self.vencedor = self.ChecaVencedor(self.tabuleiro, self.vez)

        self.fim_jogo = self.vencedor != None or self.jogadas == 0

        if(self.fim_jogo):
            return

        # Alterna a vez dos jogadores
        self.vez = Jogadores.P1 if self.vez == Jogadores.P2 else Jogadores.P2
        return

    # Verifica o fim de jogo
    def ChecaVencedor(self, tab: list, jogador: Jogadores) -> Jogadores:
        
        # Transforma o array 2D num array unidimensional 
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

    # Realizar jogada através da IA
    def Cpu(self)->tuple:
        act: tuple = self.cpu.best_action(self.tabuleiro, self.vez)
        return act
