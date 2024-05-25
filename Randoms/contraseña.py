# Variables iniciales

nombre = input("Nombre: ")
nombre_mascota = input("Nombre de su mascota: ")

#loop principal
contraseña_invalida = True
while contraseña_invalida:

    #Recibe input
    propuesta = input("Contraseña propuesta (FIN para terminar): ")

    #Condicion para salir del loop 
    if propuesta == "FIN":
        break

    #verifica minuscula 
    tiene_minuscula = False
    for caracter in propuesta: 
        if caracter in "abcdefghijklmnñopqrstuvwxyzáéíóú":
            tiene_minuscula = True

    # Se copia procedimiento anterior pero con mayusculas
    tiene_mayuscula = False
    for caracter in propuesta: 
        if caracter in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ":
            tiene_mayuscula = True

    # Se copia procedimiento anterior pero con numeros
    tiene_numero = False
    for caracter in propuesta: 
        if caracter in "1234567890":
            tiene_numero = True

    #Se copia procedimiento anterior pero con caracteres especiales
    tiene_caracter_especial = False
    for caracter in propuesta: 
        if caracter in '¡!¿?@#$%&_-+*=|\{\}[].,;:<>/\~^\'"':
            tiene_caracter_especial = True

    #Se copia procedimeinto anterior pero con caracteres invalidos
    tiene_caracter_invalido = False
    for caracter in propuesta:
        if caracter not in "abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ1234567890¡!¿?@#$%&_-+*=|\{\}[].,;:<>/\~^\'\"":
            tiene_caracter_invalido = True
    
    #Checkea nombre del usuario
    tiene_nombre_usuario = False
    nombre_aux = nombre.lower()
    propuesta_aux = propuesta.lower()
    #Revisa cada caracter de la propuesta
    for i in range(len(propuesta_aux)): 
        #Revisa si el caracter es igual a la primera letra del nombre
        if propuesta_aux[i] == nombre_aux[0]: 
            #Revisa si a partir de este caracter se escribio el nombre
            if propuesta_aux[i:len(nombre_aux)+i] == nombre_aux:
                tiene_nombre_usuario = True

    #Checkea nombre de la mascota
    tiene_nombre_mascota = False
    mascota_aux = nombre_mascota.lower()
    propuesta_aux = propuesta.lower()
    #Revisa cada caracter de la propuesta
    for i in range(len(propuesta_aux)): 
        #Revisa si el caracter es igual a la primera letra de la mascota
        if propuesta_aux[i] == mascota_aux[0]: 
            #Revisa si a partir de este caracter se escribio el nombre de la mascota
            if propuesta_aux[i:len(mascota_aux)+i] == mascota_aux: 
                tiene_nombre_mascota = True

    #Checkea repeticion de caracteres
    tiene_repeticion_caracteres = False
    cadena = ""
    #Revisa cada caracter de la propuesta 
    for i in range(len(propuesta)): 
        # selecciona substring a partir del caracter y los cinco
        # caracteres que lo siguen 
        investigo = propuesta[i:i+5]
        contador = 0
        #Revisa que no sean todos iguales
        for j in range(len(investigo)-1): 
            if investigo[j] == investigo[j+1]: 
                contador += 1
        #Si lo son, cambia condicion
        if contador == 4: 
            tiene_repeticion_caracteres = True
            cadena = investigo
                
    #verifica longitud 
    if len(propuesta) < 10:
         print("Contraseña muy corta, debe tener al menos 10 caracteres.")
    #verifica minusculas
    elif not tiene_minuscula: 
        print("Debe incluir letras minusculas.")
    #verifica mayusculas
    elif not tiene_mayuscula: 
        print("Debe incluir letras mayusculas.")
    #verifica numeros
    elif not tiene_numero: 
        print("Debe incluir digitos numericos.")
    #verifica caracteres invalidos 
    elif tiene_caracter_invalido:
        print("La contraseña contiene caracteres invalidos.")
    #verifica caracter especial
    elif not tiene_caracter_especial: 
        print("Debe incluir caracteres especiales válidos.")
    #verifica nombre de la persona 
    elif tiene_nombre_usuario:
        print("Contraseña no debe incluir su nombre.")
    #verifica nombre de la mascota
    elif tiene_nombre_mascota:
        print("Contraseña no debe incluir el nombre de su mascota.")       
    #verifica patrones 
    elif tiene_repeticion_caracteres:
        print("No debe contener patrones : "+cadena)
    else: 
        print("Contraseña valida!")