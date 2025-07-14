products = {}
cont = 0
number = int(input("Ingrese cuantos productos desea ingresar: "))
for i in range(number):
    allow = False
    print(f"{number}")
    while allow == False:
        Pcode = (f"P + {cont}")
        name = input("Ingrese el nombre del producto: ")
        category = input("Ingrese el categoria del producto: ")
        size = input("Ingrese la talla del producto: ")
        check = size.lower()
        if check == "xs" or check == "s" or check == "m" or check == "l" or check == "xl":
            price = int(input("Ingrese el precio del producto: "))
            if price <= 0:
                print("El precio ingresado no es valido")
            else:
                stock = int(input("Ingrese la cantidad del producto ingresado: "))
                if stock <= 0:
                    print("La cantidad ingresada no es valida")
                else:
                    break
        else:
            print("La talla ingresada no es valida")
    products[Pcode] = {"name": name, "category": category, "price": price, "stock": stock}
    cont = cont + 1
def Menu():
    print("Venta de Ropa")
    print("1.Mostar la lista completa de productos")
    print("2.Buscar detalles de un producto")
    print("3.Valor total del inventario")
    print("4.Mostrar cuantos productos hay por categoría")
    print("5.Salir del programa")
allow = False
while allow == False:
    Menu()
    opt = int(input("Ingrese la opción que desee: "))
    match opt:
        case 1:
            print("Información de todos los productos: ")
            print(" ")
            for code,value in products.items():
                print(f"Nombre:{value['name']} codigo: {code}")
        case 2:
            print("Buscar")
        case 3:
            print("Precio")
        case 4:
            print("Mostrar ")
        case 5:
            print("Gracias por usar el pograma")
            break
        case _:
            print("La opción seleccionada no es valida")