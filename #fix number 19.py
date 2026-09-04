#fix number 19
#Solicitación al usuario del tipo de análisis que desea realizar y la fuente de datos que desea utilizar.
print("=== ANALIZADOR DE DATOS FINANCIEROS ===")

# 1. Solicitar el tipo de análisis
print("\n¿Qué tipo de análisis deseas realizar?")
print("1. Análisis de una empresa")
print("2. Análisis de un activo bursátil")
print("3. Análisis de información económica")

tipo_analisis = input("Selecciona una opción (1-3): ")

# Solicitar fechas
fecha_inicial = input("Ingresa la fecha inicial (DD/MM/AAAA): ")
fecha_final = input("Ingresa la fecha final (DD/MM/AAAA): ")


# 2. Solicitar los datos necesarios
print("\n=== DATOS NECESARIOS ===")

if tipo_analisis == "1":
    empresa = input("Ingresa el nombre de la empresa: ")
    datos = input("¿Qué datos financieros deseas analizar?: ")

elif tipo_analisis == "2":
    activo = input("Ingresa el nombre o símbolo del activo bursátil: ")
    datos = input("¿Qué datos históricos deseas analizar?: ")

elif tipo_analisis == "3":
    indicador = input("Ingresa el indicador económico que deseas analizar: ")
    datos = input("¿Qué información económica deseas obtener?: ")

else:
    print("Opción no válida.")
    exit()


# 3. Recopilar los datos del periodo seleccionado
print("\n=== RECOPILACIÓN DE DATOS ===")

print("Tipo de análisis:", tipo_analisis)
print("Fecha inicial:", fecha_inicial)
print("Fecha final:", fecha_final)
print("Datos solicitados:", datos)

print("\nRecopilando datos...")
print("Datos del periodo seleccionado obtenidos correctamente.")