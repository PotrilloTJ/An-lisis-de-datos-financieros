#Fix number 238
from datetime import datetime

import yfinance as yf
import pandas as pd


# ======================================
# FUNCIONES GENERALES
# ======================================

def comprobar_bibliotecas():
    """Comprueba que las bibliotecas necesarias estén disponibles."""
    try:
        import yfinance
        import pandas
        return True
    except ImportError as e:
        print("\nFalta una biblioteca necesaria.")
        print(f"Error: {e}")
        print("Instala las bibliotecas con:")
        print("pip install yfinance pandas")
        return False


def limpiar_datos(datos):
    """Elimina nulos y duplicados y ordena los datos por fecha."""
    if datos is None or datos.empty:
        return datos

    valores_nulos = datos.isnull().sum()
    duplicados = datos.duplicated().sum()

    print("\nValores nulos encontrados:")
    print(valores_nulos[valores_nulos > 0])

    print(f"\nFilas duplicadas encontradas: {duplicados}")

    datos = datos.drop_duplicates()
    datos = datos.dropna()
    datos = datos.sort_index()

    return datos


def descargar_datos_historicos(ticker, fecha_inicio, fecha_fin):
    """Descarga y limpia los datos históricos."""
    datos = yf.download(
        ticker,
        start=fecha_inicio,
        end=fecha_fin,
        auto_adjust=False,
        progress=False
    )

    if datos.empty:
        return None

    return limpiar_datos(datos)


# ======================================
# OPCIÓN 1
# ANÁLISIS DE UNA EMPRESA
# ======================================

def recopilar_datos_empresa(ticker):
    """Obtiene información y estados financieros de una empresa."""
    empresa = yf.Ticker(ticker)

    informacion = empresa.get_info()
    resultados = empresa.get_income_stmt(freq="yearly")
    balance = empresa.get_balance_sheet(freq="yearly")
    flujo = empresa.get_cash_flow(freq="yearly")
    return {
        "informacion": informacion,
        "resultados": resultados,
        "balance": balance,
        "flujo": flujo
    }


def obtener_informacion_empresa(informacion, ticker):
    """Extrae la información general de la empresa."""
    return {
        "nombre": informacion.get("longName"),
        "sector": informacion.get("sector"),
        "industria": informacion.get("industry"),
        "pais": informacion.get("country"),
        "moneda": informacion.get("currency"),
        "ticker": ticker
    }


def analizar_estado_resultados(resultados):
    """Obtiene datos principales del estado de resultados."""

    ingresos = (
        resultados.loc["TotalRevenue"].values[0]
        if "TotalRevenue" in resultados.index else None
    )

    utilidad_neta = (
        resultados.loc["NetIncome"].values[0]
        if "NetIncome" in resultados.index else None
    )

    gastos = (
        resultados.loc["OperatingExpense"].values[0]
        if "OperatingExpense" in resultados.index else None
    )

    if "TotalRevenue" in resultados.index:
        ingresos_historicos = resultados.loc["TotalRevenue"].values

        if len(ingresos_historicos) > 1 and ingresos_historicos[0] != 0:
            crecimiento = (
                (ingresos_historicos[-1] - ingresos_historicos[0])
                / ingresos_historicos[0]
            ) * 100
        else:
            crecimiento = None
    else:
        crecimiento = None

    return {
        "ingresos": ingresos,
        "utilidad_neta": utilidad_neta,
        "gastos": gastos,
        "crecimiento": crecimiento
    }


def analizar_balance(balance):
    """Obtiene datos principales del balance."""

    activos = (
        balance.loc["TotalAssets"].values[0]
        if "TotalAssets" in balance.index else None
    )

    pasivos = (
        balance.loc["TotalLiabilitiesNetMinorityInterest"].values[0]
        if "TotalLiabilitiesNetMinorityInterest" in balance.index
        else None
    )

    patrimonio = (
        balance.loc["StockholdersEquity"].values[0]
        if "StockholdersEquity" in balance.index else None
    )

    if "StockholdersEquity" in balance.index:
        patrimonio_historico = balance.loc["StockholdersEquity"].values

        if len(patrimonio_historico) > 1 and patrimonio_historico[0] != 0:
            evolucion = (
                (patrimonio_historico[-1] - patrimonio_historico[0])
                / patrimonio_historico[0]
            ) * 100
        else:
            evolucion = None
    else:
        evolucion = None

    return {
        "activos": activos,
        "pasivos": pasivos,
        "patrimonio": patrimonio,
        "evolucion": evolucion
    }


def analizar_flujo_efectivo(flujo):
    """Obtiene los principales flujos de efectivo."""

    operativo = (
        flujo.loc["OperatingCashFlow"].values[0]
        if "OperatingCashFlow" in flujo.index else None
    )

    inversion = (
        flujo.loc["InvestingCashFlow"].values[0]
        if "InvestingCashFlow" in flujo.index else None
    )

    financiamiento = (
        flujo.loc["FinancingCashFlow"].values[0]
        if "FinancingCashFlow" in flujo.index else None
    )

    return {
        "operativo": operativo,
        "inversion": inversion,
        "financiamiento": financiamiento
    }


def calcular_indicadores_financieros(resultados, balance):
    """Calcula margen neto, ROA, ROE y endeudamiento."""

    utilidad_neta = resultados["utilidad_neta"]
    ingresos = resultados["ingresos"]
    activos = balance["activos"]
    patrimonio = balance["patrimonio"]
    pasivos = balance["pasivos"]

    margen_neto = (
        utilidad_neta / ingresos
        if utilidad_neta is not None and ingresos not in (None, 0)
        else None
    )

    roa = (
        utilidad_neta / activos
        if utilidad_neta is not None and activos not in (None, 0)
        else None
    )

    roe = (
        utilidad_neta / patrimonio
        if utilidad_neta is not None and patrimonio not in (None, 0)
        else None
    )

    endeudamiento = (
        pasivos / activos
        if pasivos is not None and activos not in (None, 0)
        else None
    )

    return {
        "margen_neto": margen_neto,
        "roa": roa,
        "roe": roe,
        "endeudamiento": endeudamiento
    }


def opcion_1(ticker):
    """Realiza el análisis completo de una empresa."""

    print("\n======================================")
    print("       ANÁLISIS DE LA EMPRESA")
    print("======================================")

    print("\nRecopilando información de la empresa...")

    datos = recopilar_datos_empresa(ticker)

    informacion = datos["informacion"]
    resultados = datos["resultados"]
    balance = datos["balance"]
    flujo = datos["flujo"]

    informacion_empresa = obtener_informacion_empresa(
        informacion,
        ticker
    )

    estado_resultados = analizar_estado_resultados(resultados)
    estado_balance = analizar_balance(balance)
    estado_flujo = analizar_flujo_efectivo(flujo)

    indicadores = calcular_indicadores_financieros(
        estado_resultados,
        estado_balance
    )

    print("\nDatos de la empresa recopilados correctamente.")
    print("\nInformación de la empresa:")
    print(informacion_empresa)
    print("\nEstado de resultados:")
    print(estado_resultados)
    print("\nEstado del balance:")
    print(estado_balance)
    print("\nFlujo de efectivo:")
    print(estado_flujo)
    print("\nIndicadores financieros:")
    print(indicadores)


# ======================================
# OPCIÓN 2
# ANÁLISIS DE UN ACTIVO BURSÁTIL
# ======================================

def obtener_valor_activo(ticker):
    """Obtiene el precio más reciente disponible."""
    activo = yf.Ticker(ticker)
    return activo.fast_info["last_price"]


def calcular_rendimiento(datos):
    """Calcula el rendimiento porcentual del periodo."""

    if datos is None or datos.empty:
        return None

    cierre = datos["Close"]

    # Algunas versiones/configuraciones de yfinance
    # pueden devolver una columna de un solo ticker.
    if isinstance(cierre, pd.DataFrame):
        cierre = cierre.iloc[:, 0]

    precio_inicial = cierre.iloc[0]
    precio_final = cierre.iloc[-1]

    if precio_inicial == 0:
        return None

    return ((precio_final - precio_inicial) / precio_inicial) * 100


def calcular_estadisticas(datos):
    """Calcula estadísticas básicas del precio de cierre."""

    if datos is None or datos.empty:
        return None

    cierre = datos["Close"]

    if isinstance(cierre, pd.DataFrame):
        cierre = cierre.iloc[:, 0]

    return {
        "promedio": cierre.mean(),
        "maximo": cierre.max(),
        "minimo": cierre.min(),
        "mediana": cierre.median()
    }


def tendencia_activo_bursatil(datos):
    """Indica si el precio terminó por encima o por debajo del inicio."""

    if datos is None or datos.empty:
        return None

    cierre = datos["Close"]

    if isinstance(cierre, pd.DataFrame):
        cierre = cierre.iloc[:, 0]

    if cierre.iloc[-1] > cierre.iloc[0]:
        return "Tendencia ascendente"
    elif cierre.iloc[-1] < cierre.iloc[0]:
        return "Tendencia descendente"
    else:
        return "Sin cambio"


def volatilidad_activo_bursatil(datos):
    """Calcula la desviación estándar de los rendimientos diarios."""

    if datos is None or datos.empty:
        return None

    cierre = datos["Close"]

    if isinstance(cierre, pd.DataFrame):
        cierre = cierre.iloc[:, 0]

    rendimientos = cierre.pct_change().dropna()

    if rendimientos.empty:
        return None

    return rendimientos.std()


def opcion_2(ticker, fecha_inicio, fecha_fin):
    """Realiza el análisis de un activo bursátil."""

    print("\n======================================")
    print("       ANÁLISIS DEL ACTIVO")
    print("======================================")

    print("\nDescargando datos históricos...")

    datos = descargar_datos_historicos(
        ticker,
        fecha_inicio,
        fecha_fin
    )

    if datos is None or datos.empty:
        print("\nNo se encontraron datos para ese periodo.")
        return None

    valor_actual = obtener_valor_activo(ticker)
    rendimiento = calcular_rendimiento(datos)
    estadisticas = calcular_estadisticas(datos)
    tendencia = tendencia_activo_bursatil(datos)
    volatilidad = volatilidad_activo_bursatil(datos)

    return {
        "ticker": ticker,
        "valor_actual": valor_actual,
        "rendimiento": rendimiento,
        "estadisticas": estadisticas,
        "tendencia": tendencia,
        "volatilidad": volatilidad
    }


# ======================================
# OPCIÓN 3
# INFORMACIÓN ECONÓMICA
# ======================================

def opcion_3(ticker):
    """
    Mantiene la estructura de la opción 3.
    La fuente yfinance permite obtener información de mercado,
    pero aquí puedes agregar después indicadores económicos
    específicos.
    """

    print("\n======================================")
    print("     INFORMACIÓN ECONÓMICA")
    print("======================================")

    print("\nLa estructura de esta opción está lista.")
    print("Aquí puedes agregar posteriormente los indicadores")
    print("económicos que quieras analizar.")

    return {
        "ticker": ticker,
        "mensaje": "Módulo de información económica pendiente de ampliar."
    }


# ======================================
# MENÚ
# ======================================

def seleccionar_empresa():
    """Permite al usuario seleccionar una empresa."""

    print("\nSelecciona una empresa para analizar:")
    print("1. Apple (AAPL)")
    print("2. Microsoft (MSFT)")
    print("3. Amazon (AMZN)")
    print("4. Google (GOOGL)")
    print("5. Tesla (TSLA)")
    print("6. Meta (META)")
    print("7. Netflix (NFLX)")
    print("8. Otra empresa")

    opcion = input("\nSelecciona una opción: ")

    empresas = {
        "1": "AAPL",
        "2": "MSFT",
        "3": "AMZN",
        "4": "GOOGL",
        "5": "TSLA",
        "6": "META",
        "7": "NFLX"
    }

    if opcion in empresas:
        return empresas[opcion]

    if opcion == "8":
        ticker = input(
            "Introduce el ticker de la empresa (ejemplo: AAPL): "
        ).upper().strip()

        return ticker

    print("\nOpción inválida.")
    return None


def solicitar_fechas():
    """Solicita y valida las fechas del análisis."""

    while True:
        fecha_inicio = input(
            "\nIngresa la fecha de inicio (YYYY-MM-DD): "
        )

        fecha_fin = input(
            "Ingresa la fecha de fin (YYYY-MM-DD): "
        )

        try:
            inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
            fin = datetime.strptime(fecha_fin, "%Y-%m-%d")

            if inicio >= fin:
                print("\nLa fecha de inicio debe ser anterior a la fecha final.")
                continue

            print("\nLas fechas tienen un formato válido.")
            return fecha_inicio, fecha_fin

        except ValueError:
            print("\nFormato de fecha inválido.")
            print("Utiliza el formato YYYY-MM-DD.")


def mostrar_resultado(resultado):
    """Muestra el resultado final de forma legible."""

    print("\n======================================")
    print("             RESULTADO")
    print("======================================")

    if resultado is None:
        print("No fue posible obtener resultados.")
        return

    print(resultado)


def main():
    """Función principal del programa."""

    if not comprobar_bibliotecas():
        return

    print("======================================")
    print("     ANALIZADOR DE DATOS FINANCIEROS")
    print("======================================")

    print("\n¿Qué tipo de análisis deseas realizar?")
    print("1. Análisis de una empresa")
    print("2. Análisis de un activo bursátil")
    print("3. Análisis de información económica")

    opcion = input("\nSelecciona una opción: ").strip()

    if opcion not in ["1", "2", "3"]:
        print("\nOpción inválida. Vuelve a ejecutar el programa.")
        return

    print("\nHas seleccionado la opción:", opcion)

    fecha_inicio, fecha_fin = solicitar_fechas()

    ticker = seleccionar_empresa()

    if ticker is None:
        return

    try:
        if opcion == "1":
            print("\nHas seleccionado el análisis de una empresa.")
            resultado = opcion_1(ticker)

        elif opcion == "2":
            print("\nHas seleccionado el análisis de un activo bursátil.")
            resultado = opcion_2(
                ticker,
                fecha_inicio,
                fecha_fin
            )

        else:
            print("\nHas seleccionado el análisis de información económica.")
            resultado = opcion_3(ticker)

        mostrar_resultado(resultado)

        print("\nAnálisis completado.")

    except Exception as e:
        print("\nOcurrió un error durante el análisis.")
        print(f"Tipo de error: {type(e).__name__}")
        print(f"Detalle: {e}")


if __name__ == "__main__":
    main()



    
