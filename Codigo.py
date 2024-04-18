import math

# Definir pi con 6 decimales
PI = math.pi * 1000000 / 1000000

def calcular_circunferencia(radio_cm):
    """Calcular la circunferencia de un círculo dado su radio en centímetros.

    Parámetros:
    radio_cm (float): El radio del círculo en centímetros.

    Retorna:
    float: La circunferencia del círculo en centímetros.
    """
    radio_m = radio_cm / 100  # Convertir centímetros a metros
    circunferencia = 2 * PI * radio_m
    circunferencia_cm = circunferencia * 100  # Convertir metros a centímetros
    return circunferencia_cm

# Probar la función con diferentes valores de radio en centímetros
for radio_cm in [3, 8, 10]:
    print(f"La circunferencia de un círculo con radio {radio_cm} cm es {calcular_circunferencia(radio_cm)} cm")
