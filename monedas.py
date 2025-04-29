print("Calculadora de distancias")

unidad = input("Dame la unidad ('k' para kilómetros, 'a' para millas, 'm' para metros): ").lower()
if unidad not in ['k', 'a', 'm']:
    print("Opción de unidad no válida. Terminando el programa.")
    exit()

tipo = input("Dame la métrica ('t' para taxi, 'e' para euclídea, 'm' para distancia del máximo): ").lower()
if tipo not in ['t', 'e', 'm']:
    print("Tipo de distancia no válido. Terminando el programa.")
    exit()

x1 = float(input("Dame el primer punto de x: "))
y1 = float(input("Dame el primer punto de y: "))
x2 = float(input("Dame el segundo punto de x: "))
y2 = float(input("Dame el segundo punto de y: "))

if tipo == 't':
    distancia = abs(x1 - x2) + abs(y1 - y2)
elif tipo == 'e':
    distancia = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
else:
    distancia = max(abs(x1 - x2), abs(y1 - y2))

if unidad == 'k':
    distancia *= 1000
elif unidad == 'a':
    distancia *= 1609.34

print(f"La distancia entre los puntos es de {distancia:.2f} metros :)")
