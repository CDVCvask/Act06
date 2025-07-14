products = {}
cont = 0
number = int(input("Ingrese cuantos productos desea ingresar: "))
for i in range(number):
    allow = False
    while allow == False:
        Pcode = (f"P"+{cont})
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
                    Allow = True

        else:
            print("La talla ingresada no es valida")