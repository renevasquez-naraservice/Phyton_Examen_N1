# Estudiante => Rene Alejandro Vasquez Vare
# 1º Examen 
# Taller de Aplicaciones en Internet


#-----------------------------------------------
# Clase Productos
#-----------------------------------------------
class Producto:
    def __init__(self,name,price,amount):
        self.nombre = name
        self.precio = price
        self.cantidad = amount
    #Definimos los mètodos
    def mostrar_info(self):
        print("Producto => ",self.nombre)
        print("Precio => ",self.precio)
        print("Cantidad => ",self.cantidad)
    
    def valor_total(self):
        return(self.precio*self.cantidad); 

#-----------------------------------------------
# Productos
#-----------------------------------------------
productos=[]
def agregar_producto():
    print("----------------------------------------")
    nombre_p = str(input("Nombre del Producto: "))
    precio_p = float(input("Precio: "))
    cantidad_p = int(input("Cantidad: "))
    producto_1 = Producto(nombre_p,precio_p,cantidad_p)
    productos.append(producto_1)
    print("¡Producto agregado con éxito! :)")
    print("----------------------------------------")
def mostrar_productos(lista):
    i=0
    for producto in productos:
        i+=1
        print("-------------------------------------")
        print(f"Producto N° {i} <==========")
        print (f" + Nombre: ",producto.nombre)
        print (f" + Precio: ",producto.precio)
        print (f" + Cantidad: ",producto.cantidad," Bs")
        print (f" + Valor Total: ",producto.valor_total()," Bs")
        print("-------------------------------------")

def error():
    print("**************************************************************")
    print("Dato Inválido, vuelva a ingresar un valor descrito en el menú")
    print("**************************************************************")
    
#-----------------------------------------------
# Iniciar Programa
#-----------------------------------------------

def iniciar_():
    while True:
        menu()
        accion = int(input("¿Qué desea hacer? => "))
        if accion == 1:
            agregar_producto()
        elif accion == 2:
            mostrar_productos(productos)
        elif accion == 3:
            break
            print("==> La Sesión ha terminado :)")
        else:
            error()
#-----------------------------------------------
# Menu interactivo
#-----------------------------------------------
def menu():
    print("========== MENÚ ==========")
    print("1.- Agregar Producto")
    print("2.- Mostrar Productos")
    print("3.- Salir")

#-----------------------------------------------
# Programa
#-----------------------------------------------
iniciar_()

