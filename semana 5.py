def calcular_consumo_total(consumo_diario, numero_dias):
    consumo_total = consumo_diario * numero_dias
    return consumo_total


def es_consumo_saludable(consumo_total, limite_recomendado):
    consumo_saludable = consumo_total <= limite_recomendado
    return consumo_saludable


def main():
    nombre_persona = input("Ingrese su nombre: ")
    consumo_diario = float(input("Ingrese su consumo diario de agua en litros: "))
    numero_dias = int(input("Ingrese el número de días registrados: "))
    limite_recomendado = float(input("Ingrese el límite recomendado de consumo semanal (litros): "))

    consumo_total = calcular_consumo_total(consumo_diario, numero_dias)
    consumo_saludable = es_consumo_saludable(consumo_total, limite_recomendado)

    print("\n--- Reporte de Consumo de Agua ---")
    print(f"Nombre: {nombre_persona}")
    print(f"Consumo total: {consumo_total:.2f} litros")

    if consumo_saludable:
        print("El consumo de agua es saludable ✅")
    else:
        print("El consumo de agua excede lo recomendado ⚠️")


if __name__ == "__main__":
    main()
