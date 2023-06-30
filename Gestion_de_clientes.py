from funciones import *
from Gestion_de_productos import *
import datetime
from Gestion_de_pago import Pago

clientes=[]

#Clase para definir los datos de los clientes

class Cliente:
    def __init__(self, nombre, tipo, identificacion, correo, direccion, telefono):
        self.nombre = nombre
        self.tipo = tipo
        self.identificacion = identificacion
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono
        self.historial=[]#Lista de productos
        self.carrito=[]#Lista de productos
        self.pago=0
        self.deuda=0
    
    # Función para ver los productos que están en el carrito personal
    def mostrar_carrito(self): 
        for prod in self.carrito:
            prod.mostrar()

    # Función para comprar productos de la tienda
    def compra(self,usuario):
        for producto in usuario.carrito:
            self.pago+=producto.price
        if usuario.tipo==("Jurídico").lower():
            moneda="Bolivar"
            opcion=input("Elija una opción \n 1) Pago de contado\n 2) Pago debito") # Función para distribuir los tipos de pago 
            validar(opcion,"Rango",None,3)
            if opcion=="1":
                tipo_pago="Contado" 
                self.pago-=self.pago*0.05
                self.pago+=self.pago*0.16
                self.deuda+=self.pago
                print("\n --------------TPN-----------------") # Función para generar factura
                print(f"Razón Social: {self.nombre}")
                print(f"Descuento: 5% de descuento por pago por contado")
                print(f"Factura:")

                for x in usuario.carrito:
                    print(f"""{x.name} Bs: {x.price}
                          total: {self.pago}""")
            elif opcion=="2":
                self.pago+=self.pago*0.16
                print("\n --------------TPN-----------------") # Función para generar factura 
                print(f"Razón Social: {self.nombre}")
                print(f"Descuento: N/A")
                print(f"""Factura: 
                      """)

                for x in usuario.carrito:
                    print(f"""{x.name} Bs: {x.price}
                          total: {self.pago}""")
        else:
            opcion=input("Elija una opción \n 1) Pago por divisa\n 2) Pago por bolivares")
            validar(opcion,"Rango",None,3)
            if opcion=="1":
                tipo_pago = input("Ingrese el tipo de pago (e.g. PdV, PM, Zelle): ")
                moneda="Divisa"
                self.pago+=self.pago*0.19
                print("\n --------------TPN-----------------") # Función para generar factura
                print(f"Razón Social: {self.nombre}")
                print(f"Descuento: N/A")
                print(f"Factura:")

                for x in usuario.carrito:
                    print(f"""{x.name} Bs: {x.price}
                            total: {self.pago}""")
            elif opcion=="2":
                tipo_pago = input("Ingrese el tipo de pago (e.g. PdV, PM, Zelle): ")
                validar(tipo_pago.capitalize,"TextCon",["PdV","PM","Zelle","Culo"],5)
                moneda="Bolivar"
                self.pago+=self.pago*0.16
                print("\n --------------TPN-----------------") # Función para generar factura
                print(f"Razón Social: {self.nombre}")
                print("Descuento: N/A")
                print(f"Factura:")
                for x in usuario.carrito:
                    print(f"""{x.name} Bs: {x.price}
                          total: {self.pago}""")
        
            pp=[]     
            for x in self.carrito:
                self.historial.append(x)
                pp.append(x)
            self.carrito=[]
            fecha = datetime.date.today() # Función para registrar la fecha actual
            venta=Pago(usuario.nombre,self.pago,moneda,tipo_pago,fecha,pp)
            print("------------------------------------------------")
            input("Presione ENTER para continuar")
            return(venta)
    
    
    