import os, msvcrt

menu = """MENÚ
1. Agregar alumnos 
2. Ver alumnos
3. Salir"""
while True:
    os.system('cls')
    print(menu)
    opc=input("Ingrese una opcion: ")
    if opc=="1":
        pass
    elif opc=="2":
        pass
    elif opc=="3":
        print("Adíos!")
        break
    else:
        print("Opción Incorrecta!")
    print("\n... presione una tecla para continuar...")
    msvcrt.getch()