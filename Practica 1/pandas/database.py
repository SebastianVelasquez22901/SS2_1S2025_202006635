import pyodbc

# COMPROBAR LA CONEXION CON LA BASE DE DATOS (ESTO ES OPCIONAL) (SQL SERVER)
server = r'LAPTOP-62NCHM64\SQL2022'  # PUEDE SER LOCALHOST O LA IP DE LA MÁQUINA DONDE ESTÁ LA BASE DE DATOS
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};Trusted_Connection=yes;'

def get_connection(database=None):
    try:
        conn_str = connection_string
        if database:
            conn_str += f'DATABASE={database};'
        conn = pyodbc.connect(conn_str, autocommit=True)
        return conn
    except pyodbc.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

def execute_query(query, database=None):
    conn = get_connection(database)
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            print("Operación exitosa")
            return result
        except pyodbc.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None

def drop_tables():
    queries = [
        "ALTER DATABASE SS2_practica1 SET SINGLE_USER WITH ROLLBACK IMMEDIATE;",
        "DROP DATABASE SS2_practica1;"
    ]
    for query in queries:
        execute_query(query)
    print("Base de datos eliminada")

def create_tables():
    # Crear la base de datos
    execute_query("CREATE DATABASE SS2_practica1;")
    
    # Crear las tablas en la base de datos SS2_practica1
    queries = [
        """
        CREATE TABLE DimPassenger (
            PassengerID NVARCHAR(50) COLLATE Latin1_General_CS_AS PRIMARY KEY,
            FirstName NVARCHAR(50),
            LastName NVARCHAR(50),
            Gender NVARCHAR(10),
            Age INT,
            Nationality NVARCHAR(100)
        );
        """,
        """
        CREATE TABLE DimDepartureAirport (
            DepartureAirportID INT PRIMARY KEY,
            AirportName NVARCHAR(200),
            AirportCountryCode NVARCHAR(10),
            CountryName NVARCHAR(100),
            AirportContinent NVARCHAR(10),
            Continents NVARCHAR(100)
        );
        """,
        """
        CREATE TABLE DimArrivalAirport (
            ArrivalAirportID INT PRIMARY KEY,
            AirportName NVARCHAR(10)
        );
        """,
        """
        CREATE TABLE DimDepartureDate (
            DepartureDateID INT PRIMARY KEY,
            Date DATE,
            Year INT,
            Month INT,
            Day INT
        );
        """,
        """
        CREATE TABLE DimPilot (
            PilotID INT PRIMARY KEY,
            PilotName NVARCHAR(100)
        );
        """,
        """
        CREATE TABLE DimFlightStatus (
            FlightStatusID INT PRIMARY KEY,
            FlightStatus NVARCHAR(100)
        );
        """,
        """
        CREATE TABLE FactFlight (
            FactID INT PRIMARY KEY IDENTITY(1,1),
            PassengerID NVARCHAR(50) COLLATE Latin1_General_CS_AS FOREIGN KEY REFERENCES DimPassenger(PassengerID),
            DepartureDateID INT FOREIGN KEY REFERENCES DimDepartureDate(DepartureDateID),
            DepartureAirportID INT FOREIGN KEY REFERENCES DimDepartureAirport(DepartureAirportID),
            ArrivalAirportID INT FOREIGN KEY REFERENCES DimArrivalAirport(ArrivalAirportID),
            PilotID INT FOREIGN KEY REFERENCES DimPilot(PilotID),
            FlightStatusID INT FOREIGN KEY REFERENCES DimFlightStatus(FlightStatusID)
        );
        """
    ]
    for query in queries:
        execute_query(query, database="SS2_practica1")

def query_practica(consulta):
    print(consulta)
    if consulta == 1:
        queries = [
            "SELECT COUNT(*) FROM DimPassenger;",
            "SELECT COUNT(*) FROM DimDepartureAirport;",
            "SELECT COUNT(*) FROM DimArrivalAirport;",
            "SELECT COUNT(*) FROM DimDepartureDate;",
            "SELECT COUNT(*) FROM DimPilot;",
            "SELECT COUNT(*) FROM DimFlightStatus;",
            "SELECT COUNT(*) FROM FactFlight;"
        ]
        
        table_names = [
            "DimPassenger",
            "DimDepartureAirport",
            "DimArrivalAirport",
            "DimDepartureDate",
            "DimPilot",
            "DimFlightStatus",
            "FactFlight"
        ]
        
        for query, table_name in zip(queries, table_names):
            result = execute_query(query, database="SS2_practica1")
            if result:
                print(f"Tabla: {table_name}, Número de filas: {result[0][0]}")
    elif consulta == 2:
        print("Porcentaje de pasajeros por género")
        query = """
        SELECT 
            Gender, 
            COUNT(*) * 100.0 / (SELECT COUNT(*) FROM DimPassenger) AS Percentage
        FROM 
            DimPassenger
        GROUP BY 
            Gender;
        """
        
        result = execute_query(query, database="SS2_practica1")
        if result:
            for row in result:
                print(f"Género: {row[0]}, Porcentaje: {row[1]:.2f}%") 

    elif consulta == 3:
        query = """
        SELECT 
            p.Nationality,
            FORMAT(d.Date, 'MM-yyyy') AS MonthYear,
            COUNT(*) AS Count
        FROM 
            FactFlight f
        JOIN 
            DimPassenger p ON f.PassengerID = p.PassengerID
        JOIN 
            DimDepartureDate d ON f.DepartureDateID = d.DepartureDateID
        GROUP BY 
            p.Nationality, FORMAT(d.Date, 'MM-yyyy')
        ORDER BY 
            p.Nationality, FORMAT(d.Date, 'MM-yyyy');
        """
        
        result = execute_query(query, database="SS2_practica1")
        if result:
            print("Nacionalidad | Mes-Año | Número de salidas")
            for row in result:
                print(f"{row[0]} | {row[1]} | {row[2]}")

    elif consulta == 4:
        query = """
        SELECT 
            da.CountryName AS Country,
            COUNT(*) AS FlightCount
        FROM 
            FactFlight f
        JOIN 
            DimDepartureAirport da ON f.DepartureAirportID = da.DepartureAirportID
        GROUP BY 
            da.CountryName
        ORDER BY 
            FlightCount DESC;
        """
        
        result = execute_query(query, database="SS2_practica1")
        if result:
            print("País | Número de vuelos")
            for row in result:
                print(f"{row[0]} | {row[1]}")

    elif consulta == 5:
        query = """
        SELECT TOP 5 
            da.AirportName AS Airport,
            COUNT(*) AS PassengerCount
        FROM 
            FactFlight f
        JOIN 
            DimDepartureAirport da ON f.DepartureAirportID = da.DepartureAirportID
        GROUP BY 
            da.AirportName
        ORDER BY 
            PassengerCount DESC;
        """
        
        result = execute_query(query, database="SS2_practica1")
        if result:
            print("Aeropuerto | Número de pasajeros")
            for row in result:
                print(f"{row[0]} | {row[1]}")

    elif consulta == 6:
        query = """
        SELECT 
            fs.FlightStatus,
            COUNT(*) AS FlightCount
        FROM 
            FactFlight f
        JOIN 
            DimFlightStatus fs ON f.FlightStatusID = fs.FlightStatusID
        GROUP BY 
            fs.FlightStatus;
        """
        
        result = execute_query(query, database="SS2_practica1")
        if result:
            print("Estado de vuelo | Número de vuelos")
            for row in result:
                print(f"{row[0]} | {row[1]}")
    
    elif consulta == 7:
        query = """
        SELECT TOP 5 
            da.CountryName AS Country,
            COUNT(*) AS VisitCount
        FROM 
            FactFlight f
        JOIN 
            DimDepartureAirport da ON f.DepartureAirportID = da.DepartureAirportID
        GROUP BY 
            da.CountryName
        ORDER BY 
            VisitCount DESC;
        """
        
        result = execute_query(query, database="SS2_practica1")
        if result:
            print("País | Número de visitas")
            for row in result:
                print(f"{row[0]} | {row[1]}")

    elif consulta == 8:
        query = """
        SELECT TOP 5 
            da.Continents AS Continent,
            COUNT(*) AS VisitCount
        FROM 
            FactFlight f
        JOIN 
            DimDepartureAirport da ON f.DepartureAirportID = da.DepartureAirportID
        GROUP BY 
            da.Continents
        ORDER BY 
            VisitCount DESC;
        """
        
        result = execute_query(query, database="SS2_practica1")
        if result:
            print("Continente | Número de visitas")
            for row in result:
                print(f"{row[0]} | {row[1]}")

    elif consulta == 9:
        query = """
        SELECT TOP 5 
            p.Age AS Age,
            p.Gender AS Gender,
            COUNT(*) AS PassengerCount
        FROM 
            FactFlight f
        JOIN 
            DimPassenger p ON f.PassengerID = p.PassengerID
        GROUP BY 
            p.Age, p.Gender
        ORDER BY 
            PassengerCount DESC;
        """
        
        result = execute_query(query, database="SS2_practica1")
        if result:
            print("Edad | Género | Número de pasajeros")
            for row in result:
                print(f"{row[0]} | {row[1]} | {row[2]}")

    elif consulta == 10:
        query = """
        SELECT
            FORMAT(d.Date, 'MM-yyyy') AS MonthYear,
            COUNT(*) AS FlightCount
        FROM
            FactFlight f
        JOIN
            DimDepartureDate d ON f.DepartureDateID = d.DepartureDateID
        GROUP BY
            FORMAT(d.Date, 'MM-yyyy')
        ORDER BY
            MonthYear;
        """

        result = execute_query(query, database="SS2_practica1")
        if result:
            print("Mes-Año | Número de vuelos")
            for row in result:
                print(f"{row[0]} | {row[1]}")
                

# Ejemplo de uso
if __name__ == "__main__":
    drop_tables()
    create_tables()
    query_practica()