import tkinter as tk
print("hola mundo")
def calcular_temperatura():
    """
    Obtiene el valor de la entrada, lo convierte y actualiza la salida.
    """
    try:
        # 1. Obtiene el texto de la entrada y lo convierte a float
        celsius = float(entrada_celsius.get())
        
        # 2. Calcula la temperatura en Fahrenheit
        fahrenheit = (celsius * 9/5) + 32
        
        # 3. Actualiza la etiqueta de salida con el resultado formateado a 2 decimales
        etiqueta_resultado.config(text=f"{fahrenheit:.2f} °F")

    except ValueError:
        # 4. Si la conversión falla, muestra un mensaje de error claro
        etiqueta_resultado.config(text="Error: Introduce un número válido")

# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.geometry("300x200")
ventana.title("Conversor de Temperatura")
ventana.resizable(False, False)

# --- Creación de los Widgets ---
etiqueta_instruccion = tk.Label(ventana, text="Introduce los grados Celsius:")
entrada_celsius = tk.Entry(ventana, width=15, font=("Arial", 12))
boton_convertir = tk.Button(ventana, text="Convertir a Fahrenheit", command=calcular_temperatura)
etiqueta_resultado = tk.Label(ventana, text="Resultado en °F", font=("Arial", 14, "bold"))

# --- Colocación de los Widgets en la Ventana ---
etiqueta_instruccion.pack(pady=5)
entrada_celsius.pack(pady=5)
boton_convertir.pack(pady=10)
etiqueta_resultado.pack(pady=5)

# --- Iniciar la Aplicación ---
ventana.mainloop()