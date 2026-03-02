import tkinter as tk
from calculo.propina import calcular_propina, calcular_total

def iniciar_gui():
    def calcular():
        try:
            precio = float(entry_precio.get())

            if precio <= 0:
                resultado_label.config(text="El precio debe ser mayor que 0.")
                return

            propina = calcular_propina(precio)
            total = calcular_total(precio, propina)

            resultado_label.config(
                text=f"Propina: {propina:.2f}\nTotal: {total:.2f}"
            )

        except ValueError:
            resultado_label.config(text="Ingrese un número válido.")

    ventana = tk.Tk()
    ventana.title("Calculadora de Propina")
    ventana.geometry("300x250")

    tk.Label(ventana, text="Ingrese el precio:").pack(pady=10)

    entry_precio = tk.Entry(ventana)
    entry_precio.pack()

    tk.Button(ventana, text="Calcular", command=calcular).pack(pady=10)

    resultado_label = tk.Label(ventana, text="")
    resultado_label.pack(pady=10)

    ventana.mainloop()