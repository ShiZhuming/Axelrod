import axelrod as axl

C, D = axl.Action.C, axl.Action.D
# payoff_matrix = {
#     (C, C): (1, 2),
#     (C, D): (-1, 3),
#     (D, C): (2, -1),
#     (D, D): (0, 0)
# }

payoff_matrix = {
    (C, C): (1, 2),
    (C, D): (-2, 3),
    (D, C): (3, -1),
    (D, D): (0, 0)
}

def set_score(choices):
    scores = list(map(lambda x: payoff_matrix[x], choices))
    score1 = sum([x[0] for x in scores])
    score2 = sum([x[1] for x in scores])
    return (score1, score2)


def simu():
    players = [axl.Cooperator(), axl.Defector(), axl.TitForTat(),
               axl.Random(), axl.WinStayLoseShift()]
    length = len(players)
    matrix = [[0]*length for i in range(length)]
    turns = 10

    for i in range(length):
        for j in range(length):
            match = axl.Match((players[i], players[j]), turns=turns)
            match.play()
            matrix[i][j] = list(
                map(lambda x: x/turns, set_score(match.result)))

    gen_table(matrix, players)
    gen_rank(matrix, players)


def gen_table(matrix, players):
    table = r"\begin{tabular}{"
    for i in range(len(players)+1):
        table = table + "|c"
    table = table + "|}"
    table = table + "\\\\\n\hline\n"

    table = table + r"\diagbox{行玩家}{列玩家}"
    for p in players:
        table = table + "&" + p.name
    table = table + "\\\\\n\hline\n"

    for i in range(len(players)):
        row = matrix[i]
        table = table + players[i].name
        for cell in row:
            table = table + "&"+str(tuple(cell))
        table = table + "\\\\"+"\n" + "\hline\n"

    table = table + r"\end{tabular}"

    print(table)


def gen_rank(matrix, players):
    length = len(players)
    for i in range(length):
        row_score = 0
        col_score = 0
        for j in range(length):
            if i != j:
                row_score += matrix[i][j][0]
        for k in range(length):
            if i != k:
                col_score += matrix[k][i][1]
        players[i].row_score = row_score/(length-1)
        players[i].col_score = col_score/(length-1)
        players[i].ave_score = (players[i].row_score + players[i].col_score)/2

    row_rank = sorted(players, key=lambda x: x.row_score, reverse=True)
    col_rank = sorted(players, key=lambda x: x.col_score, reverse=True)
    ave_rank = sorted(players, key=lambda x: x.ave_score, reverse=True)

    table = ""
    for i in range(length):
        table = table + row_rank[i].name + "&" + str(row_rank[i].row_score)[:4] + \
            "&" + col_rank[i].name + "&" + str(col_rank[i].col_score)[:4] + \
            "&" + ave_rank[i].name + "&" + str(ave_rank[i].ave_score)[:4]
        table = table + "\\\\"+"\n" + "\hline\n"

    print(table)


if __name__ == "__main__":
    simu()
