while True:
    def main():
        def inches_to_feets():
            return measurement / 12
        
        def inches_to_yards():
            return measurement / 36
        
        def inches_to_miles():
            return measurement / 63360
        
        def feets_to_inches():
            return measurement * 12
      
        def feets_to_yards():
            return measurement / 3
        
        def feets_to_miles():
            return measurement / 5280
        
        def yards_to_feets():
            return measurement * 3
        
        def yards_to_miles():
            return measurement / 1760
        
        def yards_to_inches():
            return measurement * 36
        
        def miles_to_yards():
            return measurement * 1760
        
        def miles_to_feets():
            return measurement * 5280
        
        def miles_to_inches():
            return measurement * 63360

        print("Digite o numero correspondente da operação desejada:\n1. polegadas para pés\n2. polegadas para jardas\n3. polegadas para milhas\n4. pés para polegadas\n5. pés para jardas\n6. pés para milhas\n7. jardas para polegadas\n8. jardas para pés\n9. jardas para milhas\n10.milhas para polegadas\n11.milhas para pés\n12.milhas para jardas\n")
        operation = int(input("Operação: "))
        measurement = float(input("\nInsira a medida a ser convertida: "))
        print("")
        if operation == 1:
            print(f"{measurement} polegadas são {inches_to_feets():.4f} pés.\n")
        elif operation == 2:
            print(f"{measurement} polegadas são {inches_to_yards():.4f} jardas.\n")
        elif operation == 3:
            print(f"{measurement} polegadas são {inches_to_miles():.4f} milhas.\n")
        elif operation == 4:
            print(f"{measurement} pés são {feets_to_inches():.4f} polegadas.\n")
        elif operation == 5:
            print(f"{measurement} pés são {feets_to_yards():.4f} jardas.\n")
        elif operation == 6:
            print(f"{measurement} pés são {feets_to_miles():.4f} milhas.\n")
        elif operation == 7:
            print(f"{measurement} jardas são {yards_to_inches():.4f} polegadas.\n")
        elif operation == 8:
            print(f"{measurement} jardas são {yards_to_feets():.4f} pés.\n")
        elif operation == 9:
            print(f"{measurement} jardas são {yards_to_miles():.4f} milhas.\n")
        elif operation == 10:
            print(f"{measurement} milhas são {miles_to_inches():.4f} polegadas.\n")
        elif operation == 11:
            print(f"{measurement} milhas são {miles_to_feets():.4f} pés.\n")
        elif operation == 12:
            print(f"{measurement} milhas são {miles_to_yards():.4f} jardas.\n")
        else:
            print(f"Operação \"{operation}\" inválida\n")

    if __name__ == "__main__":
        main()

