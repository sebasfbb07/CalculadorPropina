def calcular_propina(precio):
    if precio <20:
        porcentaje= 0.10
    elif precio <= 50:
        porcentaje= 0.15
    else:
        porcentaje=0.20
        
    return precio * porcentaje

def calcular_total(precio, propina):
    return precio+propina 
