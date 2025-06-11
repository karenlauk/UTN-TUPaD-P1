#FUNCIONES PRÁCTICO
#EJERCIOS:
# 1)

def imprimir_hola_mundo():
    print("Hola mundo!");
imprimir_hola_mundo();

# 2)
def saludar_usuario(nombre):
    return f"Hola {nombre}!";
nombre = input("Ingrese su nombre: ");
print(saludar_usuario(nombre));

# 3)
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}");
nombre = input("Nombre: ");
apellido = input("Apellido: ");
edad = input("Edad: ");
residencia = input("Residencia: ");
informacion_personal(nombre, apellido, edad, residencia);

# 4)
import math
def calcular_area_circulo(radio):
    return math.pi * radio ** 2;

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio;
radio = float(input("Ingrese el radio del círculo: "));

print(f"Área: {calcular_area_circulo(radio):.2f}");
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}");

# 5)
def segundos_a_horas(segundos):
    return segundos / 3600;
segundos = int(input("Ingrese los segundos: "));
print(f"Horas: {segundos_a_horas(segundos):.2f}");

# 6)
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}");
numero = int(input("Ingrese un número: "));
tabla_multiplicar(numero);

# 7)
def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b);
a = float(input("Ingrese el primer número: "));
b = float(input("Ingrese el segundo número: "));

suma, resta, multiplicacion, division = operaciones_basicas(a, b);
print(f"Suma: {suma}");
print(f"Resta: {resta}");
print(f"Multiplicación: {multiplicacion}");
print(f"División: {division}");

# 8)
def calcular_imc(peso, altura):
    return peso / (altura ** 2);
peso = float(input("Ingrese su peso en kg: "));
altura = float(input("Ingrese su altura en metros: "));
print(f"Su IMC es: {calcular_imc(peso, altura):.2f}");

# 9)
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32;
celsius = float(input("Ingrese temperatura en Celsius: "));
print(f"Temperatura en Fahrenheit: {celsius_a_fahrenheit(celsius):.2f}");

# 10)
def calcular_promedio(a, b, c):
    return (a + b + c) / 3;
a = float(input("Primer número: "));
b = float(input("Segundo número: "));
c = float(input("Tercer número: "));
print(f"Promedio: {calcular_promedio(a, b, c):.2f}");
