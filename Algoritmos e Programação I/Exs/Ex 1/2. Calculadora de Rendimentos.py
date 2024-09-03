while True:
    def main():
        deposit = float(input("Insira o valor do depósito: $"))
        _yield = float(input("\nInsira a Taxa de rendimento anual: "))/100
        period = 12
        yielded = deposit * _yield / 12 * period
        amount = deposit * (_yield / 12 * period + 1)
        print(f"\nRendimentos após {period} meses: ${yielded}\nValor total após {period} meses: ${amount:.2f}\n")
    if __name__ == "__main__":
        main()
