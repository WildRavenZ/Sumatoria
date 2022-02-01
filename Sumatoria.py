while True:
    print("Ingresa una opción: ")
    op = input("1 - Sumatoria de cuadrados\n2 - Sumatoria de cubos\n")
    while op != str(1) and op != str(2):
        print("Por favor, ingresa una opción válida")
        op = input("1 - Sumatoria de cuadrados\n2 - Sumatoria de cubos\n")
    else:
        n = input("Ingresa el valor de n: ")
        while n.isdigit() == False or int(n) == 0:
            print("n debe ser un número natural")
            n = input("Ingresa el valor de n: ")
        else:
            if(op == str(1)):
                print("\n-----------------------------------")
                print("SUMATORIA DE CUADRADOS (x²)")
                print("-----------------------------------")
                print("Mediante sumatoria: ")
                print("-----------------------------------")
                sumatoria = 0
                for i in range(1, int(n) + 1):
                    print(str(i) + "² = " + str(i * i)) 
                    sumatoria = sumatoria + (i * i)
                print("El resultado de la sumatoria es:", sumatoria, "\n")
                print("-----------------------------------")
                print("Mediante formula: ")
                print("-----------------------------------")
                formula = int((int(n) * (int(n) + 1) * (2 * int(n) + 1)) / 6)
                print(" n(n + 1)(2n + 1)     " + n + "(" + n + " + 1)(2(" + n + ") + 1)")
                print("------------------ = -------------------- =", formula)
                print("         6                     6       \n")
            if(op == str(2)):
                print("\n-----------------------------------")
                print("SUMATORIA DE CUBOS (x³)")
                print("-----------------------------------")
                print("Mediante sumatoria: ")
                print("-----------------------------------")
                sumatoria = 0
                for i in range(1, int(n) + 1):
                    print(str(i) + "³ = " + str((i * i) * i)) 
                    sumatoria = sumatoria + (i * i) * i
                print("El resultado de la sumatoria es:", sumatoria, "\n")
                print("-----------------------------------")
                print("Mediante formula: ")
                print("-----------------------------------")
                formula = int((int(n) * int(n) * (int(n) + 1) * (int(n) + 1)) / 4)
                print(" n²(n + 1)²     " + n + "²(" + n + " + 1)²")
                print("------------ = ------------ =", formula)
                print("      4              4       ")
