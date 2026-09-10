#fix number 185
from abc import ABC, abstractmethod
from datetime import datetime
#No sabía como extraer las bibliotecas, lo tuve que investigar y parece ser que es así, no sé si es correcto, pero funciona.
try:
    import yfinance as yf
except ImportError: 

    def _require_yfinance():
        raise ImportError(
            "La biblioteca 'yfinance' no está instalada. Instálala con: pip install yfinance"
        )
try: 
    import pandas as pd
except ImportError: 

    def _require_pandas():
        raise ImportError(
            "La biblioteca 'pandas' no está instalada. Instálala con: pip install pandas"
        )
# Jejejejeje
# Mantiene el modulo util para el analisis y, a la vez, evita que el usuario tenga que instalarlo manualmente. Esto es útil para garantizar que el código funcione correctamente sin depender de la instalación previa de bibliotecas externas.

def comprobar_bibliotecas():

    if yf is None:
        print("\nLa biblioteca 'yfinance' no está instalada.")
        print("Instálala con: pip install yfinance")
        return False

    if pd is None:
        print("\nLa biblioteca 'pandas' no está instalada.")
        print("Instálala con: pip install pandas")
        return False

    return True


def limpiar_datos(datos):

    # Comprobar valores nulos (función isnull() de pandas) y contar cuántos valores nulos hay en cada columna (función sum() de pandas)
    valores_nulos = datos.isnull().sum()

    # Comprobar filas duplicadas (función duplicated() de pandas)
    duplicados = datos.duplicated().sum()

    # Eliminar filas duplicadas (función drop_duplicates() de pandas)
    datos = datos.drop_duplicates()

    # Eliminar filas con valores nulos (función dropna() de pandas)
    datos = datos.dropna()

    # Ordenar los datos cronológicamente (función sort_index() de pandas)
    datos = datos.sort_index()

    return datos

# ======================================
# FUNCIONES PARA LA OPCIÓN 1
# ANÁLISIS DE UNA EMPRESA
# ======================================
def opcion_1():

    def recopilar_datos_empresa(ticker):

        empresa = yf.Ticker(ticker)

        informacion = empresa.info
        resultados = empresa.income_stmt
        balance = empresa.balance_sheet
        flujo = empresa.cashflow

        return informacion, resultados, balance, flujo

    def obtener_informacion_empresa(informacion, ticker):
    #La instrucción .get funciona como un método seguro para acceder a los valores del diccionario, evitando errores si la clave no existe.
        return {
        #obterner información general de la empresa, como su nombre, sector, industria, país, moneda y ticker.
        "nombre": informacion.get("longName"),
        "sector": informacion.get("sector"),
        "industria": informacion.get("industry"),
        "pais": informacion.get("country"),
        "moneda": informacion.get("currency"),
        "ticker": ticker
        }


    def analizar_estado_resultados(resultados):
    #La instrucción .loc de pandas se utiliza para acceder a filas y columnas específicas de un DataFrame utilizando etiquetas. En este caso, se utiliza para obtener los valores de ingresos, utilidad neta y gastos de la empresa a partir del estado de resultados.
    # Devolver resultados
        return {
            # Obtener ingresos
    "ingresos": resultados.loc["Total Revenue"].values[0] if "Total Revenue" in resultados.index else None,
    # Obtener utilidad neta
    "utilidad_neta": resultados.loc["Net Income"].values[0] if "Net Income" in resultados.index else None,
    # Obtener gastos
    "gastos": resultados.loc["Operating Expenses"].values[0] if "Operating Expenses" in resultados.index else None,
    # Calcular crecimiento
    "crecimiento": (resultados.loc["Total Revenue"].values[-1] - resultados.loc["Total Revenue"].values[0]) / resultados.loc["Total Revenue"].values[0] * 100 if "Total Revenue" in resultados.index and len(resultados.loc["Total Revenue"].values) > 1 else None
        }


    def analizar_balance(balance):
    #Tristemente, todos estos deben de estar en ingles. Maldigo a los gringos por no traducirlo, pero bueno, es lo que hay. No me queda de otra que adaptarme a su idioma.
    # Obtener activos
        activos = balance.loc["Total Assets"].values[0] if "Total Assets" in balance.index else None
    # Obtener pasivos
        pasivos = balance.loc["Total Liabilities"].values[0] if "Total Liabilities" in balance.index else None
    # Obtener patrimonio
        patrimonio = balance.loc["Total Stockholder Equity"].values[0] if "Total Stockholder Equity" in balance.index else None
    # Analizar su evolución
        evolucion_patrimonio = (balance.loc["Total Stockholder Equity"].values[-1] - balance.loc["Total Stockholder Equity"].values[0]) / balance.loc["Total Stockholder Equity"].values[0] * 100   if patrimonio and balance.loc["Total Stockholder Equity"].values[0] != 0 else None
    # Devolver resultados
        return {    
        "activos": activos,
        "pasivos": pasivos,
        "patrimonio": patrimonio,
        "evolucion": evolucion_patrimonio
        }


    def analizar_flujo_efectivo(flujo):
    # operación, inversión y financiamiento.
        return {
        # Obtener flujo de efectivo de operación
        "operativo": flujo.loc["Total Cash From Operating Activities"].values[0] if "Total Cash From Operating Activities" in flujo.index else None,
        # Obtener flujo de efectivo de inversión
        "inversion": flujo.loc["Total Cashflows From Investing Activities"].values[0] if "Total Cashflows From Investing Activities" in flujo.index else None,
        # Obtener flujo de efectivo de financiamiento   
        "financiamiento": flujo.loc["Total Cash From Financing Activities"].values[0] if "Total Cash From Financing Activities" in flujo.index else None
    }


    def calcular_indicadores_financieros(resultados, balance):
    # Calcular margen neto
        margen_neto = resultados["utilidad_neta"] / resultados["ingresos"] if resultados["ingresos"] else None
    # Calcular ROA
        roa = resultados["utilidad_neta"] / balance["activos"] if balance["activos"] else None
    # Calcular ROE
        roe = resultados["utilidad_neta"] / balance["patrimonio"] if balance["patrimonio"] else None
    # Calcular endeudamiento
        endeudamiento = balance["pasivos"] / balance["activos"] if balance["activos"] else None
    # Devolver indicadores
        indicadores = {
        "margen_neto": margen_neto,
        "roa": roa,
        "roe": roe,
        "endeudamiento": endeudamiento
    }

        return indicadores


    def analizar_empresa(ticker):

        print("\n======================================")
        print("       ANÁLISIS DE LA EMPRESA")
        print("======================================")

        print("\nRecopilando información de la empresa...")

    informacion, resultados, balance, flujo = recopilar_datos_empresa(ticker)

    # Limpiar los estados financieros
    resultados = limpiar_datos(resultados)
    balance = limpiar_datos(balance)
    flujo = limpiar_datos(flujo)

    # Obtener información general
    informacion_empresa = obtener_informacion_empresa(
        informacion,
        ticker
    )

    # Analizar los diferentes estados financieros
    estado_resultados = analizar_estado_resultados(
        resultados
    )

    estado_balance = analizar_balance(
        balance
    )

    estado_flujo = analizar_flujo_efectivo(
        flujo
    )

    # Calcular indicadores financieros
    indicadores = calcular_indicadores_financieros(
        estado_resultados,
        estado_balance
    )

    print("\nDatos de la empresa recopilados correctamente.")

    return {
        "informacion": informacion_empresa,
        "resultados": estado_resultados,
        "balance": estado_balance,
        "flujo": estado_flujo,
        "indicadores": indicadores
    }
opcion_1()
# ======================================
# FUNCIONES PARA LA OPCIÓN 2
# ANÁLISIS DE UN ACTIVO BURSÁTIL
# ======================================
def opcion_2():
    def recopilar_datos_empresa(ticker):

        empresa = yf.Ticker(ticker)

        informacion = empresa.info
        resultados = empresa.income_stmt
        balance = empresa.balance_sheet
        flujo = empresa.cashflow

        return informacion, resultados, balance, flujo
    
opcion_2()
# ======================================
# FUNCIONES PARA LA OPCIÓN 3
# ANÁLISIS DE INFORMACIÓN ECONÓMICA
# ======================================







#Otras funciones que se pueden agregar para mejorar el análisis financiero, como calcular el rendimiento de la acción en el período seleccionado y calcular estadísticas básicas de los datos descargados.
def calcular_rendimiento(datos):
    #La función calcular_rendimiento calcula el rendimiento de la acción en el período seleccionado. Se toma el precio de cierre inicial y final, y se calcula el rendimiento porcentual utilizando la fórmula: ((precio_final - precio_inicial) / precio_inicial) * 100.
    #Precio inicial y precio final se obtienen de la columna "Close" del DataFrame de datos, utilizando iloc para acceder a los valores en las posiciones correspondientes.
    precio_inicial = datos["Close"].iloc[0]
    precio_final = datos["Close"].iloc[-1]

    rendimiento = (
        (precio_final - precio_inicial)
        / precio_inicial
    ) * 100

    return rendimiento
def calcular_estadisticas(datos):
    #La función calcular_estadisticas calcula estadísticas básicas de los datos descargados, como el promedio, máximo, mínimo y mediana de los precios de cierre. Se utiliza la columna "Close" del DataFrame de datos y se aplican las funciones mean(), max(), min() y median() de pandas para obtener los valores correspondientes.
    estadisticas = {
        "promedio": datos["Close"].mean(),
        "maximo": datos["Close"].max(),
        "minimo": datos["Close"].min(),
        "mediana": datos["Close"].median()
    }

    return estadisticas

#Está muy desordenado jejejejeje, pero funciona, lo importante es que funcione y que sea entendible para el usuario.
def recopilar_datos_empresa(ticker):

    empresa = yf.Ticker(ticker)

    informacion = empresa.info
    resultados = empresa.income_stmt
    balance = empresa.balance_sheet
    flujo = empresa.cashflow

    return informacion, resultados, balance, flujo
#Para que sea vea "llamativo" y "profesional" el analizador de datos financieros.
print("======================================")
print("     ANALIZADOR DE DATOS FINANCIEROS")
print("======================================")

# 1. Solicitar el tipo de análisis
#Solicitación al usuario del tipo de análisis que desea realizar y la fuente de datos que desea utilizar.

print("\n¿Qué tipo de análisis deseas realizar?")
print("1. Análisis de una empresa")
print("2. Análisis de un activo bursátil")
print("3. Análisis de información económica")

opcion = input("\nSelecciona una opción: ")

print("\nHas seleccionado la opción:", opcion)


# Solicitar fechas que desea analizar y verificar que sean válidas
# 2. Solicitar los datos necesarios
if opcion in ["1", "2", "3"]:

    fecha_inicio = input(
        "\nIngresa la fecha de inicio (YYYY-MM-DD): "
    )

    fecha_fin = input(
        "Ingresa la fecha de fin (YYYY-MM-DD): "
    )

    try:

        datetime.strptime(fecha_inicio, "%Y-%m-%d")
        datetime.strptime(fecha_fin, "%Y-%m-%d")

        print("\nLas fechas tienen un formato válido.")

    except ValueError:

        print("\nFormato de fecha inválido.")
        print("Utiliza el formato YYYY-MM-DD.")
# 3. Recopilar los datos del periodo seleccionado
print("\nSelecciona una empresa para analizar:")
print("1. Apple (AAPL)")
print("2. Microsoft (MSFT)")
print("3. Amazon (AMZN)")
print("4. Google (GOOGL)")
print("5. Tesla (TSLA)")
print("6. Meta (META)")
print("7. Netflix (NFLX)")
print("8. Otra empresa")

N = input("\nSelecciona una opción: ")

if N == "1":
    ticker = "AAPL"
elif N == "2":
    ticker = "MSFT"
elif N == "3":
    ticker = "AMZN"
elif N == "4":
    ticker = "GOOGL"
elif N == "5":
    ticker = "TSLA"
elif N == "6":
    ticker = "META"
elif N == "7":
    ticker = "NFLX"
elif N == "8":
    ticker = input(
        "Introduce el ticker de la empresa (ejemplo: AAPL): "
    ).upper()
else:
    print("Opción inválida.")
    ticker = None
# Obtener datos históricos de las fechas ingresadas por el usuario, utilizando la biblioteca yfinance para descargar los datos financieros de la empresa seleccionada.
datos = yf.download( 
    ticker,
    start=fecha_inicio,
    end=fecha_fin
)

def obtener_informacion_empresa(ticker):
    #yf.ticker funciona como un objeto que representa una empresa en Yahoo Finance, y permite acceder a información detallada sobre la empresa, como su nombre, sector, industria, país, moneda y otros datos relevantes.
    empresa = yf.Ticker(ticker)
    #empresa.info devuelve un diccionario con información detallada sobre la empresa, incluyendo su nombre, sector, industria, país, moneda y otros datos relevantes.
    informacion = empresa.info

    return {
        #.get funciona como un método seguro para acceder a los valores del diccionario, evitando errores si la clave no existe.
        "nombre": informacion.get("longName"),
        "sector": informacion.get("sector"),
        "industria": informacion.get("industry"),
        "pais": informacion.get("country"),
        "moneda": informacion.get("currency"),
        "ticker": ticker
    }

def analizar_estado_resultados(ticker):

    empresa = yf.Ticker(ticker)

    resultados = empresa.income_stmt

    return resultados


def analizar_balance(ticker):

    empresa = yf.Ticker(ticker)

    balance = empresa.balance_sheet

    return balance


def analizar_flujo_efectivo(ticker):

    empresa = yf.Ticker(ticker)

    flujo = empresa.cashflow

    return flujo


def analizar_empresa(ticker):

    print("\n======================================")
    print("       ANÁLISIS DE LA EMPRESA")
    print("======================================")

    informacion, resultados, balance, flujo = recopilar_datos_empresa(ticker)

    indicadores = calcular_indicadores_financieros(
        resultados,
        balance
    )

    print("\nAnálisis de empresa completado.")

    return {
        "informacion": informacion,
        "resultados": resultados,
        "balance": balance,
        "flujo": flujo,
        "indicadores": indicadores
    }
analizar_empresa(ticker)
if opcion == "1":
    print("\nHas seleccionado el análisis de una empresa.")
    print("\nRecopilando datos de la empresa seleccionada...")
    print("\nAnalizando la empresa...")
    print(f"{opcion_1(ticker)}")
    print("\nAnálisis de empresa completado.")
elif opcion == "2":
    print("\nHas seleccionado el análisis de un activo bursátil.")
    print("\nRecopilando datos del activo bursátil seleccionado...")
    print("\nAnalizando el activo bursátil...")

elif opcion == "3":
    print("\nHas seleccionado el análisis de información económica.")
    

else:
    print("\nOpción inválida. Por favor, vuelve a ejecutar el programa y selecciona una opción válida.")


# 3. Recopilar los datos del periodo seleccionado

# Comprobar que existen datos
# paso 4 fue recorrido a la linea 19, que es la función limpiar_datos, que se encarga de limpiar los datos descargados y eliminar valores nulos y duplicados.
# 5. Estructurar los datos y ordenarlos
# .sort_index() de pandas se utiliza para ordenar los datos cronológicamente según el índice del DataFrame, que en este caso es la fecha. Esto asegura que los datos estén en el orden correcto para realizar análisis y cálculos posteriores.
datos = datos.sort_index()

    
