productos_list = []


def validar_disponible(disponible):
    if not disponible in ["SI", "NO"]:
        print(" ERROR, solo se puede ingresar Si o No")
        return False

    return True


def validar_precio(precio):
    if not precio > 0:
        print(" ERROR, el precio debe ser mayor a 0")
        return False

    return True


def validar_texto(texto):
    if len(texto.strip()) == 0:
        print(" ERROR, ingrese datos nuevamente para continuar-")
        return False

    if " " in texto:
        print(" ERROR, el texto no puede contener espacios vacios")
        return False

    return True


def validar_codigo(codigo):
    for producto in productos_list:
        if producto["codigo"] == codigo:
            print(" ERROR, el codigo ya se encuentra registrado")
            return False

    if len(codigo.strip()) == 0:
        print(" ERROR, ingrese datos nuevamente para continuar-")
        return False

    return True


def imprimir_producto(producto):
    dispo = "Disponible" if producto["disponible"] == True else "No-Disponible"
    print(f"""
=========Producto========
Nombre: {producto["nombre"]}
Categoria: {producto["categoria"]}
Precio: ${producto["precio"]}
Disponible: {dispo}
=========================""")


def imprimir_inventario(producto):
    print(
        f"Codigo: {producto["codigo"]} [Stock:{producto["stock"]} / Vendidos:{producto["vendidos"]}]"
    )


def stock_por_categoria():
    if (len(productos_list)) == 0:
        print(" No hay registros de los datos")
    else:
        print("\n---Stock por categoria---")
        categoria = str(input("Ingrese categoria del producto: ")).strip().upper()
        while not validar_texto(categoria):
            categoria = str(input("Ingrese categoria del producto: ")).strip().upper()
        bandera_stock = False
        for producto in productos_list:
            if producto["categoria"] == categoria:
                bandera_stock = True
                imprimir_inventario(producto)
        if bandera_stock == False:
            print(f"-No hay registros de la categoria: {categoria}-")


def buscar_por_precio():
    if (len(productos_list)) == 0:
        print("No hay registros de los datos hasta el momento")
    else:
        print("\n---Buscar por rango de precios---")
        while True:
            try:
                min = int(input("Ingrese Rango minimo de busqueda: "))
                while not validar_precio(min):
                    min = int(input("Ingrese Rango minimo de busqueda: "))
                break
            except:
                print(" ERROR, el minimo debe ser un numero ")
        while True:
            try:
                max = int(input("Ingrese el rango inferior de busqueda: "))
                while not validar_precio(max):
                    max = int(input("Ingrese  el rango superior de busqueda: "))
                break
            except:
                print("ERROR, el maximo debe ser un numero")
        bandera_rango_precios = False
        for producto in productos_list:
            if min <= producto["precio"] <= max:
                bandera_rango_precios == True
                imprimir_producto(producto)
        if bandera_rango_precios == False:
            print(" No hay registros del producto en ese rango de precios")


def actualizar_precio():
    if (len(productos_list)) == 0:
        print(" No hay registros de los datos ")
    else:
        print("\n---Actualizar precio de producto---")
        codigo = str(input("Ingrese el codigo del producto: ")).strip().upper()
        while not validar_codigo(codigo):
            codigo = str(input("Ingrese el codigo del producto: ")).strip().upper()
        bandera_actualizar_precio = False
        for producto in productos_list:
            if producto["codigo"] == codigo:
                bandera_actualizar_precio = True
                while True:
                    try:
                        precio = int(input("Ingrese el nuevo precio del producto: "))
                        while not validar_precio(precio):
                            precio = int(input("Ingrese el nuevo precio del producto: "))
                        break
                    except:
                        print(" ERROR, El precio debe ser un numero-")
                producto["precio"] = precio
        if bandera_actualizar_precio == False:
            print(f" No hay registros del codigo: {codigo}-")


def agregar_producto():
    print("\n---Agregar producto---")
    codigo = str(input("Ingrese el codigo del producto: ")).strip().upper()
    while not validar_codigo(codigo):
        codigo = str(input("Ingrese codigo de producto: ")).strip().upper()
    nombre = str(input("Ingrese el nombre del producto: ")).strip().upper()
    while not validar_texto(nombre):
        nombre = str(input("Ingrese el nombre del producto: ")).strip().upper()
    categoria = str(input("Ingrese la categoria del producto: ")).strip().upper()
    while not validar_texto(categoria):
        categoria = str(input("Ingrese la categoria del producto: ")).strip().upper()
    while True:
        try:
            precio = int(input("Ingrese el precio del producto: "))
            while not validar_precio(precio):
                precio = int(input("Ingrese el precio del producto: "))
            break
        except:
            print(" ERROR, El precio debe ser un numero")
    disponible = str(input("""
¿Producto esta disponible?
        Si/No: """)).strip().upper()
    while not validar_disponible(disponible):
        disponible = str(input("""
¿Producto esta disponible?
        Si/No: """)).strip().upper()
    esta_disponible = True if disponible == "SI" else False
    while True:
        try:
            stock = int(input("Ingrese el stock de producto: "))
            while not validar_inventario(stock):
                stock = int(input("Ingrese el stock de producto: "))
            break
        except:
            print(" ERROR, El stock debe ser un numero")
    while True:
        try:
            vendidos = int(input("Ingrese cantidad vendida: "))
            while not validar_inventario(vendidos):
                vendidos = int(input("Ingrese cantidad vendida: "))
            break
        except:
            print("-ERROR Cantidad debe ser un numero-")
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "disponible": esta_disponible,
        "stock": stock,
        "vendidos": vendidos,
    }

    productos_list.append(producto)
    print("...Producto agregado con exito a la lista...")


def eliminar_producto():
    if (len(productos_list)) == 0:
        print(" No hay registros de datos hasta el momento")
    else:
        print("---Eliminar producto de lista---")
        codigo = str(input("Ingrese codigo de producto a eliminar: ")).strip().upper()
        while not validar_codigo(codigo):
            codigo = (
                str(input("Ingrese codigo de producto a eliminar: ")).strip().upper()
            )
        bandera_eliminar = False
        for producto in productos_list:
            if producto["codigo"] == codigo:
                bandera_eliminar = True
                productos_list.remove(producto)
                print(f"¡¡...Producto: {codigo} eliminado con exito...!!")
        if bandera_eliminar == False:
            print(f" No hay registros del codigo: {codigo}-")


def mostrar_productos():
    if (len(productos_list)) == 0:
        print(" No existen productos en la lista")
    else:
        print("---Productos enlistados---")
        for producto in productos_list:
            imprimir_producto(producto)


def validar_inventario(inventario):
    if not inventario >= 0:
        print("ERROR, La cantidad debe ser mayor o igual a 0")
        return False

    return True

