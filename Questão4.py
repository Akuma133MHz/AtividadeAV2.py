def atualizar_saldo(saldo, valor, operacao):
    if operacao == "deposito":
        return saldo + valor
    elif operacao == "saque":
        if valor <= saldo:
            return saldo - valor
        else:
            print("Saldo insuficiente!")
            return saldo
    else:
        print("Operação inválida!")
        return saldo


saldo = float(input("Digite o saldo atual: "))
valor = float(input("Digite o valor da operação: "))
operacao = input("Digite deposito ou saque: ").lower()

novo_saldo = atualizar_saldo(saldo, valor, operacao)

print("Novo saldo: R$", novo_saldo)
