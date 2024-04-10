# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=2938

### Variables ###

MY_STRING_VARIABLE = "My String variable"
print(MY_STRING_VARIABLE)

MY_INT_VARIABLE = 5
print(MY_INT_VARIABLE)

MY_INT_TO_STR_VARIABLE = str(MY_INT_VARIABLE)
print(MY_INT_TO_STR_VARIABLE)
print(type(MY_INT_TO_STR_VARIABLE))

MY_BOOL_VARIABLE = False
print(MY_BOOL_VARIABLE)

# Concatenación de variables en un print
print(MY_STRING_VARIABLE, MY_INT_TO_STR_VARIABLE, MY_BOOL_VARIABLE)
print("Este es el valor de:", MY_BOOL_VARIABLE)

# Algunas funciones del sistema
print(len(MY_STRING_VARIABLE))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", 'MoureDev', 35
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)

# Inputs
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)

# Cambiamos su tipo
NAME = 35
AGE = "Brais"
print(name)
print(age)

# ¿Forzamos el tipo?
ADDRESS: str = "Mi dirección"
ADDRESS = True
ADDRESS = 5
ADDRESS = 1.2
print(type(ADDRESS))
