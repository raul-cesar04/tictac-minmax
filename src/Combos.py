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
    def GenerateCombos() -> list:
        combos = []
        for i in range(len(Combos.winCombos)):
            combos.append(Combos.ComboToBin(Combos.winCombos[i]))
        
        return combos
    
    def ComboToBin(mat: list)->int:
        st: str = "".join([str(e) for e in mat])
        n: int = int(st, 2)
        return n

