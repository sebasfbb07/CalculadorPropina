# 💰 Calculadora de Propinas

Proyecto desarrollado en Python que calcula la propina y el total a pagar en un restaurante según el monto de la cuenta.

---

## 📌 Descripción

Este programa solicita al usuario el precio de su consumo en un restaurante y calcula automáticamente:

- El porcentaje de propina según el monto
- El valor de la propina
- El total final a pagar

Además, incluye validación de datos usando `try/except` para evitar errores si el usuario ingresa valores inválidos.

---

## 🧮 Reglas de Cálculo

| Precio de la Cuenta | Porcentaje de Propina |
|---------------------|----------------------|
| Menor a 20          | 10%                  |
| Entre 20 y 50       | 15%                  |
| Mayor a 50          | 20%                  |

---

## 📂 Estructura del Proyecto
CalculadorPropina/
│
├── src/
│ ├── main.py
│ │
│ ├── calculo/
│ │ └── propina.py
│ │
│ └── interfaz/
│ └── io.py
│
└── README.md
### 🔹 main.py
Punto de entrada del programa.  
Coordina la ejecución llamando a las funciones necesarias.

### 🔹 calculo/propina.py
Contiene la lógica del negocio:
- Cálculo del porcentaje
- Cálculo del total

### 🔹 interfaz/io.py
Se encarga de:
- Solicitar datos al usuario
- Validar entradas
- Mostrar resultados

---

## 🚀 Cómo Ejecutarlo

1. Abrir la terminal.
2. Ir a la carpeta `src`:

```bash
cd src
🛡 Manejo de Errores

El programa utiliza:

try/except para capturar errores de tipo ValueError

Validación para evitar números negativos o iguales a 0

while True para repetir la entrada hasta que sea válida

🎯 Objetivo del Proyecto

Este proyecto fue desarrollado como práctica para aprender:

Arquitectura modular en Python

Separación de responsabilidades

Uso de funciones (def, return)

Manejo de errores (try/except)

Organización en carpetas

Buenas prácticas de programación

🧠 Autor

Sebastián Bernal
Estudiante en formación de desarrollo en Python.



