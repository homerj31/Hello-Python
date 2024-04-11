# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###

MY_STRING = "Mi String"
MY_OTHER_STRING = 'Mi otro String'

print(len(MY_STRING))
print(len(MY_OTHER_STRING))
print(MY_STRING + " " + MY_OTHER_STRING)

MY_NEW_LINE_STRING = "Este es un String\ncon salto de línea"
print(MY_NEW_LINE_STRING)

MY_TAB_STRING = "\tEste es un String con tabulación"
print(MY_TAB_STRING)

MY_SCAPE_STRING = "\\tEste es un String \\n escapado"
print(MY_TAB_STRING)

# Formateo

name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres

LANGUAGE = "python"
A, B, C, D, E, F = LANGUAGE
print(A)
print(E)

# División

LANGUAGE_SLICE = LANGUAGE[1:3]
print(LANGUAGE_SLICE)

LANGUAGE_SLICE = LANGUAGE[1:]
print(LANGUAGE_SLICE)

LANGUAGE_SLICE = LANGUAGE[-2]
print(LANGUAGE_SLICE)

LANGUAGE_SLICE = LANGUAGE[0:6:2]
print(LANGUAGE_SLICE)

# Reverse

REVERSED_LANGUAGE = LANGUAGE[::-1]
print(REVERSED_LANGUAGE)

# Funciones del lenguaje

print(LANGUAGE.capitalize())
print(LANGUAGE.upper())
print(LANGUAGE.count("t"))
print(LANGUAGE.isnumeric())
print("1".isnumeric())
print(LANGUAGE.lower())
print(LANGUAGE.lower().isupper())
print(LANGUAGE.startswith("Py"))
print("Py" == "py")  # No es lo mismo
