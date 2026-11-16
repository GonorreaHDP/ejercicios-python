import random

# Inicializamos la lista vacía
notas = []

# Rellenamos la lista con 100 números aleatorios entre 0 y 10
while len(notas) < 100:
    nota = random.randint(0, 10)
    notas.append(nota)

# Mostramos cuántos ceros hay inicialmente
print("En mi lista tengo", notas.count(0), "ceros.")

# ==========================================
# OPTIMIZACIÓN DEL BORRADO DE CEROS
# ==========================================
# En lugar de usar un bucle while con .remove() (que es O(N^2)),
# utilizamos una comprensión de listas para crear una nueva lista
# conservando únicamente los elementos que NO sean iguales a 0.
# Esto reduce el coste computacional a O(N).
notas = [nota for nota in notas if nota != 0]

# Si necesitas modificar la misma lista "in situ" (manteniendo la misma referencia en memoria),
# puedes usar rebanado (slicing) en su lugar:
# notas[:] = [nota for nota in notas if nota != 0]

# Mostramos la longitud final de la lista y su contenido actualizado
print(len(notas), notas)