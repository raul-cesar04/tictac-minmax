from Velha import Jogadores

# ===================================================
#   Classe com os métodos referentes à decisões da IA
# ===================================================
class Ai:

    # Computa o resultado da jogada. Retorna uma cópia do tabuleiro e realiza a jogada
    def __jogada(tabuleiro: list, pos: tuple, jogador: Jogadores)->list:
        pass

    # Retorna uma lista de todas as jogadas (posições) possiveis dada o estado atual do tabuleiro
    def __jogadas_possiveis(tabuleiro: list) ->list:
        pass

    # Computa o score das jogadas
    def __minimax(tabuleiro: list, jogador_atual: Jogadores, eu: Jogadores, max_depth = 9)->int:
        pass

    # Dado o estado atual do tabuleiro e o jogador, retorne a melhor jogada
    # Tupla contendo a posição em que será feita a jogada
    def best_action(tabuleiro: list, jogador: Jogadores) -> tuple:
        pass
    