import pandas as pd

def transform(df):
    print("\033[H\033[J")
    
    # Normalizar fechas al formato 'YYYY-MM-DD'
    def parse_dates(date_str):
        for fmt in ('%m/%d/%Y', '%m-%d-%Y'):
            try:
                return pd.to_datetime(date_str, format=fmt)
            except ValueError:
                continue
        return pd.NaT

    df['Departure Date'] = df['Departure Date'].apply(parse_dates)

    # Crear dimensión de fechas de salida
    dim_departure_date = df[['Departure Date']].drop_duplicates()
    dim_departure_date['DepartureDateID'] = range(1, len(dim_departure_date) + 1)
    dim_departure_date['Year'] = dim_departure_date['Departure Date'].dt.year
    dim_departure_date['Month'] = dim_departure_date['Departure Date'].dt.month
    dim_departure_date['Day'] = dim_departure_date['Departure Date'].dt.day
    
    print("DimDepartureDate:")
    print(dim_departure_date.head())
    input("Presione Enter para continuar...")

    # Crear dimensión de aeropuertos de llegada
    dim_arrival_airport = df[['Arrival Airport']].drop_duplicates()
    dim_arrival_airport['ArrivalAirportID'] = range(1, len(dim_arrival_airport) + 1)
    
    # Crear dimensión de pilotos
    dim_pilot = df[['Pilot Name']].drop_duplicates()
    dim_pilot['PilotID'] = range(1, len(dim_pilot) + 1)
    
    # Crear dimensión de estados de vuelo
    dim_flight_status = df[['Flight Status']].drop_duplicates()
    dim_flight_status['FlightStatusID'] = range(1, len(dim_flight_status) + 1)
    print('Flight Status:', dim_flight_status)
    input("Presione Enter para continuar...")

    # Crear dimensión de aeropuertos de salida
    dim_departure_airport = df[['Airport Name', 'Airport Country Code', 'Country Name', 'Airport Continent', 'Continents']].drop_duplicates()
    dim_departure_airport['DepartureAirportID'] = range(1, len(dim_departure_airport) + 1)
    dim_departure_airport = dim_departure_airport.drop_duplicates(subset=['Airport Name'])

    print(dim_departure_airport['Airport Name'].duplicated().sum())  # Debe ser 0
    input("Presione Enter para continuar...")

    # Crear dimensión de pasajeros
    dim_passenger = df[['Passenger ID', 'First Name', 'Last Name', 'Gender', 'Age', 'Nationality']].drop_duplicates()
    
    # Relacionar tabla de hechos con dimensiones
    df['DepartureDateID'] = df['Departure Date'].map(dim_departure_date.set_index('Departure Date')['DepartureDateID'])
    df['ArrivalAirportID'] = df['Arrival Airport'].map(dim_arrival_airport.set_index('Arrival Airport')['ArrivalAirportID'])
    df['PilotID'] = df['Pilot Name'].map(dim_pilot.set_index('Pilot Name')['PilotID'])
    df['FlightStatusID'] = df['Flight Status'].map(dim_flight_status.set_index('Flight Status')['FlightStatusID'])
    df['DepartureAirportID'] = df['Airport Name'].map(dim_departure_airport.set_index('Airport Name')['DepartureAirportID'])
    
    # Crear tabla de hechos
    fact_flight = df[['Passenger ID', 'DepartureDateID', 'ArrivalAirportID', 'PilotID', 'FlightStatusID', 'DepartureAirportID']]
    
    # Verificar datos
    print("DimPassenger:")
    print(dim_passenger.head())
    print("Número total de registros:", len(dim_passenger))
    input("Presione Enter para continuar...")
    print("DimDepartureDate:")
    print(dim_departure_date.head())
    print("Número total de registros:", len(dim_departure_date))
    input("Presione Enter para continuar...")
    print("DimArrivalAirport:")
    print(dim_arrival_airport.head())
    print("Número total de registros:", len(dim_arrival_airport))
    input("Presione Enter para continuar...")
    print("DimPilot:")
    print(dim_pilot.head())
    print("Número total de registros:", len(dim_pilot))
    input("Presione Enter para continuar...")
    print("DimFlightStatus:")
    print(dim_flight_status.head())
    print("Número total de registros:", len(dim_flight_status))
    input("Presione Enter para continuar...")
    print("DimDepartureAirport:")
    print(dim_departure_airport.head())
    print("Número total de registros:", len(dim_departure_airport))
    input("Presione Enter para continuar...")
    print("FactFlight:")
    print(fact_flight.head())
    print("Número total de registros:", len(fact_flight))
    input("Presione Enter para continuar...")
    
    return [dim_passenger, dim_departure_date, dim_departure_airport, dim_arrival_airport, dim_pilot, dim_flight_status, fact_flight]