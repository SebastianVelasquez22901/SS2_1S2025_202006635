
## UNIVERSIDAD SAN CARLOS DE GUATEMALA

## FACULTAD DE INGENIERÍA

## ESCUELA DE CIENCIAS Y SISTEMAS

## LABORATORIO SEMINARIO DE SISTEMAS 2


## Practica 1


>>**Nombre:** Sebastian Alejadro Velasquez Bonilla **Carne:** 202006635


# Descripción del Modelo de Datos

La tabla de hechos `FactFlight` almacena claves foráneas que conectan con las dimensiones y representa los eventos de vuelos. Contiene información clave como el pasajero, aeropuerto de salida y llegada, fecha del vuelo, piloto y estado del vuelo. Esta tabla permite realizar análisis sobre la cantidad de vuelos por pasajero, la frecuencia de vuelos entre aeropuertos y el desempeño de los pilotos.

Las dimensiones complementan la información almacenada en la tabla de hechos. `DimPassenger` contiene datos sobre los pasajeros, como su nombre, género, edad y nacionalidad. `DimDepartureAirport` y `DimArrivalAirport` almacenan información sobre los aeropuertos, incluyendo nombre, país y continente. `DimDepartureDate` desglosa la fecha del vuelo en año, mes y día, lo que facilita consultas temporales. `DimPilot` registra los datos de los pilotos y `DimFlightStatus` categoriza los estados de los vuelos, como "A tiempo", "Retrasado" o "Cancelado".

## Ventajas del Modelo Estrella

![Texto alternativo](image.png)

El modelo estrella es adecuado porque optimiza las consultas analíticas al permitir acceso rápido a los datos sin necesidad de múltiples uniones complejas. Su estructura facilita la generación de reportes y dashboards en herramientas de Business Intelligence. Además, es fácil de mantener y escalar, permitiendo la adición de nuevas dimensiones o métricas sin afectar la estabilidad del sistema. Su simplicidad lo hace ideal para analizar patrones de viaje, evaluar la eficiencia de los aeropuertos y detectar tendencias en el estado de los vuelos.

### Beneficios del Modelo Estrella

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

### Ejemplo de Consultas en el Modelo Estrella

| Consulta | Descripción |
|----------|-------------|
| `SELECT COUNT(*) FROM FactFlight WHERE PassengerID = 'P123';` | Cuenta el número de vuelos de un pasajero específico. |
| `SELECT DepartureAirportID, COUNT(*) FROM FactFlight GROUP BY DepartureAirportID;` | Cuenta el número de vuelos desde cada aeropuerto de salida. |
| `SELECT PilotID, AVG(FlightDuration) FROM FactFlight GROUP BY PilotID;` | Calcula la duración promedio de los vuelos por piloto. |

### Comparación con Otros Modelos

- **Modelo Copo de Nieve:**
  - Más complejo debido a la normalización de las tablas de dimensiones.
  - Puede mejorar el almacenamiento, pero a costa de un rendimiento de consulta más lento.

- **Modelo Galaxia:**
  - Utiliza múltiples tablas de hechos y dimensiones compartidas.
  - Más adecuado para sistemas muy grandes y complejos, pero más difícil de mantener.

### Conclusión

El modelo estrella es una elección óptima para nuestro sistema de análisis de vuelos debido a su simplicidad, rendimiento y facilidad de uso. Permite realizar análisis complejos de manera eficiente y es compatible con las herramientas de Business Intelligence más utilizadas, facilitando la toma de decisiones basada en datos.