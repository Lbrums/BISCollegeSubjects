def main():
    saldo = 0
    def deposito():
        global saldo
        quantia = float(input("Quanto você deseja depositar?\n"))
        saldo += quantia
        return "$" + saldo
    def saque():
        global saldo, quantia
        quantia = float(input("Quanto você deseja sacar?\n"))
        saldo -= quantia
        return "$" + saldo
if __name__ == "__main__":
    main()