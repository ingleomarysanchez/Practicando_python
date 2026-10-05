
 #*  Billetes y monedas


# TODOD: ENTRADA
monto = float(input("Ingrese el monto: "))

# Convertimos todo a centavos sumando 0.0001 Porque los números con decimales 
# (float) no son exactos en Python, y // y % con decimales pueden dar resultados equivocados.

centavos = int(monto * 100 + 0.0001)

#  TODO: PROCESO  (BILLETES)
b100 = centavos // 10000
centavos = centavos % 10000
b50 = centavos // 5000
centavos = centavos % 5000
b20 = centavos // 2000
centavos = centavos % 2000
b10 = centavos // 1000
centavos = centavos % 1000
b5 = centavos // 500
centavos = centavos % 500
b2 = centavos // 200
centavos = centavos % 200

#  TODO:  PROCESO - (monedas)
m100 = centavos // 100
centavos = centavos % 100
m50 = centavos // 50
centavos = centavos % 50
m25 = centavos // 25
centavos = centavos % 25
m10 = centavos // 10
centavos = centavos % 10
m5 = centavos // 5
centavos = centavos % 5
m1 = centavos // 1

# TODO:  SALIDA  


print("Billetes:")
print(f"Billetes de 100: {b100}")
print(f"Billetes de 50: {b50}")
print(f"Billetes de 20: {b20}")
print(f"Billetes de 10: {b10}")
print(f"Billetes de 5: {b5}")
print(f"Billetes de 2: {b2}")

print("Monedas:")
print(f"Monedas de 1.00: {m100}")
print(f"Monedas de 0.50: {m50}")
print(f"Monedas de 0.25: {m25}")
print(f"Monedas de 0.10: {m10}")
print(f"Monedas de 0.05: {m5}")
print(f"Monedas de 0.01: {m1}")

