# Definição dos Combos que resultam em vitória
class Combos:
    winCombos = [
        [
            1, 1, 1,
            0, 0, 0,
            0, 0, 0
        ],
        [
            0, 0, 0,
            1, 1, 1,
            0, 0, 0
        ],
        [
            0, 0, 0,
            0, 0, 0,
            1, 1, 1
        ],

        [
            1, 0, 0,
            1, 0, 0,
            1, 0, 0
        ],

        [
            0, 1, 0,
            0, 1, 0,
            0, 1, 0
        ],

        [
            0, 0, 1, 
            0, 0, 1, 
            0, 0, 1,
        ],

        [
            1, 0, 0, 
            0, 1, 0, 
            0, 0, 1,
        ],
    
        
        [
            0, 0, 1, 
            0, 1, 0, 
            1, 0, 0,
        ],
    ]
    # Gera uma lista com todos os combos que resultam em vitória convertidos em um número
    def GenerateCombos() -> list:
        combos = []
        for combo in Combos.winCombos:
            combos.append(Combos.ComboToBin(combo))
        
        return combos
    
    # Converte a matriz que representa a jogada em uma string de numero binario e retorna o numero equivalente
    def ComboToBin(mat: list)->int:
        st: str = "".join([str(e) for e in mat])
        n: int = int(st, 2)
        return n

