# rebotes.py
#nota:
# Una pelota de goma es arrojada desde una altura de 100 metros 
# y cada vez que toca el piso salta 3/5 de la altura desde la que cayó.
# cuales son las alturas que alcanza en cada uno de sus primeros diez rebotes.
#altura de 100 metros, calculada en un rango de diez rebotes, siendo 
#cada nueva altura igual a 3/5 de la alcanzada en el rebote anterior.
# Archivo de ejemplo
# Ejercicio
altura = 100
for i in range(10):
    altura *= (3/5)
    print(round(altura,4))
    