from datetime import datetime

# Obtener la fecha de nacimiento del usuario (en formato YYYY-MM-DD)
fecha_nacimiento = input("Ingresa tu fecha de nacimiento (YYYY-MM-DD): ")

# Convertir la fecha de nacimiento en un objeto datetime
fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')

# Obtener la fecha actual
fecha_actual = datetime.now()

# Calcular la edad actual
diferencia_edad = fecha_actual - fecha_nacimiento
edad_años = diferencia_edad.days // 365

# Verificar si ya tienes 80 años o más
if edad_años >= 80:
    print("¡Estás en tiempo extra!")

else:
    # Calcular la fecha objetivo (80 años desde la fecha de nacimiento)
    fecha_objetivo = fecha_nacimiento.replace(year=fecha_nacimiento.year + 80)

    # Calcular la diferencia de tiempo hasta la fecha objetivo
    diferencia_tiempo = fecha_objetivo - fecha_actual

    # Calcular años, meses, días, horas, minutos y segundos restantes
    años_restantes = diferencia_tiempo.days // 365
    meses_restantes = (diferencia_tiempo.days % 365) // 30
    dias_restantes = (diferencia_tiempo.days % 365) % 30
    horas_restantes, segundos_restantes = divmod(diferencia_tiempo.seconds, 3600)
    minutos_restantes, segundos_restantes = divmod(segundos_restantes, 60)

    # Mostrar la edad actual y el tiempo restante
    print(f"Tienes {edad_años} años.")
    print(f"Te quedan aproximadamente {años_restantes} años, {meses_restantes} meses, {dias_restantes} días, {horas_restantes} horas, {minutos_restantes} minutos y {segundos_restantes} segundos hasta los 80 años de vida.")
