while True:  
    def main():
        gross_wage = float(input("Insira o Salário: $"))
        bonus =  float(input("insira o percentual de gratificação: "))/100
        income_tax = float(input("insira a alíquota do imposto: "))/100
        net_wage = gross_wage + bonus * gross_wage - income_tax * gross_wage
        print(f"\nSeu salario liquido é de: ${net_wage}\n")
    if  __name__ == "__main__":
        main()