from Gestion_de_productos import *
from Gestion_de_clientes import *
from funciones import validar
from Clase_tienda import *

#Menú interno de la tienda

class Tienda:
    def __init__(self):
        self.productos=productos
        self.clientes=clientes
        self.ventas=[]
        self.motorizado=None
        self.motorizados=[]
    
    def agregar_motorizado(self, nombre, placa):
     self.motorizado = {'nombre': nombre, 'placa': placa}
    
    def tienda_menu(self,usuario): #Esta función sirve para activar las funciones internas de la tienda
        print("          -------- [ Menu ] --------          \n")
        print("     1. Añadir al carrito")
        print("     2. Procesar pago")
        print("     3. Ver carrito")
        print("     4. Salir")
        opcion = input("     Ingrese el número de opción deseada: ")
        validar(opcion,"Rango",None,5)
        if opcion == "1": # Función para agregar productos a un carrito de compras personal
            print("------------------------------------------------")
            self.añadir_carrito(usuario)
        elif opcion == "2": # Función para generar la factura de la compra y te ofrece el delivery 
            print("------------------------------------------------")
            if len(usuario.carrito)==0: #Comprobación de los items dentro del carrito
                print("Usted no tiene nada en el carrito para comprar")
                self.tienda_menu(usuario)
            else:
                self.ventas.append(usuario.compra(usuario))
                ask=input("¿Qué método de envío desea?(MRW, Zoom, Delivery): ") #Función para registrar el método de envio
                validar(ask.capitalize(),"TextCon",["MRW","Zoom","Delivery"],None)
                if ask.capitalize()=="Delivery": #Función para registrar el motorizado
                    nombre_motorizado=input("Ingrese el nombre del motorizado: ")
                    validar(nombre_motorizado,"Texto", None, None)
                    telefono_motorizado=input("Ingrese el teléfono del motorizado: ")
                    validar(telefono_motorizado,"C.I", None, None)
                    self.motorizados.append({"Nombre":f"{nombre_motorizado}","Telefono":f"{telefono_motorizado}"})
                    print("El servicio tendrá un costo de 3$")
                    print("Gracias por su compra")
                elif ask=="MRW" or "Zoom":
                    print(f"Su envío se hará por {ask}")
                    print("Gracias por su compra")
                    pass
        elif opcion =="3": # Función para ver todos los productos dentro del carrito
            print("------------------------------------------------")
            usuario.mostrar_carrito()
            input("\nPresiona ENTER para continuar")
            self.tienda_menu(usuario)
        elif opcion=="4": #Aquí te devuelves al menú principal 
            print("¡Gracias por visitar nuestra tienda!")
            pass
        
    
    def Admin_menu(self): # Función para un menú para los administradores de la tienda 
        print("-------- [ Menu Del Administrador ] --------          \n")
        print("     1. Modificar productos")
        print("     2. Modificación de clientes")
        print("     3. Buscar venta")
        print("     4. Salir")
    
        opcion = input("     Ingrese el número de opción deseada: ")
        print("---------------------------------------------------")
        validar(opcion,"Rango",None,5)
        
        if opcion == "1": # Función para un menú para gestionar los productos
            print("---------------------------------------------------")
            print("     1. Añadir producto")
            print("     2. Modificar producto")
            print("     3. Eliminar producto")
            print("     4. Salir")
            opcion = input("     Ingrese el número de opción deseada: ")
            print("---------------------------------------------------")
            validar(opcion,"Rango",None,5)
            if opcion == "1": # Función para registrar un nuevo productio en la tienda
                print("------------------------------------------------")
                self.registro_de_producto()
            if opcion == "2": # Función para modificar la información de los productos existentes
                print("------------------------------------------------")
                self.modificar_producto()
            if opcion == "3": # Función para eliminar productos de la tienda
                print("------------------------------------------------")
                self.eliminar_producto()
            if opcion == "4":
                pass
            
        elif opcion=="2": # Función para un menú para gestionar los clientes
            print("     1. Modificar información de cliente")
            print("     2. Eliminar cliente de la tienda")
            print("     3. Salir")
            opcion = input("     Ingrese el número de opción deseada: ")
            print("---------------------------------------------------")
            validar(opcion,"Rango",None,4)
            if opcion == "1": # Función para modificar la información de un cliente existente
                print("------------------------------------------------")
                self.modificar_cliente()
            elif opcion=="2": # Función para eliminar clientes de la tienda
                print("------------------------------------------------")
                self.eliminar_cliente()
                
        elif opcion == "3": # Función para un menú para hacer busquedas
                print("------------------------------------------------")
                print("     1. Buscar por Cliente")
                print("     2. Buscar por Fecha de la venta")
                print("     3. Salir")
                opcion = input("     Ingrese el número de opción de busqueda deseada: ")
                print("---------------------------------------------------")
                validar(opcion,"Rango",None,5)
                if opcion=="1": # Función para buscar el cliente
                    print("------------------------------------------------")
                    self.buscar_por_cliente()
                elif opcion=="2": # Función para buscar una venta por su fecha
                    print("------------------------------------------------")
                    self.buscar_por_fecha()
                elif opcion=="3":
                    pass
                
        elif opcion=="4": 
            self.Admin_menu()
        
    def registro_de_producto(self): # Función para registrar el producto con todos sus nuevos datos
        name = input("Ingrese el nombre del producto: ")
        description = input("Indique la descripcion del producto: ")
        price = int(input("Ingrese el precio del producto: "))
        category = input("Indique la categoría del producto: ")
        inventario= int(input("Indique el inventario del producto: "))
        productos.append(Products(name, description, price, category,inventario))
        for producto in productos:
            producto.mostrar()
    
    def modificar_producto(self): # Función para modificar los datos ya registrados de un porducto
            nombre = input("Ingrese el nombre del producto que desea modificar: ")
            encontrado = False

            for productmodi in productos:
                if productmodi.name == nombre:
                    nuevo_nombre = input(f"Ingrese el nuevo nombre del producto {productmodi.name}: ")
                    nuevo_descripcion = input(f"Ingrese la nueva descripcion del producto {productmodi.name}: ")
                    nuevo_precio = input(f"Ingrese el nuevo precio del producto {productmodi.name}: ")
                    nueva_categoria = input(f"Ingrese la nueva categoría del producto {productmodi.name}: ")
                    nuevo_inventario = input(f"Ingrese la nueva cantidad disponible del producto {productmodi.name}: ")
                    productmodi.name = nuevo_nombre
                    productmodi.description = nuevo_descripcion
                    productmodi.price = nuevo_precio
                    productmodi.category = nueva_categoria
                    productmodi.iventario = nuevo_inventario

                    print("Producto modificado con éxito.")
                    encontrado = True
                    break
            if not encontrado:
                print("No se encontró un producto con ese nombre.")
    
    def eliminar_producto(self): # Función para eliminar productos de la tienda
            nombre = input("Ingrese el nombre del producto que desea eliminar: ")
            encontrado = False

            for productdelete in productos:
                if productdelete.name == nombre:
                    productos.remove(productdelete)
                    print("Producto eliminado con éxito.")
                    encontrado = True
                    break
            if not encontrado:
                print("No se encontró un producto con ese nombre.")
            
    def añadir_carrito(self,usuario): # Función para el menú para buscar y agregar los productos al carrito de compras personal
        print("     1. Buscar por nombre")
        print("     2. Buscar por precio")
        print("     3. Buscar por categoría")
        print("     4. Buscar por inventario")
        print("     5. Ver todo")
        opcion=input("Elija una opcion>>>")
        validar(opcion,"Rango",None,6)
        if opcion=="1": # Función para buscar el producto que necesitas por su nombre
            print("------------------------------------------------")
            Products.buscar_producto_por_nombre()
        elif opcion=="2": # Función para buscar el producto que necesitas por su precio
            print("------------------------------------------------")
            Products.buscar_producto_por_precio(productos)
        elif opcion=="3": # Función para buscar el producto que necesitas por su categoria
            print("------------------------------------------------")
            Products.buscar_producto_por_categoria(productos)
        elif opcion=="4": # Función para buscar el producto que necesitas por su disponibilidad
            print("------------------------------------------------")
            Products.buscar_producto_por_inventario(productos)
        elif opcion=="5": # Función para ver la lista de todos los productos de la tienda
            print("------------------------------------------------")
            Products.mostrar_productos()
        Prod=Products.buscar_producto_por_nombre()
        if Prod!=None:
            usuario.carrito.append(Prod)
        elif Prod==None:
            print("El producto no se pudo añadir")
            self.tienda_menu(usuario)
        ask=input("Desea continuar? y/n")
        validar(ask,"TextCon",["Y","N"],None)
        if ask =="y":
            self.añadir_carrito(usuario)
        else:
            self.tienda_menu(usuario)
    
    def registrar_cliente(self): # Función para registrar el cliente con todos sus nuevos datos
        nombre = input("Ingrese el nombre y apellido o razón social del cliente: ")
        validar(nombre, "Texto", None, None)
        tipo = input("Ingrese el tipo de cliente (Natural o Jurídico): ")
        validar(tipo, "TextCon", ["Jurídico", "Natural"],None)
        identificacion = input("Ingrese la cédula o RIF del cliente: ")
        validar(identificacion, "C.I", None, None)
        while True:
            correo = input("Ingrese el correo electrónico del cliente: ")
            if "@" in correo:
                    break
            else:
                print("Entrada invalida, recuerde usar @. Intente de nuevo: ")
        direccion = input("Ingrese la dirección de envío del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        validar(telefono,"C.I", None, None)
        nuevo_cliente = Cliente(nombre, tipo, identificacion, correo, direccion, telefono)
        clientes.append(nuevo_cliente)
        print("Cliente registrado con éxito.")
        return nuevo_cliente
    
    def modificar_cliente(self): # Función para modificar los datos ya registrados de un cliente
        identificacion = input("Ingrese la cédula o RIF del cliente que desea modificar: ")
        encontrado = False

        for cliente in clientes:
            if cliente.identificacion == identificacion:
                nuevo_nombre = input(f"Ingrese el nuevo nombre y apellido o razón social para el cliente {cliente.nombre}: ")
                nuevo_tipo = input(f"Ingrese el nuevo tipo de cliente para el cliente {cliente.nombre}: ")
                nuevo_correo = input(f"Ingrese el nuevo correo electrónico para el cliente {cliente.nombre}: ")
                nueva_direccion = input(f"Ingrese la nueva dirección de envío para el cliente {cliente.nombre}: ")
                nuevo_telefono = input(f"Ingrese el nuevo teléfono para el cliente {cliente.nombre}: ")
                cliente.nombre = nuevo_nombre
                cliente.tipo = nuevo_tipo
                cliente.correo = nuevo_correo
                cliente.direccion = nueva_direccion
                cliente.telefono = nuevo_telefono

                print("Cliente modificado con éxito.")
                encontrado = True
                break

        if not encontrado:
            print("No se encontró un cliente con la cédula o RIF ingresado.")


    def eliminar_cliente(self): # Función para eliminar clientes de la tienda
        identificacion = input("Ingrese la cédula o RIF del cliente que desea eliminar: ")
        encontrado = False

        for cliente in clientes:
            if cliente.identificacion == identificacion:
                clientes.remove(cliente)
                print("Cliente eliminado con éxito.")
                encontrado = True
                break

        if not encontrado:
            print("No se encontró un cliente con la cédula o RIF ingresado.")

    
    def buscar_cliente_por_identificacion(self): # Función para buscar el cliente por su cedula o RIF
        identificacion = input("Ingrese la cédula o RIF del cliente que desea buscar: ")
        for cliente in self.clientes:
            if cliente.identificacion == identificacion:
                print("Información del cliente encontrado:")
                print(f"Nombre: {cliente.nombre}") 
                print(f"Tipo: {cliente.tipo}")
                print(f"Correo electrónico: {cliente.correo}")
                print(f"Dirección de envío: {cliente.direccion}")
                print(f"Teléfono: {cliente.telefono}")
                self.clientes.append(cliente)
                return cliente

        print("No se encontró un cliente con la cédula o RIF ingresado.")


    def buscar_cliente_por_correo(self): # Función para buscar el cliente por su correo electrónico
        correo = input("Ingrese el correo electrónico del cliente que desea buscar: ")
        for cliente in self.clientes:
            if cliente.correo == correo:
                print("Información del cliente encontrado:")
                print(f"Nombre: {cliente.nombre}")
                print(f"Tipo: {cliente.tipo}")
                print(f"Cédula o RIF: {cliente.identificacion}")
                print(f"Dirección de envío: {cliente.direccion}")
                print(f"Teléfono: {cliente.telefono}")
                return cliente

        print("No se encontró un cliente con el correo electrónico ingresado.")
        
    # Función para buscar pagos por cliente
    def buscar_por_cliente(self):
        cliente = input("Ingrese el nombre del cliente: ")
        resultados = []
        for pago in self.ventas:
            if pago.cliente == cliente:
                resultados.append(pago)
        if len(resultados) == 0:
            print("No se encontraron pagos para el cliente especificado.")
        else:
            print("Se encontraron los siguientes pagos para el cliente", cliente)
            for pago in resultados:
                print("- Monto:", pago.monto, pago.moneda, "- Tipo:", pago.tipo, "- Fecha:", pago.fecha)
                

    # Función para buscar pagos por fecha
    def buscar_por_fecha(self):
        fecha = input("Ingrese la fecha en formato DD/MM/AAAA: ")
        resultados = []
        for pago in self.ventas:
            if pago.fecha == fecha:
                resultados.append(pago)
        if len(resultados) == 0:
            print("No se encontraron pagos para la fecha especificada.")
        else:
            print("Se encontraron los siguientes pagos para la fecha", fecha)
            for pago in resultados:
                print("- Cliente:", pago.cliente, "- Monto:", pago.monto, pago.moneda, "- Tipo:", pago.tipo)

    # Función para buscar pagos por tipo de pago
    def buscar_por_tipo(self):
        tipo = input("Ingrese el tipo de pago (e.g. PdV, PM, Zelle, Cash): ")
        resultados = []
        for pago in self.ventas:
            if pago.tipo == tipo:
                resultados.append(pago)
        if len(resultados) == 0:
            print("No se encontraron pagos para el tipo de pago especificado.")
        else:
            print("Se encontraron los siguientes pagos para el tipo de pago", tipo)
            for pago in resultados:
                print("- Cliente:", pago.cliente, "- Monto:", pago.monto, pago.moneda, "- Fecha:", pago.fecha)

    # Función para buscar pagos por moneda
    def buscar_por_moneda(self):
        moneda = input("Ingrese la moneda del pago: ")
        resultados = []
        for pago in self.ventas:
            if pago.moneda == moneda:
                resultados.append(pago)
        if len(resultados) == 0:
            print("No se encontraron pagos para la moneda especificada.")
        else:
            print("Se encontraron los siguientes pagos para la moneda", moneda)
            for pago in resultados:
                print("- Cliente:", pago.cliente, "- Monto:", pago.monto, "- Tipo:", pago.tipo, "- Fecha:", pago.fecha)
                
        
