def sumar(a: float, b: float) -> float:
    """
    Suma dos números reales (float).
    Retorna la suma formateada a dos decimales.
    """
    try:
        resultado = round(a + b, 2)
        return resultado
    except TypeError:
        print("Ambos valores deben ser números reales.")

def restar(a: float, b: float) -> float:
    """
    Resta dos números reales (float).
    Retorna la resta del primer número menos el segundo, formateada a dos decimales.
    """
    try:
        resultado = round(a - b, 2)
        return resultado
    except TypeError:
        print("Ambos valores deben ser números reales.")

def dividir(a: float, b: float) -> float:
    """
    Divide dos números reales (float).
    Retorna la división del primer número entre el segundo formateada a dos decimales.
    Maneja el caso de división por cero con una excepción.
    """
    try:
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
        resultado = round(a / b, 2)
        return resultado
    except TypeError:
        print("Ambos valores deben ser números reales.")

def multiplicar(a: float, b: float) -> float:
    """
    Multiplica dos números reales (float).
    Retorna el producto formateado a dos decimales.
    """
    try:
        resultado = round(a * b, 2)
        return resultado
    except TypeError:
        print("Ambos valores deben ser números reales.")

def sumar_n(*args: float) -> float:
    """
    Suma una cantidad variable de números reales (float).
    Retorna la suma total formateada a dos decimales.
    """
    if not args:
        print("Debe proporcionar al menos un número.")
    try:
        resultado = round(sum(args), 2)
        return resultado
    except TypeError:
        print("Todos los valores deben ser números reales.")

def promedio_n(*args: float) -> float:
    """
    Calcula el promedio de una cantidad variable de números reales (float).
    Retorna el promedio formateado a dos decimales.
    """
    if not args:
        print("Debe proporcionar al menos un número.")
    try:
        resultado = round(sum(args) / len(args), 2)
        return resultado
    except TypeError:
        print("Todos los valores deben ser números reales.")


def menu():
    while True:
        print("\nMenú de Opciones:")
        print("1. Sumar dos números")
        print("2. Restar dos números")
        print("3. Dividir dos números")
        print("4. Multiplicar dos números")
        print("5. Sumar varios números")
        print("6. Calcular promedio de varios números")
        print("7. Salir")

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == '7':
            print("Saliendo...")
            break

        if opcion in ['1', '2', '3', '4']:
            try:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Por favor, ingrese números válidos.")
                continue

            if opcion == '1':
                resultado = sumar(a, b)
            elif opcion == '2':
                resultado = restar(a, b)
            elif opcion == '3':
                resultado = dividir(a, b)
            elif opcion == '4':
                resultado = multiplicar(a, b)

            if resultado is not None:
                print(f"Resultado: {resultado}")

        elif opcion in ['5', '6']:
            try:
                entrada = input("Ingrese los números separados por espacio: ")
                numeros = entrada.split()
                numeros = [float(num) for num in numeros]  # Conversión sin map
            except ValueError:
                print("Por favor, ingrese números válidos.")
                continue

            if opcion == '5':
                resultado = sumar_n(*numeros)
            elif opcion == '6':
                resultado = promedio_n(*numeros)

            if resultado is not None:
                print(f"Resultado: {resultado}")

        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 7.")

# Ejecutar el menú
menu()