def filtrar_aprovados(notas):
    return [nota for nota in notas if nota >= 7]


notas = [5, 7, 8, 4, 10, 6, 9]
aprovados = filtrar_aprovados(notas)

print("Notas dos aprovados:", aprovados)
