
## UNIVERSIDAD SAN CARLOS DE GUATEMALA

## FACULTAD DE INGENIERÍA

## ESCUELA DE CIENCIAS Y SISTEMAS

## LABORATORIO SEMINARIO DE SISTEMAS 2


## Practica 1


>>**Nombre:** Sebastian Alejadro Velasquez Bonilla **Carne:** 202006635




## Introducción

Este documento describe el proceso ETL (Extracción, Transformación y Carga) implementado para el análisis de datos de vuelos. Utilizamos Python 3.12 y SQL Server como base de datos para nuestro Data Warehouse.

## Extracción

* La extracción de datos implica obtener los datos de las fuentes originales de manera eficiente sin afectar el rendimiento de los sistemas operacionales. Los datos pueden ser extraídos de bases de datos relacionales, aplicaciones, servicios web, entre otros.

## Transformación

* Durante la transformación, los datos se limpian, convierten a un formato estándar y enriquecen para que sean consistentes y útiles en el sistema de destino. Esto incluye operaciones como la `validación de datos`, la `agregación`, la `normalización`, entre otros.

### Consideraciones para la Transformación:

* **Filtrado de Datos Innecesarios:** Eliminar datos que no son relevantes para el análisis.
* **Corrección de Errores y Limpieza de Datos:** Identificar y corregir errores en los datos.
* **Normalización y Estandarización de Datos:** Asegurar que los datos sigan un formato consistente.
* **Conversión de Tipos de Datos:** Convertir los datos a los tipos adecuados para el análisis.
* **Enriquecimiento de Datos:** Agregar información adicional para mejorar el análisis.
* **Agregación de Datos:** Resumir los datos para facilitar el análisis.
* **Creación de Cálculos Derivados:** Generar nuevas métricas a partir de los datos existentes.
* **Transformación de Formatos:** Cambiar el formato de los datos para que sean compatibles con el sistema de destino.
* **Validación de Datos Transformados:** Verificar que los datos transformados sean correctos y completos.
* **Preparación para la Carga:** Asegurar que los datos estén listos para ser cargados en el sistema de destino.

## Carga

* La carga implica insertar los datos transformados en la base de datos destino o en el almacén de datos. Dependiendo de la naturaleza del proceso, puede ser una carga `completa` (todos los datos se cargan de nuevo) o `incremental` (solo los nuevos o modificados).

## Ejemplo ETL

Para estos ejemplos utilizaremos `Pandas` debido al uso de `Python` como lenguaje, además se utilizará `SQL Server` como almacenamiento de nuestro `Data Warehouse`. Con esto en cuenta, debemos instalar las siguientes librerías con los siguientes comandos:

```sh
pip install pandas pyodbc tqdm
```

Si deseas instalarlas individualmente, usa:

```sh
pip install pandas
pip install pyodbc
pip install tqdm
```

### Descripción de cada librería y alternativas

1. **pandas**
   - **Uso:** Manejo y análisis de datos estructurados en formato de tablas (DataFrames y Series). Se utiliza en ciencia de datos, análisis financiero y procesamiento de datos.
   - **Alternativas:**
     - **Polars:** Más rápido y eficiente en memoria que pandas, especialmente para grandes volúmenes de datos.
     - **Dask:** Permite procesar grandes conjuntos de datos de manera distribuida y en paralelo.
     - **Vaex:** Especialmente diseñado para manejar grandes volúmenes de datos sin cargar todo en memoria.

2. **pyodbc**
   - **Uso:** Conectar Python con bases de datos que soportan ODBC, como SQL Server, MySQL y PostgreSQL. Se utiliza en desarrollo de aplicaciones y análisis de datos.
   - **Alternativas:**
     - **SQLAlchemy:** Proporciona una capa de abstracción para trabajar con bases de datos relacionales.
     - **psycopg2:** Especializado en conexiones con PostgreSQL, ofreciendo un mejor rendimiento.
     - **mysql-connector-python:** Cliente nativo de MySQL para una integración más fluida con esta base de datos.

3. **tqdm**
   - **Uso:** Mostrar barras de progreso en loops y procesos iterativos, útil en procesamiento de datos y machine learning.
   - **Alternativas:**
     - **alive-progress:** Más personalizable y con efectos visuales avanzados.
     - **progressbar2:** Ofrece múltiples estilos de barra y soporte para diferentes entornos.
     - **rich:** Además de barras de progreso, permite imprimir texto con colores y formatos enriquecidos en la terminal.

## Variaciones y consideraciones

Primero se debe elegir qué modelo se va a implementar para almacenar los datos extraídos del `.csv`.

### Encabezados del Archivo Original
```plaintext
Passenger ID, First Name, Last Name, Gender, Age, Nationality, Airport Name, Airport Country Code, Country Name, Airport Continent, Continents, Departure Date, Arrival Airport, Pilot Name, Flight Status
```

### Modelo Estrella

El modelo estrella es una elección óptima para nuestro sistema de análisis de vuelos debido a su simplicidad, rendimiento y facilidad de uso. Permite realizar análisis complejos de manera eficiente y es compatible con las herramientas de Business Intelligence más utilizadas, facilitando la toma de decisiones basada en datos.

#### Ventajas del Modelo Estrella

- **Rendimiento de Consultas:**
  - Las consultas en un modelo estrella son más rápidas debido a la simplicidad de las uniones entre la tabla de hechos y las tablas de dimensiones.
  - Las tablas de dimensiones suelen ser más pequeñas y pueden ser almacenadas en memoria, lo que acelera el acceso a los datos.

- **Facilidad de Uso:**
  - La estructura del modelo estrella es intuitiva y fácil de entender para los usuarios finales.
  - Los analistas de datos pueden escribir consultas SQL de manera más sencilla y eficiente.

- **Escalabilidad:**
  - Es fácil agregar nuevas dimensiones o métricas sin afectar la estructura existente.
  - Permite la expansión del modelo para incluir más datos y análisis sin una reestructuración significativa.

- **Compatibilidad con Herramientas de BI:**
  - La mayoría de las herramientas de Business Intelligence están optimizadas para trabajar con modelos estrella.
  - Facilita la creación de dashboards y reportes interactivos.

#### Ejemplo de Consultas en el Modelo Estrella

| Consulta | Descripción |
|----------|-------------|
| `SELECT COUNT(*) FROM FactFlight WHERE PassengerID = 'P123';` | Cuenta el número de vuelos de un pasajero específico. |
| `SELECT DepartureAirportID, COUNT(*) FROM FactFlight GROUP BY DepartureAirportID;` | Cuenta el número de vuelos desde cada aeropuerto de salida. |
| `SELECT PilotID, AVG(FlightDuration) FROM FactFlight GROUP BY PilotID;` | Calcula la duración promedio de los vuelos por piloto. |

#### Comparación con Otros Modelos

- **Modelo Copo de Nieve:**
  - Más complejo debido a la normalización de las tablas de dimensiones.
  - Puede mejorar el almacenamiento, pero a costa de un rendimiento de consulta más lento.

- **Modelo Galaxia:**
  - Utiliza múltiples tablas de hechos y dimensiones compartidas.
  - Más adecuado para sistemas muy grandes y complejos, pero más difícil de mantener.

### Conclusión

El modelo estrella es una elección óptima para nuestro sistema de análisis de vuelos debido a su simplicidad, rendimiento y facilidad de uso. Permite realizar análisis complejos de manera eficiente y es compatible con las herramientas de Business Intelligence más utilizadas, facilitando la toma de decisiones basada en datos.