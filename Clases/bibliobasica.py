import math

# Mi solución
def factorial(n):
    fact = n
    i = 1

    if n < 2:
        return 1

    while i < n:
        fact *= n - i
        i += 1

    return fact
    

def distancia(r, theta, z):
    """Función para calcular la distancia al origen.
    Funciona siempre y cuando el ángulo no esté en radianes.
    """
    theta_rad = (theta * math.pi) / 180
    
    x = r * math.sin(theta_rad)
    y = r * math.cos(theta_rad)

    return math.sqrt(x ** 2 + y ** 2 + z ** 2)