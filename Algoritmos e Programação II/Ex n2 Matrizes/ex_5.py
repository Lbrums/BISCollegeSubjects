"""
Faça um algoritmo que lê uma matriz M2X2 que calcula e
mostra o resultado do determinante desta matriz.
"""


def det2x2(m2x2):
    return m2x2[0][0] * m2x2[1][1] - m2x2[1][0] * m2x2[0][1]
