velocidad_inicial = float(input("Introduzca su velocidad inicial en m/s:"))
aceleración = float(input("Introduzca su aceleración en m/s^2:"))
posición_inicial = float(input("Introduzca su posición inicial en m:"))
tiempo = float(input("Introduzca el momento exacto en s:"))
posición_final = posición_inicial + (velocidad_inicial * tiempo) + (1/2 * aceleración * (tiempo ** 2))
velocidad_final = velocidad_inicial + aceleración * tiempo
print("Su posición final es",posición_final,"m")
print("Su velocidad final es:",velocidad_final,"m/s")