#Faça uma sub-rotina que verifique se a matriz informada é simétrica ou não. Uma matriz só pode ser considerada simétrica se A[ i, j ] = A [ j, i ].

def verificar_simetria(matriz):
    if len(matriz) != len(matriz[0]):
        return False