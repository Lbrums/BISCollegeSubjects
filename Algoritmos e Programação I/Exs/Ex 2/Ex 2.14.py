# A granja Frangotech possui um controle automatizado de cada frango da sua produção.
# No pé direito do frango há um anel com um chip de identificação;
# no pé esquerdo são dois anéis para indicar o tipo de alimento que ele deve consumir.
# Sabendo que o anel com chip custa R$4,00 e o anel de alimento custa R$3,50 cada,
# faça um algoritmo para calcular o gasto total da granja para marcar todos os seus frangos

frangos = int(input("Insira a quantidade de frangos: "))
chip_a = 3.5 * 2 * frangos
chip_i = 4 * frangos
chip_total = chip_a + chip_i

print(f"Você gastará R${chip_total:.2f} para comprar os chips.")
