s = "Hola ahi! Que debe ser esta cadena?"

# Longitud debe ser 35
print("Longitud de s = %d" % len(s))

# Primer evento de "a" deberá estar en el lugar 3
print("Primer evento de la letra a = %d" % s.index("a"))

# El número de a's deberá ser 5
print("a ocurre %d veces" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5])  # Start to 5)
print("The next five characters are '%s'" % s[5:10])  # 5 to 10)
print("The thirteenth character is '%s'" % s[12])  # Just number 12)

print("The last five characters are '%s'" % s[-5:])  # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Hol"):
    print("String starts with 'Hol'. Good!")

# Check how a string ends
if s.endswith("ena?"):
    print("String ends with 'ena?!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split("3"))

# SEGUNDO EJERCISIO
# Cambia las variables de la primera sección, tanto que el código en la sección se ejecute a través de un if

# cambia este codigo
number = 10
second_number = 10
first_array = [4, 5, 9]
second_array = [1, 3]

if number < 15:
    print("1")

if first_array == [4, 5, 9]:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[1] == 5:
    print("5")

if not second_number == 2:
    print("6")

# TERCER

NUMBERS = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
i = NUMBERS
for i in NUMBERS:
    if i > 7:
        continue
    if i % 2 == 0:
        break
    print(i)


    def mensaje():
        print(
            "codigo mas organizado" " " "codigo mas facil de leer" " " "reuso de codigo mas facil" " " "permitir a los programadores compartir codigo y compartilo")
