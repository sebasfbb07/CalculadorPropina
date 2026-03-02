def pedir_precio():
    while True: 
        try: 
            precio=float(input("Ingrese el precio de la venta:  "))
            if precio <= 0: 
                print("Su numero debe ser diferente a 0.")
                continue
            else: return precio
        except ValueError:
            print("Ingrese un numero valido.")

        
    return precio 

def mostrar_resultado(propina,total):
    print(f"propina es igual a {propina:.2f}")
    print(f"total a pagar {total:.2f}")

