from enum import Enum

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
        return

    # Recebe uma jogada de entrada
    def Jogada(self, jogada: tuple):
        # Verifica se a jogada é valida
        if(self.tabuleiro[ jogada[1] ] [jogada[0] ] != Jogadores.V): return

        # Atualiza a jogada
        self.tabuleiro[ jogada[1]] [jogada[0]] = self.vez
        self.jogadas -= 1

        # Verifica se o jogo acabou
        game_over = self.__ChecaVencedor() != None or self.jogadas == 0

        # Alterna a vez dos jogadores
        self.vez = Jogadores.P1 if self.vez == Jogadores.P2 else Jogadores.P2
        return

    # Verifica o fim de jogo
    def __ChecaVencedor(self) -> Jogadores:
        pass
