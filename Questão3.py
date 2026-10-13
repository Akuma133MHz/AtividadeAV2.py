def verificar_carga_horaria(horas):
    if horas >= 40:
        return "Carga completa"
    else:
        return "Carga incompleta"


horas = float(input("Digite as horas trabalhadas na semana: "))
print(verificar_carga_horaria(horas))
