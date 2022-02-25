
#Declaración de variables
x = math.pi/8
n = 0
iteraciones = 1
aproximacion_actual = None
aproximacion_anterior = None
nivel_de_tolerancia = 0.5 * 10**-1
print(f"Niverl de tolerancia: {nivel_de_tolerancia}\n\n")

while True:
    
    #Obteniendo solamente aproximación actual en la primer iteración
    if iteraciones == 1:
        aproximacion_actual = x**(2*n+1)/math.fabs((2*n)+1)
        print(f"Iteración: {iteraciones}\nAproximación: {aproximacion_actual}\nNivel de tolerancia: {nivel_de_tolerancia}\n\n")
        n += 1
        iteraciones += 1
        continue
    #Obteniendo ambas aproximaciones para sacar el error aproximado desde la segunda iteración
    else:
        aproximacion_anterior = aproximacion_actual
        aproximacion_actual = aproximacion_anterior + (x**(2*n+1)/math.fabs((2*n)+1))
        error_aproximado = math.fabs((aproximacion_actual - aproximacion_anterior)/aproximacion_actual)*100
        print(f"Iteración: {iteraciones}\nAproximación: {aproximacion_actual}\nNivel de tolerancia: {nivel_de_tolerancia}\nError aproximado: {error_aproximado}\n\n")

        #Comprobando criterio de break
        if  error_aproximado < nivel_de_tolerancia:
            break
        else:
            iteraciones += 1
            n += 1

print(f"La solucion es: {aproximacion_actual}")
