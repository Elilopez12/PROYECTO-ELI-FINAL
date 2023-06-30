from funciones import validar
from Gestion_de_clientes import Cliente
from Clase_tienda import *


#Menu principal

tienda=Tienda()
def menu_principal():
        print("          -------- [ Menu ] --------          \n")
        print("     1. Registrar cliente")
        print("     2. Buscar cliente")
        print("     3. Opciones de gestión")
        print("     4. Obtener informes de venta")
        opcion = input("     Ingrese el número de opción deseada: ")
        validar(opcion,"Rango",None,4)
        if opcion == "1":
            print("------------------------------------------------")
            usuario=tienda.registrar_cliente()
            tienda.tienda_menu(usuario)
        elif opcion == "2":
            print("------------------------------------------------")
            tienda.tienda_menu(tienda.buscar_cliente_por_identificacion())
        elif opcion =="3":
            print("------------------------------------------------")
            tienda.tienda_menu(tienda.Admin_menu())
        elif opcion=="4":
            pass
        else: 
            menu_principal()

menu_principal()

