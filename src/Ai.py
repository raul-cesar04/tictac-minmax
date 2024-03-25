from enum import Enum
import copy
import random

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

# ===================================================
#   Classe com os métodos referentes à decisões da IA
# ===================================================
class Ai:
    velha = None
    def __init__(self, velha) -> None:
        self.velha = velha
        self.velha.cpu = self
        pass
    # Computa o resultado da jogada. Retorna uma cópia do tabuleiro e realiza a jogada
    def __jogada(self, tabuleiro: list, pos: tuple, jogador: Jogadores)->list:
        jogada: list = copy.deepcopy(tabuleiro)
        jogada[pos[0]][pos[1]] = jogador

        return jogada

    # Retorna uma lista de todas as jogadas (posições) possiveis dada o estado atual do tabuleiro
    def __jogadas_possiveis(self, tabuleiro: list) ->list:
        jogadas: list = []

        for r in range(3):
            for c in range(3):
                if(tabuleiro[r][c] == Jogadores.V):
                    jogadas.append((r,c))

        return jogadas

    # Computa o score das jogadas
    # tabuleiro - matriz representando o tabuleiro
    # jogador_atual - quem é o jogador que está jogando
    # eu - quem é o jogador que quer ser beneficiado (?)
    def __minimax(self, tabuleiro: list, jogador_atual: Jogadores, eu: Jogadores, max_depth = 9)->int:
        oponente: Jogadores = Jogadores.P2 if eu == Jogadores.P1 else Jogadores.P1
        if(self.velha.ChecaVencedor(tabuleiro, eu) != None): return 1         # Vitoria
        if(self.velha.ChecaVencedor(tabuleiro, oponente) != None): return -1        # Derrota
        if(self.__is_tabuleiro_cheio(tabuleiro)): return 0 # Empate

        # if(max_depth == 0): return quit()#random.randrange(-999, 999) # Heuristica temporária


        jogadas: list = self.__jogadas_possiveis(tabuleiro)
        if(jogador_atual == eu): # MAX
            best_score: float = float("-inf")
            for jogada in jogadas:
                resultado = self.__jogada(tabuleiro, jogada, jogador_atual)
                score = self.__minimax(resultado, (Jogadores.P1 if jogador_atual == Jogadores.P2 else Jogadores.P2), eu, max_depth-1)
                
                if(score > best_score):
                    best_score = score
            return best_score
        else: # MIN
            best_score: float = float("inf")
            for jogada in jogadas:
                resultado = self.__jogada(tabuleiro, jogada, jogador_atual)
                score = self.__minimax(resultado, (Jogadores.P1 if jogador_atual == Jogadores.P2 else Jogadores.P2), eu, max_depth-1)
                
                if(score < best_score):
                    best_score = score
            return best_score

    # Dado o estado atual do tabuleiro e o jogador, retorne a melhor jogada
    # Tupla contendo a posição em que será feita a jogada
    def best_action(self, tabuleiro: list, jogador: Jogadores) -> tuple:
        jogadas: list = self.__jogadas_possiveis(tabuleiro)

        best_score: float = float("-inf")
        best_action: tuple = None
        # Para cada possivel jogada
        for jogada in jogadas:
            resultado: list = self.__jogada(tabuleiro, jogada, jogador)
            score = self.__minimax(resultado, Jogadores.P1 if jogador == Jogadores.P2 else Jogadores.P2, jogador)

            if(score > best_score):
                best_score = score
                best_action = jogada
        # quit()
        return best_action
    
    def __is_tabuleiro_cheio(self, tabuleiro: list)->bool:
        ret: bool = True

        for r in range(3):
            for c in range(3):
                if(tabuleiro[r][c] == Jogadores.V):
                    return False
        return ret


    def clean_print(self, tabuleiro: list):
        for r in range(3):
            for c in range(3):
                print(tabuleiro[r][c].value, end=" ")
            print("")
        print("")