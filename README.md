# Análisis de datos financieros
### CONTEXTO
El análisis financiero es una disciplina fundamental que aprovecha el análisis de datos, los modelos estadísticos y las herramientas informáticas para ayudar a empresas y particulares a tomar decisiones financieras con conocimiento de causa. Mediante el examen de las tendencias históricas, la dinámica del mercado y el rendimiento de la organización, las empresas pueden identificar patrones, prever tendencias futuras y optimizar sus resultados financieros. Este proceso es vital para crear estrategias que mejoren la eficiencia, gestionen el riesgo y optimicen los recursos.

En análisis financiero sigue evolucionando, su integración con tecnologías como el aprendizaje automático es cada vez más importante. Los algoritmos de aprendizaje automático pueden mejorar las capacidades predictivas, permitiendo a las empresas anticiparse a los cambios del mercado y responder en consecuencia.

Este programa se enfocará a realizar un panel que sea capaz de utilizar librerías especializadas para descargar, limpiar, calcular métricas y visualizar información bursátil o económica de forma automatizada. El analizador funcionará transformando datos contables y de mercado en información clara para guiar la toma de decisiones.

Algunos pasos que busca seguir el programa son:
    -Recopilación de datos
    -Estructuración para la visualización de los datos y ayudar al fácil entendimiento del usuario
    -Procesamiento y cálculos para medir indicadores clave como la liquidez y rentabilidad

El análisis de datos financieros soluciona la falta de visibilidad sobre la salud económica, permitiendo tomar decisiones informadas y detectar riesgos a tiempo. Los Problemas principales que resuelve el análisis de datos son:
    - Desconocimiento de la rentabilidad real
    - Riesgo de crédito y morosidad
    - Falta de liquidez y problemas de flujo de caja
    - Incumplimiento normativo
    - Procesos manuales lentos

    Analizador de Datos Financieros
## Funcionalidades

Actualmente, el programa contempla tres modalidades de análisis:

### 1. Análisis de empresas

Permite consultar y procesar información financiera de empresas mediante su identificador bursátil (ticker).

Incluye:

Información general: nombre, sector, industria, país y moneda.

Estado de resultados: ingresos, utilidad neta, gastos operativos y crecimiento de ingresos.

Balance general: activos, pasivos y patrimonio.

Estado de flujo de efectivo: actividades operativas, de inversión y financiamiento.

Indicadores financieros:

Margen neto.

Rendimiento sobre activos (ROA).

Rendimiento sobre patrimonio (ROE).

Razón de endeudamiento.

### 2. Análisis de activos bursátiles

Permite obtener y analizar información histórica de un activo bursátil durante un periodo determinado.

Incluye:

Recopilación de precios históricos.

Limpieza y organización de datos.

Cálculo del rendimiento porcentual.

Estadísticas descriptivas:

Precio promedio.

Precio máximo.

Precio mínimo.

Mediana.

Cálculo de volatilidad mediante las variaciones porcentuales de los precios de cierre.

### 3. Análisis de información económica

Modalidad contemplada en el menú principal, actualmente en desarrollo.

## Tecnologías utilizadas

### Tecnología

Aplicación

    Python

Lenguaje principal de programación.

    Python

Manipulación y procesamiento de datos:

    Pandas

Obtención de información financiera e histórica.

    yfinance

Validación y procesamiento de fechas.

    datetime


## Instalación y ejecución

### Requisitos previos

- Python 3 instalado.

- Conexión a Internet.

- Bibliotecas necesarias para el análisis.

### 1. Clonar el repositorio

    git clone https://github.com/PotrilloTJ/An-lisis-de-datos-financieros.git

### 2. Acceder al directorio

    cd An-lisis-de-datos-financieros

### 3. Instalar las dependencias

    pip install pandas yfinance
### 4. Ejecutar el programa

    python "#fix number 19.py"

## Ejemplo de uso

Al iniciar el programa, se presenta un menú que permite seleccionar la modalidad de análisis:

    ======================================
       Analizador de datos financieros
    ======================================
    ¿Qué tipo de análisis deseas realizar?
    
    1. Análisis de una empresa
    2. Análisis de un activo bursátil
    3. Análisis de información económica

Selecciona una opción:

El usuario selecciona la modalidad deseada, proporciona los parámetros solicitados y recibe los resultados correspondientes.

## Indicadores financieros

El proyecto incorpora diferentes indicadores para evaluar aspectos de la situación financiera de una empresa.

    Indicador

    Fórmula

    Margen neto

    Utilidad neta / Ingresos

    ROA

    Utilidad neta / Activos

    ROE

    Utilidad neta / Patrimonio

    Endeudamiento

    Pasivos / Activos

Estos indicadores permiten estudiar la rentabilidad y estructura financiera de una organización.

## Alcance actual y futuras mejoras

El proyecto se encuentra en desarrollo incremental.

Entre las mejoras contempladas se encuentran:

1. Implementación del análisis de información económica.

2. Ampliación de los indicadores financieros.

3. Incorporación de visualizaciones gráficas.

4. Comparación entre diferentes periodos.

5. Optimización de la estructura y organización del código.

6. Implementación de pruebas para validar los resultados.

## Consideraciones

La disponibilidad de información depende de la fuente de datos utilizada.

Algunos indicadores pueden no calcularse cuando faltan datos financieros necesarios.

Los resultados dependen de la información proporcionada por las fuentes externas.

Este proyecto tiene fines educativos y de análisis de datos; sus resultados no constituyen asesoramiento financiero.

## Autor

PotrilloTJ

Desarrollado como proyecto de programación enfocado en el análisis de datos financieros, la automatización y la aplicación de herramientas computacionales.
