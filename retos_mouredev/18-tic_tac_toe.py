def tic_tac_toe(table):
    win_combs = {
        "r0": ((0,0), (0,1), (0,2)),
        "r1": ((1,0), (1,1), (1,2)),
        "r2": ((2,0), (2,1), (2,2)),
        "c0": ((0,0), (1,0), (2,0)),
        "c1": ((0,1), (1,1), (2,1)),
        "c2": ((0,2), (1,2), (2,2)),
        "d0": ((0,0), (1,1), (2,2)),
        "d1": ((0,2), (1,1), (2,0))
    }
    
    # Check number of rows and columns
    if len(table) != 3:
        return "Null"
    for row in table:
        if len(row) != 3:
            return "Null"
            
    # Check number of Xs and Os
    x = []
    o = []
    for row in range(3):
        for pos in range(3):
            if table[row][pos] == "X":
                x.append((row,pos)) 
            elif table[row][pos] == "O":
                o.append((row,pos))
            elif table[row][pos] != "":
                return "Null"
    if len(x) < 3 and len(o) < 3:
        return "Null"
    if abs(len(x) - len(o)) > 1:
        return "Null"
        
    # Check who win
    x_win = False
    o_win = False
    win_combs_keys = tuple(win_combs.keys())
    for key in win_combs_keys:
        x_result = all(comb in x for comb in win_combs[key])
        o_result = all(comb in o for comb in win_combs[key])
        if (x_result): x_win = True
        if (o_result): o_win = True
    if x_win and o_win: return "Null"
    if not x_win and not o_win: return "Draw"
    if x_win: return "X"
    if o_win: return "O"

    
table1 = (
    ("X", "O", "O"),
    ("X", "O", "O"),
    ("O", "X", "X")
)

table2 = (
    ("", "O", "X"),
    ("", "O", "X"),
    ("", "",  "X")
)

table3 = (
    ("X", "O", "X"),
    ("X", "O", "O"),
    ("O", "X", "X")
)

table4 = (
    ("X", "",  "X"),
    ("O", "Y", "O"),
    ("",  "",  "X")
)

print(tic_tac_toe(table1))
print(tic_tac_toe(table2))
print(tic_tac_toe(table3))
print(tic_tac_toe(table4))
