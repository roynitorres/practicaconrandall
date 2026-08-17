estaturas = [2.34, 3.24, 2.01, 1.30, 0.12]

suma = 0

for estatura in estaturas:
    suma = suma + estatura

media = suma / len(estaturas)

mayores = 0
menores = 0

for estatura in estaturas:
    if estatura > media:
        mayores = mayores + 1
    elif estatura < media:
        menores = menores + 1

print("Estaturas:", estaturas)
print("Media de las estaturas:", media)
print("Cantidad de estudiantes más altos que la media:", mayores)
print("Cantidad de estudiantes más bajos que la media:", menores)