
# Práctico de Estructuras de datos complejas

# 1. Añadir frutas al diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2. Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3. Lista con nombres de frutas
solo_frutas = list(precios_frutas.keys())
print("Frutas:", solo_frutas)

# 4. Agenda telefónica
agenda = {}
for _ in range(5):
    nombre = input("Ingresá el nombre del contacto: ")
    numero = input("Ingresá el número telefónico: ")
    agenda[nombre] = numero

consulta = input("¿De quién querés saber el número?: ")
if consulta in agenda:
    print(f"Número de {consulta}: {agenda[consulta]}")
else:
    print("Contacto no encontrado.")

# 5. Palabras únicas y frecuencia
frase = input("Ingresá una frase: ").lower()
palabras = frase.split()

palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

frecuencia = {}
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
print("Frecuencia de palabras:", frecuencia)

# 6. Promedio de alumnos
alumnos = {}
for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Nota {i+1} de {nombre}: ")) for i in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: promedio = {promedio:.2f}")

# 7. Sets de estudiantes
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# 8. Stock de productos
stock = {
    'Arroz': 10,
    'Fideos': 20
}
producto = input("Producto a consultar: ")

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto no encontrado. ¿Cuántas unidades tiene?: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)

# 9. Agenda con tuplas como claves
agenda_eventos = {
    ('lunes', '10:00'): 'Reunión de equipo',
    ('martes', '14:00'): 'Clase de inglés'
}
dia = input("Día a consultar: ").lower()
hora = input("Hora a consultar: ")

evento = agenda_eventos.get((dia, hora))
if evento:
    print(f"Actividad: {evento}")
else:
    print("No hay actividad programada en ese horario.")

# 10. Invertir diccionario países-capitales
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Francia': 'París',
    'Japón': 'Tokio'
}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Diccionario invertido:", capitales_paises)
