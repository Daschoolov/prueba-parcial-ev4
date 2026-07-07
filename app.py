import os
import modulo as mm

opmenu = ""

while True:
    os.system("cls")
    opmenu = str(input("""
=========Menu=======
1. Stock por categoria
2. Buscar por rango de precio
3. Actualizar precios
4. Agregar producto
5. Eliminar productos
6. Mostrar productos
7. Salir
=====================
Elija una opcion: """)).strip()

    match opmenu:
        case "0":
            mm.data_test()
            os.system("pause")
        case "1":
            os.system("cls")
            mm.stock_por_categoria()
            os.system("pause")
        case "2":
            os.system("cls")
            mm.buscar_por_precio()
            os.system("pause")
        case "3":
            os.system("cls")
            mm.actualizar_precio()
            os.system("pause")
        case "4":
            os.system("cls")
            mm.agregar_producto()
            os.system("pause")
        case "5":
            os.system("cls")
            mm.eliminar_producto()
            os.system("pause")
        case "6":
            os.system("cls")
            mm.mostrar_productos()
            os.system("pause")
        case 7:
            break

        case _:
            print("OPCION INVALIDA")
            os.system("pause")
