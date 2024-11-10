import numpy as np

def clasificar_vehiculo(nivel_individual_dB, tipo_vehiculo):
    """
    Clasifica el sonido de cada vehículo según su tipo y nivel de ruido en decibelios.
    
    Parámetros:
    - nivel_individual_dB: El nivel de sonido de cada vehículo en decibelios.
    - tipo_vehiculo: El tipo de vehículo (por ejemplo: 'moto', 'automovil', 'camion', etc.).
    
    Devuelve:
    - Una cadena que indica si el vehículo es poco ruidoso, ruidoso, molesto o insoportable.
    """
    # Clasificación personalizada basada en el tipo de vehículo
    if tipo_vehiculo == "moto":
        rango_ruido = np.random.randint(75, 86)  # Motos son más ruidosas
    elif tipo_vehiculo == "automovil":
        rango_ruido = np.random.randint(65, 76)  # Automóviles son más silenciosos
    elif tipo_vehiculo == "taxi":
        rango_ruido = np.random.randint(70, 81)  # Taxis son similares a los autos pero más usados
    elif tipo_vehiculo == "camion":
        rango_ruido = np.random.randint(80, 91)  # Camiones generan más ruido
    elif tipo_vehiculo == "bus":
        rango_ruido = np.random.randint(85, 96)  # Buses son los más ruidosos
    else:
        rango_ruido = 70  # Por defecto, asignamos 70 dB para vehículos desconocidos

    if nivel_individual_dB < 50:
        return "Poco ruidoso"
    elif 50 <= nivel_individual_dB < 65:
        return "Ruidoso"
    elif 65 <= nivel_individual_dB < 80:
        return "Molesto"
    else:
        return "Insoportable"

def calcular_sonido_total(vehiculos, tipos_vehiculos):
    """
    Calcula el nivel total de sonido generado por varios vehículos, y clasifica cada uno.
    
    Parámetros:
    - vehiculos: Número total de vehículos.
    - tipos_vehiculos: Lista con los tipos de cada vehículo ('moto', 'automovil', 'camion', etc.).
    
    Devuelve:
    - El nivel total de sonido en decibelios y las clasificaciones de cada vehículo.
    """
    # Inicializamos la suma de intensidades
    intensidades_totales = 0
    clasificaciones = []
    
    # Clasificamos cada vehículo y sumamos su intensidad
    for tipo in tipos_vehiculos:
        # Generamos el ruido de cada vehículo de acuerdo a su tipo
        nivel_ruido = np.random.randint(65, 95)  # Nivel de ruido base para cualquier tipo de vehículo
        clasificacion = clasificar_vehiculo(nivel_ruido, tipo)
        clasificaciones.append(f"{tipo.capitalize()}: {clasificacion} (Nivel de sonido: {nivel_ruido} dB)")
        
        # Convertir el nivel de dB a intensidad lineal
        intensidad_individual = 10 ** (nivel_ruido / 10)
        intensidades_totales += intensidad_individual
    
    # Convertir la intensidad total de vuelta a decibelios
    nivel_total_dB = 10 * np.log10(intensidades_totales)
    
    return nivel_total_dB, clasificaciones

# Parámetros de entrada
numero_vehiculos = int(input("Introduce el número de vehículos en el tráfico: "))

# Generamos una lista de tipos de vehículos (puedes ajustar esto o permitir la entrada del usuario)
tipos_vehiculos = np.random.choice(['moto', 'automovil', 'taxi', 'camion', 'bus'], size=numero_vehiculos)

# Calculamos el nivel total de sonido y las clasificaciones de los vehículos
nivel_total, clasificaciones = calcular_sonido_total(numero_vehiculos, tipos_vehiculos)

# Mostrar resultados
print(f"\nNivel total de sonido generado por {numero_vehiculos} vehículos es: {nivel_total:.2f} dB\n")
print("Clasificación de los vehículos por tipo y nivel de sonido:")
for clasificacion in clasificaciones:
    print(clasificacion)

# Clasificación global del ambiente
def clasificar_ambiente(nivel_total_dB):
    """
    Clasifica el ambiente global según el nivel total de sonido.
    
    Parámetros:
    - nivel_total_dB: El nivel total de sonido en decibelios.
    
    Devuelve:
    - Una cadena que indica si el ambiente es poco ruidoso, ruidoso, molesto o insoportable.
    """
    if nivel_total_dB < 50:
        return "Ambiente poco ruidoso"
    elif 50 <= nivel_total_dB < 65:
        return "Ambiente ruidoso"
    elif 65 <= nivel_total_dB < 80:
        return "Ambiente molesto"
    else:
        return "Ambiente insoportable"

# Clasificar el ambiente global
clasificacion_global = clasificar_ambiente(nivel_total)

# Mostrar la clasificación global del ambiente
print(f"\nClasificación global del ambiente: {clasificacion_global}")
