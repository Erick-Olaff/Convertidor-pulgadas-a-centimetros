# Paso 1: Solicitar al usuario las medidas de las piezas del mueble en cms
medida_en_cms = float(input("Por favor, ingresa las medidas de las piezas del mueble en centimetros: "))

# Paso 2: Convertir las medidas de centimetros a pulgadas
medida_en_pulgadas = medida_en_cms / 2.54

# Paso 3: Mostrar las medidas en pulgadas al usuario
print("Las medidas en pulgadas de las piezas del mueblo son: ", medida_en_pulgadas)