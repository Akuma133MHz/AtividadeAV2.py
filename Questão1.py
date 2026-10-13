try:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    resultado = n1 / n2
    print("Resultado da divisão:", resultado)

except ValueError:
    print("Entrada inválida! Digite apenas números.")

except ZeroDivisionError:
    print("Não é possível dividir por zero!")
