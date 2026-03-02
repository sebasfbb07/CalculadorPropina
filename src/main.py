from interfaz.io import pedir_precio, mostrar_resultado
from calculo.propina import calcular_propina, calcular_total
from interfaz.gui import iniciar_gui
def main():
    precio=pedir_precio()
    propina=calcular_propina(precio)
    total=calcular_total(precio, propina)
    mostrar=mostrar_resultado (propina, total)

if __name__ == "__main__":
    iniciar_gui()