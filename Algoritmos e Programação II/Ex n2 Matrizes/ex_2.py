"""
Faça um algoritmo que lê uma matriz M10x10. 
Troque a seguir os valores contidos na linha de índice 2 com os da linha de índice 8 e
também troque os valores da linha de índice 5 com os da coluna de índice 9. 
No final mostre a matriz.
"""

m10x10 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
]

m10x10[2], m10x10[8] = m10x10[8], m10x10[2]

for i in range(10):
    m10x10[5][i], m10x10[i][9] = m10x10[i][9], m10x10[5][i]

for i in m10x10:
    print(i)
