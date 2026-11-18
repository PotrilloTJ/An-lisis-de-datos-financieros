# ANALIZADOR DE DATOS FINANCIEROS

from datetime import datetime

# Importar yfinance
try:
    import yfinance as yf
except ImportError:
    yf = None

# Importar pandas
try:
    import pandas as pd
except ImportError:
    pd = None
# ======================================
# DICCIONARIOS A UTILIZAR PARA OBTENER VALORES DE LOS ESTADOS FINANCIEROS
# ======================================
# Ingresos
ETIQUETAS_INGRESOS = [
    "Total Revenue",
    "Operating Revenue",
    "Revenue",
    "Total Revenues",
    "Sales Revenue",
    "Net Sales"
]

# Utilidad neta
ETIQUETAS_UTILIDAD_NETA = [
    "Net Income",
    "Net Income Common Stockholders",
    "Net Income Continuous Operations",
    "Net Income From Continuing Operation Net Minority Interest",
    "Net Income From Continuing And Discontinued Operation",
    "Net Income Including Noncontrolling Interests"
]

# Gastos operativos
ETIQUETAS_GASTOS = [
    "Operating Expense",
    "Operating Expenses",
    "Total Expenses",
    "Selling General And Administration",
    "Research And Development"
]

# Utilidad operativa
ETIQUETAS_UTILIDAD_OPERATIVA = [
    "Operating Income",
    "Total Operating Income As Reported",
    "EBIT"
]

# Utilidad bruta
ETIQUETAS_UTILIDAD_BRUTA = [
    "Gross Profit"
]

# Costo de ventas
ETIQUETAS_COSTO_VENTAS = [
    "Cost Of Revenue",
    "Reconciled Cost Of Revenue"
]

# Activos
ETIQUETAS_ACTIVOS = [
    "Total Assets",
    "Total Asset"
]

# Pasivos
ETIQUETAS_PASIVOS = [
    "Total Liabilities Net Minority Interest",
    "Total Liabilities",
    "Total Non Current Liabilities Net Minority Interest"
]

# Patrimonio
ETIQUETAS_PATRIMONIO = [
    "Stockholders Equity",
    "Total Stockholder Equity",
    "Common Stock Equity",
    "Total Equity Gross Minority Interest"
]

# Activos corrientes
ETIQUETAS_ACTIVOS_CORRIENTES = [
    "Current Assets",
    "Total Current Assets"
]

# Pasivos corrientes
ETIQUETAS_PASIVOS_CORRIENTES = [
    "Current Liabilities",
    "Total Current Liabilities"
]

# Deuda total
ETIQUETAS_DEUDA = [
    "Total Debt",
    "Long Term Debt",
    "Current Debt",
    "Long Term Debt And Capital Lease Obligation"
]

# Efectivo
ETIQUETAS_EFECTIVO = [
    "Cash And Cash Equivalents",
    "Cash Cash Equivalents And Short Term Investments",
    "Cash Equivalents",
    "Cash Financial"
]

TIQUETAS_FLUJO_OPERATIVO = [
    "Operating Cash Flow",
    "Total Cash From Operating Activities",
    "Cash Flow From Continuing Operating Activities"
]

# Flujo de inversión
ETIQUETAS_FLUJO_INVERSION = [
    "Investing Cash Flow",
    "Total Cash Flows From Investing Activities",
    "Cash Flow From Continuing Investing Activities"
]

# Flujo de financiamiento
ETIQUETAS_FLUJO_FINANCIAMIENTO = [
    "Financing Cash Flow",
    "Total Cash From Financing Activities",
    "Cash Flow From Continuing Financing Activities"
]

# Flujo de efectivo libre
ETIQUETAS_FLUJO_LIBRE = [
    "Free Cash Flow"
]

# Gastos de capital
ETIQUETAS_CAPEX = [
    "Capital Expenditure",
    "Capital Expenditures"
]

# Depreciación y amortización
ETIQUETAS_DEPRECIACION = [
    "Depreciation And Amortization",
    "Depreciation",
    "Depreciation Amortization Depletion",
    "Reconciled Depreciation"
]
# Flujo de efectivo operativo, inversión y financiamiento
ETIQUETAS_FLUJO_OPERATIVO = [
    "Operating Cash Flow",
    "Total Cash From Operating Activities",
    "Cash Flow From Continuing Operating Activities"
]
# Flujo de efectivo de inversión
ETIQUETAS_FLUJO_INVERSION = [
    "Investing Cash Flow",
    "Total Cash Flows From Investing Activities",
    "Cash Flow From Continuing Investing Activities"
]
# Flujo de efectivo de financiamiento
ETIQUETAS_FLUJO_FINANCIAMIENTO = [
    "Financing Cash Flow",
    "Total Cash From Financing Activities",
    "Cash Flow From Continuing Financing Activities"
]

# ======================================
# IMPLEMENTACIÓN DE LAS LIBRERÍAS PARA FACILITAR EL ANÁLISIS DE DATOS FINANCIEROS PQ ME DIÓ FLOJERA HACER TODAS LAS CONDICIONES YO XD
# ======================================

def obtener_valor(dataframe, etiquetas): #Mi cerebro no daba y, la neta, lo tuve que buscar en Yahoo, pero, lo entiendo.

    for etiqueta in etiquetas:

        if etiqueta in dataframe.index:

            valores = dataframe.loc[etiqueta].values

            if len(valores) > 0:
                return valores[0]

    return None

# ======================================
# FUNCIONES GENERALES
# ======================================

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

    # Comprobar valores nulos
    valores_nulos = datos.isnull().sum()

    # Comprobar filas duplicadas
    duplicados = datos.duplicated().sum()

    # Eliminar filas duplicadas
    datos = datos.drop_duplicates()

    # Eliminar filas con valores nulos
    datos = datos.dropna()

    # Ordenar los datos cronológicamente
    datos = datos.sort_index()

    return datos


# ======================================
# FUNCIONES PARA LA OPCIÓN 1
# ANÁLISIS DE UNA EMPRESA
# ======================================

def info_empresa(ticker):
    empresa = yf.Ticker(ticker)
    informacion = empresa.info
    return informacion

def resultados_empresa(ticker):
    empresa = yf.Ticker(ticker)
    resultados = empresa.income_stmt
    return resultados

def balance_empresa(ticker):
    empresa = yf.Ticker(ticker)
    balance = empresa.balance_sheet
    return balance

def flujo_empresa(ticker):
    empresa = yf.Ticker(ticker)
    flujo = empresa.cashflow
    return flujo


def obtener_informacion_empresa(informacion, ticker):

    return {
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
    "crecimiento": (resultados.loc["Total Revenue"].values[0] - resultados.loc["Total Revenue"].values[-1]) / resultados.loc["Total Revenue"].values[-1] * 100 if "Total Revenue" in resultados.index and len(resultados.loc["Total Revenue"].values) > 1 else None
        }


def analizar_balance(balance):
    activos = obtener_valor(
        balance, ETIQUETAS_ACTIVOS
    )
    pasivos = obtener_valor(
        balance, ETIQUETAS_PASIVOS
    )

    patrimonio = obtener_valor(
        balance, ETIQUETAS_PATRIMONIO
    )
    return {
        "activos": activos,
        "pasivos": pasivos,
        "patrimonio": patrimonio
    }


def analizar_flujo_efectivo(flujo):

    operativo = obtener_valor(
        flujo, ETIQUETAS_FLUJO_OPERATIVO
    )

    inversion = obtener_valor(
        flujo, ETIQUETAS_FLUJO_INVERSION
    )

    financiamiento = obtener_valor(
        flujo, ETIQUETAS_FLUJO_FINANCIAMIENTO
    )

    return {
        "operativo": operativo,
        "inversion": inversion,
        "financiamiento": financiamiento
    }



def calcular_indicadores_financieros(resultados, balance):
    # Calcular margen neto
        margen_neto = resultados["utilidad_neta"] / resultados["ingresos"] if resultados["ingresos"] else None
    # Calcular ROA
        roa = resultados["utilidad_neta"] / balance["activos"] if balance["activos"] else None
    # Calcular ROE
        roe = resultados["utilidad_neta"] / balance["patrimonio"] if balance["patrimonio"] else None
    # Calcular endeudamiento
        endeudamiento = (
    balance["pasivos"] / balance["activos"]
    if balance["activos"] is not None
    and balance["pasivos"] is not None
    and balance["activos"] != 0
    else None
)
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

    informacion = info_empresa(ticker)
    resultados = resultados_empresa(ticker)
    balance = balance_empresa(ticker)
    flujo = flujo_empresa(ticker)
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

    print("\ninformacion:", informacion_empresa)
    print("\nresultados:", estado_resultados)
    print("\nbalance:", estado_balance)
    print("\nflujo:", estado_flujo)
    print("\nindicadores:", indicadores)

# ======================================
# FUNCIONES PARA LA OPCIÓN 2
# ANÁLISIS DE UN ACTIVO BURSÁTIL
# ======================================

def recopilar_datos_activo(ticker, fecha_inicio, fecha_fin):

    datos = yf.download(
        ticker,
        start=fecha_inicio,
        end=fecha_fin
    )

    return datos


def calcular_rendimiento(datos):

    precio_inicial = datos["Close"].iloc[0]
    precio_final = datos["Close"].iloc[-1]

    rendimiento = (
        (precio_final - precio_inicial)
        / precio_inicial
    ) * 100

    return rendimiento


def calcular_estadisticas(datos):

    estadisticas = {
        "promedio": datos["Close"].mean(),
        "maximo": datos["Close"].max(),
        "minimo": datos["Close"].min(),
        "mediana": datos["Close"].median()
    }

    return estadisticas


def calcular_volatilidad(datos):
    # Ni idea de cómo encontré la función pct_change, pero me sirve para calcular la volatilidad de los precios de cierre del activo bursátil.
    # Aparentemenete, la función pct_change() de pandas calcula el cambio porcentual entre el valor actual y el valor anterior en una serie de datos. En este caso, se utiliza para calcular las variaciones porcentuales diarias del precio de cierre del activo bursátil.
    variaciones = datos["Close"].pct_change()

    volatilidad = variaciones.std()

    return volatilidad


def analizar_activo(ticker, fecha_inicio, fecha_fin):

    print("\n======================================")
    print("       ANÁLISIS DEL ACTIVO")
    print("======================================")

    print("\nRecopilando datos del activo bursátil...")

    datos = recopilar_datos_activo(
        ticker,
        fecha_inicio,
        fecha_fin
    )

    if datos.empty:
        print("\nNo se encontraron datos para el periodo seleccionado.")
        return None

    datos = limpiar_datos(datos)

    rendimiento = calcular_rendimiento(datos)
    estadisticas = calcular_estadisticas(datos)
    volatilidad = calcular_volatilidad(datos)

    print("\nDatos del activo recopilados correctamente.")

    print("datos:", datos)
    print("rendimiento:", rendimiento)
    print("estadisticas:", estadisticas)
    print("volatilidad:", volatilidad)


# ======================================
# FUNCIONES PARA LA OPCIÓN 3
# INFORMACIÓN ECONÓMICA
# ======================================

def analizar_informacion_economica():

    print("\n======================================")
    print("    ANÁLISIS DE INFORMACIÓN ECONÓMICA")
    print("======================================")

    print("\nEsta sección se desarrollará posteriormente.")
    

    return None


# ======================================
# PROGRAMA PRINCIPAL
# ======================================

if not comprobar_bibliotecas():

    print("\nNo se puede ejecutar el programa. Comprueba que todas las bibliotecas necesarias estén instaladas.")
    
else:

    print("======================================")
    print("     ANALIZADOR DE DATOS FINANCIEROS")
    print("======================================")

    # ==================================
    # 1. Solicitar el tipo de análisis
    # ==================================

    print("\n¿Qué tipo de análisis deseas realizar?")
    print("1. Análisis de una empresa")
    print("2. Análisis de un activo bursátil")
    print("3. Análisis de información económica")

    opcion = input("\nSelecciona una opción: ")

    # ==================================
    # 2. Solicitar fechas
    # ==================================

    if opcion in ["1", "2", "3"]:

        fecha_inicio = input(
            "\nIngresa la fecha de inicio (YYYY-MM-DD): "
        )

        fecha_fin = input(
            "Ingresa la fecha de fin (YYYY-MM-DD): "
        )

        try:

            fecha_inicio_obj = datetime.strptime(
                fecha_inicio,
                "%Y-%m-%d"
            )

            fecha_fin_obj = datetime.strptime(
                fecha_fin,
                "%Y-%m-%d"
            )

            if fecha_inicio_obj >= fecha_fin_obj:

                print("\nLa fecha de inicio debe ser anterior")
                print("a la fecha final.")

            else:

                print("\nLas fechas tienen un formato válido.")

                # ==================================
                # 3. Seleccionar empresa
                # ==================================

                if opcion == "1":

                    print("\nSelecciona una empresa para analizar (escribe el número):")
                    print("1. Apple (AAPL)")
                    print("2. Microsoft (MSFT)")
                    print("3. Amazon (AMZN)")
                    print("4. Google (GOOGL)")
                    print("5. Tesla (TSLA)")
                    print("6. Meta (META)")
                    print("7. Netflix (NFLX)")
                    print("8. Otra empresa")

                    seleccion_empresa = input(
                        "\nSelecciona una opción: "
                    )

                    if seleccion_empresa == "1":
                        ticker = "AAPL"

                    elif seleccion_empresa == "2":
                        ticker = "MSFT"

                    elif seleccion_empresa == "3":
                        ticker = "AMZN"

                    elif seleccion_empresa == "4":
                        ticker = "GOOGL"

                    elif seleccion_empresa == "5":
                        ticker = "TSLA"

                    elif seleccion_empresa == "6":
                        ticker = "META"

                    elif seleccion_empresa == "7":
                        ticker = "NFLX"

                    elif seleccion_empresa == "8":

                        ticker = input(
                            "\nIntroduce el ticker de la empresa "
                            "(ejemplo: AAPL): "
                        ).upper()

                    else:

                        print("\nOpción inválida.")
                        ticker = None

                    if ticker is not None:

                        print(
                            "\nHas seleccionado el análisis "
                            "de una empresa."
                        )

                        print("\n======================================")
                        print("      INFORMACIÓN GENERAL")
                        print("======================================")
                        analizar_empresa(ticker)
                        print("Gracias por utilizar el Analizador de Datos Financieros.")

                # ==================================
                # OPCIÓN 2
                # ==================================

                elif opcion == "2":

                    print(
                        "\nHas seleccionado el análisis "
                        "de un activo bursátil."
                    )

                    ticker = input(
                        "\nIntroduce el ticker del activo "
                        "(ejemplo: AAPL): "
                    ).upper()

                    resultado = analizar_activo(
                        ticker,
                        fecha_inicio,
                        fecha_fin
                    )

                    if resultado is not None:

                        print("\n======================================")
                        print("       RESULTADOS DEL ANÁLISIS")
                        print("======================================")

                        print(resultado)


                # ==================================
                # OPCIÓN 3
                # ==================================

                elif opcion == "3":

                    print(
                        "\nHas seleccionado el análisis "
                        "de información económica."
                    )

                    analizar_informacion_economica()

        except ValueError:

            print("\nFormato de fecha inválido.")
            print("Utiliza el formato YYYY-MM-DD.")

    else:

        print(
            "\nOpción inválida. Por favor, vuelve a ejecutar "
            "el programa y selecciona una opción válida."
        )