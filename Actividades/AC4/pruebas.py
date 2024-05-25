import main

resultados = main.separar_msg_encriptado(
    bytearray(b'\x00\x00\x03\x44\x02\x01\x03\x00\x01\x02\x00\x00\x00\x01\x00\x00\x05')
)

for i in range(1,len(resultados)+1): 
    print(f"Resultado {i}: {resultados[i-1]}")

#print(f"Resultado 1 esperado: {bytearray(b'\x01\x02\x44')}")
#print(f"Resultado 2 esperado: {bytearray(b'\x03\x00\x01\x02\x00')}")
#print(f"Resultado 3 esperado: {bytearray(b'\x00\x00\x01\x00\x00\x05')}")2