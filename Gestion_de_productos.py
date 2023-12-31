
class Products():
    def __init__(self, name, description, price, category,inventario):
        self.name=name
        self.description=description
        self.price=price
        self.category=category
        self.inventario=inventario
        
    def mostrar_name(self):
        print(self.name)

    def mostrar(self):
        print(f""" 
    - {self.name}
    - {self.description}
    - {self.price}
    - {self.category}
    - {self.inventario}
              """)
    
    def mostrar_productos():
        for producto in productos:
            producto.mostrar()
            
    def registro_de_producto():

        name = input("Ingrese el nombre del producto: ")
        description = input("Indique la descripcion del producto: ")
        price = int(input("Ingrese el precio del producto: "))
        category = input("Indique la categoría del producto: ")
        inventario= int(input("Indique el inventario del producto: "))
        productos.append(Products(name, description, price, category,inventario))
        for producto in productos:
            producto.mostrar()
            
    def buscar_producto_por_categoria(productos):
        categoria= input("Ingrese la categoría del producto que desea buscar: ").title()
        producto_encontrado = False
        for productscategory in productos:
            if productscategory.category == categoria:
                print("Información del producto encontrado:")
                productscategory.mostrar()
                producto_encontrado = True
        if not producto_encontrado:
            print("No se encontró un producto en esa categoria.")  

    def buscar_producto_por_precio(productos):
        price = input("Indique el precio que estima pagar: ")
        int_price = int(price)
        producto_encontrado = False
        for productsprice in productos:
            if productsprice.price == int_price:
                print("Información del producto encontrado:")
                productsprice.mostrar()
                producto_encontrado = True
        if not producto_encontrado:
            print("No se encontró un producto en ese precio.")

    def buscar_producto_por_nombre():
        nombre = input("Ingrese el nombre del producto: ")

        for productname in productos:
            if productname.name == nombre:
                print("Información del producto encontrado:")
                print(f"Nombre: {productname.name}")
                print(f"Descripción: {productname.description}")
                print(f"Precio: {productname.price}")
                print(f"Categoría: {productname.category}")
                print(f"Inventario: {productname.inventario}")
                return productname

        print("No se encontraron productos con ese nombre.")
                            
    def buscar_producto_por_inventario(productos):
        inventario = input("Indique la cantidad de unidades que necesita: ")
        int_inventario = int(inventario)
        producto_encontrado = False
        for productstock in productos:
            if productstock.inventario == int_inventario:
                print("Información del producto encontrado:")
                productstock.mostrar()
                producto_encontrado = True
        if not producto_encontrado:
            print("No se encontró un producto en esa cantidad.")
    

    def modificar_producto():
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
                

    def eliminar_producto():
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
                
p=Products
                
def menuproductos():
    
    while True:
        print("          -------- [ Menú ] --------          \n")
        print("     1. Ver productos") 
        print("     2. Registrar nuevo producto")
        print("     3. Modificar información del producto")
        print("     4. Eliminar producto")
        print("     5. Buscar producto por categoría")
        print("     6. Buscar producto por precio")
        print("     7. Buscar producto por nombre")
        print("     8. Buscar producto por disponibilidad")
        print("     9. Salir")
        opcion = input("     Ingrese el número de opción deseada: ")

        if opcion == "1":
            p.mostrar_productos()    
        elif opcion == "2":
            p.registro_de_producto()
        elif opcion == "3":
            p.modificar_producto()
        elif opcion == "4":
            p.eliminar_producto()
        elif opcion == "5":
            p.buscar_producto_por_categoria(productos)
        elif opcion == "6":
            p.buscar_producto_por_precio(productos)
        elif opcion == "7":
            p.buscar_producto_por_nombre()
        elif opcion == "8":
            p.buscar_producto_por_inventario(productos)
        elif opcion=="9":    
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
    print("Gracias por utilizar el sistema de gestión de productos.") 
        

        
import json
productos=[]
with open("PROYECTO ELIZABETH LÓPEZ.py/products (1).json") as x:
    lines=json.load(x)
    for x in lines:
        producto = Products(x.get("name"), x.get("description"), x.get("price"), x.get("category"), 10)
        productos.append(producto)
  
   