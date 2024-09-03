# Faça um programa que leia três valores inteiros diferentes fornecidos pelo User
# e exiba o valor intermediário entre eles.

n = []
while len(n) < 3:
    x = int(input("Insira um número: "))

    if x not in n:
        n.append(x)
    else:
        while x in n:
            print(f"{x} ja foi inserido.")
            x = int(input("Insira um número diferente: "))
        n.append(x)

n.sort()

print(n[1])
