import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def extract():
    print("\033[H\033[J")
    
    # Ocultar la ventana principal de Tkinter
    Tk().withdraw()
    
    # Abrir el cuadro de diálogo para seleccionar el archivo
    path = askopenfilename(title="Seleccione el archivo CSV", filetypes=[("CSV files", "*.csv")])
    
    if not path:
        print("No se seleccionó ningún archivo.")
        return 0
    
    try:
        df = pd.read_csv(path)
        print("Número total de registros:", len(df))
        print("\nPrimeras 5 filas:")
        print(df.head())
        input("Presione Enter para continuar...")
        print("\nÚltimas 5 filas:")
        print(df.tail())
        input("Presione Enter para continuar...")
        return df
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        input("Presione Enter para continuar...")
        return 0