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
        price = int(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese la cantidad del producto ingresado: "))