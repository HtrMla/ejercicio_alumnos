import os, msvcrt


menu = """MENÚ
1. Agregar alumnos 
2. Ver alumnos
3. Salir"""
alumnos=[]
while True:
    os.system('cls')
    print(menu)
    opc=input("Ingrese una opcion: ")
    if opc=="1":
        print("AGREGAR ALUMNO")
        codigo=input("Ingrese código: ")
        edad=int(input("Ingrese edad: "))
        while True:
            nombre=input("Ingrese nombre: ").strip().title()
            if len(nombre)>=3 and nombre.isalpha:
                break
            else:
                print("ERROR! nombre muy corto!")
        alumno={
            "codigo": codigo,
            "nombre": nombre,
            "edad": edad
        }
        alumnos.append(alumno)
        print("Alumnos guardado con éxito!")

    elif opc=="2":
        print("VER ALUMNOS")
        for a in alumnos:
            print(f"El alumno {a["nombre"]} de codigo {a["codigo"]} tiene {a["edad"]} años")
            #print(a)

    elif opc=="3":
        print("Adíos!")
        break
    else:
        print("Opción Incorrecta!")
    print("\n... presione una tecla para continuar...")
    msvcrt.getch()