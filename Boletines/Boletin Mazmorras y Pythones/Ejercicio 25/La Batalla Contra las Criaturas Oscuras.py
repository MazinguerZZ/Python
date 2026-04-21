def encuentro_monstruos(poder_monstruos, poder_heroe):
    for poder in poder_monstruos:
        if poder > poder_heroe:
            return 1
    return 0


print(encuentro_monstruos([5, 10, 7], 8))
print(encuentro_monstruos([2, 3, 1], 5))
print(encuentro_monstruos([10, 10, 10], 10))