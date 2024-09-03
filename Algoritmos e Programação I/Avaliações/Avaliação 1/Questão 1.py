# Cada degrau de uma escada tem X de altura.
# Faça um programa que receba essa altura do degrau e
# a altura que o usúario deseja alcançar subindo a escada,
# Calcule e mostre quantos degraus ele deverá subir para atingir seu objetivo.
# Todas as medidas devem estar em metros.

degrau = float(input("Altura do degrau(em metros): "))
altura_objetivo = float(input("Altura que deseja alcançar(em metros):"))

degraus_total = altura_objetivo / degrau

print(f"Para alcançar a altura desejada sera necessario subir {degraus_total} degraus.")
