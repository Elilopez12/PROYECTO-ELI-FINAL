#Funciones de validación

def validar(entrada,tipo_dato,pedido,rango): # Función para validar texto
    if tipo_dato=="Texto": # Función para validar texto desconocido (input)
        if entrada.isalpha()!=True:
            entrada=input("Entrada inválida, intente de nuevo: ")
            return(validar(entrada,"Texto",None,None))
    if tipo_dato=="TextCon": # Función para validar texto conocido
        if entrada.isalpha()!=True or (entrada.capitalize() not in pedido): # Función para validar mayusculas y minusculas
            entrada=input("Entrada inválida, intente de nuevo: ")
            return(validar(entrada,"TextCon",pedido,None))
    if tipo_dato=="Rango": 
        ent=[]
        for x in range(rango):
            ent.append(x)
        ent.pop(0)
        if entrada.isnumeric()==False: # Función para validar numeros
            entrada=input("Entrada inválida, intente de nuevo")
            return(validar(entrada,"Rango",None,rango))
        if int(entrada) not in ent: # Función para validar enteros
            entrada=input("Entrada inválida, intente de nuevo: ")
            return(validar(entrada,"Rango",None,rango))
    if tipo_dato=="C.I": # Función para validar cédulas
        if entrada.isnumeric()!=True or "." in entrada or "," in entrada:
            entrada=input("Entrada inválida, intente de nuevo: ")
            return(validar(entrada,"C.I",None,None))
