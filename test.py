import random

solve = [['R', 'R\'', 'R2', 'R2\''],
         ['L', 'L\'', 'L2', 'L2\''],
         ['U', 'U\'', 'U2', 'U2\''],
         ['B', 'B\'', 'B2', 'B2\''],
         ['F', 'F\'', 'F2', 'F2\''],
         ['D', 'D\'', 'D2', 'D2\'']
         ]


def solving(solve: list) -> str:
    result = ''
    xx = -1
    flag = True
    for i in range(20):
        while flag:
            x = random.randint(0, 5)
            if xx != x:
                xx = x
                flag = False
        y = random.randint(0, 3)
        result += str(solve[x][y]) + ' '
        flag = True
    return result


print(solving(solve))
