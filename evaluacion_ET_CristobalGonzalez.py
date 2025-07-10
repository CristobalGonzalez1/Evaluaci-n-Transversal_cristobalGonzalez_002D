# datos de almacenamiento
productos = {"8475HD":{"marca":"HP",'pantalla':15.6,'ram':"8BG",'disco':"DD",'GBdeDD':"1T",'preocesador':"Intel Core i5",'video':"Nvidia GTX1050"},
             "2175HD" :{"marca":"Acer",'pantalla':14,'ram':"4BG",'disco':"SSD",'GBdeDD':"512GB",'preocesador':"Intel Core i5",'video':"Nvidia GTX1050"},
             "JfjFHD" :{"marca":"Asus",'pantalla':14,'ram':"16BG",'disco':"SSD",'GBdeDD':"256GB",'preocesador':"Intel Core i7",'video':"Nvidia RTX2080Ti"}}

stock = {"8475HD":{'precio':387990,"stock":10},
         "2175HD":{'precio':327990,"stock":4},
         "JfjFHD":{'precio':424990,"stock":2}}
#funciones para el menu
def Stock_marca(marca):
    stock_total = 0
    
 
def Busqueda_precio(p_min,p_max):
    lista = []
    
    
def eliminar_producto(modelo):
    if modelo in productos:
        productos.pop(modelo)
        stock.pop(modelo)
        return True
    else:
        return False


while True:
    print("*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Busqueda por precio.")
    print("3. Eliminar producto.")
    print("4. Salir.")
    op = int(input("Ingrese una opcion: "))
    if op == 1:
        marca = input("Ingrese marca a consultar: ").lower()
        Stock_marca(marca)
    elif op == 2:
        while True:
            try:
                p_min = int(input("\ningrese precio minimo: "))
                if p_min < 0:
                    print("Debe ingresar numeros enteros positivos")
                    break
                p_max = int(input("ingrese precio maximo: "))
                if p_min < 0:
                    print("Debe ingresar numeros enteros positivos")
                    break
                Busqueda_precio(p_min,p_max)
                break
            except ValueError:
                print("Debe ingresar numeros!!")
    elif op == 3:
        while True:
            modelo = input("Ingrese modelo a eliminar: ")
            resultado = eliminar_producto(modelo)
            if resultado:
                print("Producto eliminado!!")
            else:
                print("El modelo no existe!!")
    elif op == 4:
        print("programa finalizado.")
        break
    else:
        print("Debe seleccionar una opcion valida!!")
