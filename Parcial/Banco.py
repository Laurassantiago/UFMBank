from main import Transacciones

def banco():
    menu()
    
def menu():
    coleccion_info = []
    while True:
        print("¡Bienvenido al rastreador financiero personal!")
        print("""
            1. Ver Resumen de Transacciones
            2. Agregar Transacción
            3. Eliminar Transacción
            4. Ver Transacciones por Categoría
            5. Establecer Presupuesto
            6. Salir
        """)
        opcion = int(input("Ingrese una opción del menú (1-6): "))
        if opcion == 1:
            coleccion_info.ver_resumen()   
        elif opcion == 2:
            monto_agregar = float(input("Ingresa el monto: "))
            categoria_agregar = input("Ingresa la categoría (comida, servicios, salarios, gastos): ").lower()
            fecha_agregar = input("Ingrese fecha: ")
            descripcion_agerar = input("Ingrese una mini descripcion: ")
            nuevo_transaccion=(monto_agregar,categoria_agregar,fecha_agregar,descripcion_agerar)
            coleccion_info.append(nuevo_transaccion)
            print("Transaccion agregado con exito")
            
        elif opcion == 3:

            pass
        elif opcion == 4:

            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            print("Salir")
            break
        else:
            print("Ingrese un número del 1 al 6")

banco()
