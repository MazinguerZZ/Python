def uefa_euro_2016(teams, scores):
    if scores[0] > scores[1]:
        ganador = teams[0]
        return f"At match {teams[0]} - {teams[1]}, {ganador} won!"
    elif scores[1] > scores[0]:
        ganador2 = teams[1]
        return f"At match {teams[0]} - {teams[1]}, {ganador2} won!"
    elif scores[0] == scores[1]:
        return f"At match {teams[0]} - {teams[1]}, teams played draw."

print(uefa_euro_2016(['Germany', 'Ukraine'], [2, 0]))
print(uefa_euro_2016(['Belgium', 'Italy'], [0, 2]))
print(uefa_euro_2016(['Portugal', 'Iceland'], [1, 1]))