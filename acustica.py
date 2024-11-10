def velocidad_sonido_aire(temperatura):
    """
    Calcula la velocidad del sonido en el aire en m/s dado la temperatura en grados Celsius.
    """
    return 331.3 + 0.6 * temperatura

def velocidad_sonido_agua(temperatura):
    """
    Calcula la velocidad del sonido en el agua en m/s dado la temperatura en grados Celsius.
    """
    return 1482 + 4.3 * temperatura

def velocidad_sonido_acero():
    """
    Calcula la velocidad del sonido en el acero en m/s (aproximadamente constante).
    """
    return 5000

def calcular_velocidad(medio, temperatura=None):
    """
    Calcula la velocidad del sonido en un medio dado.
    :param medio: 'aire', 'agua', 'acero'
    :param temperatura: Temperatura en grados Celsius (necesaria solo para aire y agua)
    :return: Velocidad del sonido en m/s
    """
    if medio == 'aire':
        if temperatura is None:
            raise ValueError("Se requiere la temperatura para calcular la velocidad del sonido en el aire.")
        return velocidad_sonido_aire(temperatura)
    
    elif medio == 'agua':
        if temperatura is None:
            raise ValueError("Se requiere la temperatura para calcular la velocidad del sonido en el agua.")
        return velocidad_sonido_agua(temperatura)
    
    elif medio == 'acero':
        return velocidad_sonido_acero()
    
    else:
        raise ValueError("Medio no reconocido. Usa 'aire', 'agua' o 'acero'.")

# Ejemplo de uso
if __name__ == "__main__":
    medio = input("Introduce el medio (aire, agua, acero): ").strip().lower()

    if medio in ['aire', 'agua']:
        temperatura = float(input("Introduce la temperatura en grados Celsius: "))
        velocidad = calcular_velocidad(medio, temperatura)
        print(f"La velocidad del sonido en {medio} a {temperatura} °C es: {velocidad:.2f} m/s")
    
    elif medio == 'acero':
        velocidad = calcular_velocidad(medio)
        print(f"La velocidad del sonido en el acero es: {velocidad} m/s")
    
    else:
        print("Medio no válido. Debes elegir entre 'aire', 'agua' o 'acero'.")
