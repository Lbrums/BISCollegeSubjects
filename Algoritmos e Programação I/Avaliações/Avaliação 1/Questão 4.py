# Faça um programa que leia a capacidade de um elevador e o peso de 5 pessoas.
# Ao final informe se o elevador está liberado para subir ou
# se excedeu a capacidade máxima.

capacidade_max = 450
pesos = [60.0, 75.0, 57.0, 90.0, 63.0]
peso_total = sum(pesos)

if peso_total > capacidade_max:
    print("Peso ultrapassa a capacidade máxima.")

else:
    print("Peso dentro da capacidade.")
