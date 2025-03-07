from etl_1_extract import extract
from etl_2_transform import transform
from etl_3_load import load
from database import *

def main():
    # print("\033[H\033[J")  # Esta línea limpia la pantalla al inicio del programa
    while True:
        # print("\033[H\033[J")  # Esta línea limpia la pantalla en cada iteración del bucle
        print("Seleccione una opción:")
        print("1. Borrar Modelo")
        print("2. Crear Modelo")
        print("3. Extraer datos")
        print("4. Transformar datos")
        print("5. Cargar datos")
        print("6. Realizar Consultas")
        print("7. Salir")

        option = input("Opción: ")

        if option == "1":
            print("Borrando tablas...")
            drop_tables()
        elif option == "2":
            print("Creando tablas...")
            create_tables()
        elif option == "3":
            df = extract()
        elif option == "4":
            data = transform(df)
        elif option == "5":
            load(data)
        elif option == "6":
            print("Realizando consultas...")
            consultas()
        elif option == "7":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")
            input("Presione Enter para continuar...")
            # print("\033[H\033[J")  # Esta línea limpia la pantalla después de una opción inválida



def consultas():
    print("\033[H\033[J")  # Esta línea limpia la pantalla en cada iteración del bucle
    while True:
        
        print("Seleccione una consulta:")
        print("1. Consulta de todas las tablas")
        print("2. Porcentaje de pasajeros por género")
        print("3. Nacionalidades con su mes año de mayor fecha de salida")
        print("4. COUNT de vuelos por país")
        print("5. Top 5 aeropuertos con mayor número de pasajeros")
        print("6. COUNT dividido por estado de vuelo")
        print("7. Top 5 de los países más visitados")
        print("8. Top 5 de los continentes más visitados")
        print("9. Top 5 de edades dividido por género que más viajan")
        print("10. COUNT de vuelos por MM-YYYY")
        print("11. Volver al menú principal")

        consulta_option = input("Opción: ")

        if consulta_option == "1":
            print("Ejecutando consulta: SELECT COUNT(*) de todas las tablas")
            query_practica(1)
            
        elif consulta_option == "2":
            print("Ejecutando consulta: Porcentaje de pasajeros por género")
            query_practica(2)
        elif consulta_option == "3":
            query_practica(3)
            print("Ejecutando consulta: Nacionalidades con su mes año de mayor fecha de salida")
            # Aquí puedes agregar la lógica para la consulta
        elif consulta_option == "4":
            print("Ejecutando consulta: COUNT de vuelos por país")
            query_practica(4)
            # Aquí puedes agregar la lógica para la consulta
        elif consulta_option == "5":
            print("Ejecutando consulta: Top 5 aeropuertos con mayor número de pasajeros")
            query_practica(5)
            # Aquí puedes agregar la lógica para la consulta
        elif consulta_option == "6":
            print("Ejecutando consulta: COUNT dividido por estado de vuelo")
            query_practica(6)
            # Aquí puedes agregar la lógica para la consulta
        elif consulta_option == "7":
            print("Ejecutando consulta: Top 5 de los países más visitados")
            query_practica(7)
            # Aquí puedes agregar la lógica para la consulta
        elif consulta_option == "8":
            print("Ejecutando consulta: Top 5 de los continentes más visitados")
            query_practica(8)
            # Aquí puedes agregar la lógica para la consulta
        elif consulta_option == "9":
            print("Ejecutando consulta: Top 5 de edades dividido por género que más viajan")
            query_practica(9)
            # Aquí puedes agregar la lógica para la consulta
        elif consulta_option == "10":
            print("Ejecutando consulta: COUNT de vuelos por MM-YYYY")
            query_practica(10)
            # Aquí puedes agregar la lógica para la consulta
        elif consulta_option == "11":
            break
        else:
            print("Opción inválida")
            input("Presione Enter para continuar...")


if __name__ == "__main__":
    main()