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
        for combo in Combos.winCombos:
            combos.append(Combos.ComboToBin(combo))
        
        return combos
    
    def ComboToBin(mat: list)->int:
        st: str = "".join([str(e) for e in mat])
        n: int = int(st, 2)
        return n

