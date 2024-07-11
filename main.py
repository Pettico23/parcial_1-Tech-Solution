'''
Apellido: Pettico
Nombre/s: Rodrigo
División: 314
DNI: 34623153
'''

from funciones import *
from parseado import *
from ordenamiento import *

nombre_archivo = 'Proyectos.csv'
proyectos = parse_csv(nombre_archivo)

def menu():
    while True:
        print("1. Ingresar Proyecto\n2. Modificar proyecto.\n3. Cancelar proyecto\n4. Comprobar proyectos\n5. Mostrar todos\n6. Calcular promedio\n7. Buscar proyecto por nombre\n8. Ordenar proyectos\n9. Retomar proyecto\n10. Ingresar un presupuesto máximo\n11. Informe de un proyecto\n12. Salir.\nR. Presupuesto de proyectos activos que contienen la palabra 'Desarrollo'.\nP. Proyectos finalizados con más de 3 años.")
        opcion = input("\nSeleccione una opción: ")
        opcion = opcion.lower()

        if opcion == '1':
            agregar_proyecto(proyectos)

        elif opcion == '2':
            print(ver_id(nombre_archivo))
            time.sleep(4)
            id_proyecto = (input("Por favor, ingresa el ID del proyecto que quieres modificar: "))
            modificar_proyecto(proyectos, id_proyecto)

        elif opcion == '3':
            print(ver_id(nombre_archivo))
            time.sleep(2)
            id_proyecto = int(input("Por favor, ingresa el ID del proyecto que quieres cancelar: "))
            cancelar_proyecto(proyectos, id_proyecto)
            
            time.sleep(4)

        elif opcion == '4':
            comprobar_proyectos(proyectos)
            time.sleep(4)

        elif opcion == '5':
            
            mostrar_todo(proyectos)
            time.sleep(4)

        elif opcion == '6':
            presupuesto_promedio(proyectos)
            time.sleep(4)

        elif opcion == '7':
            print(ver_id(nombre_archivo))
            time.sleep(4)
            nombre = input('Ingrese el nombre del proyecto a buscar: ')
            nombre = nombre.lower()
            buscar_por_nombre(nombre, proyectos)
            time.sleep(4)

        elif opcion == '8':
            opcion = input('\n¿Cómo desea ordenarlo?\n1. Por nombre.\n2. Por presupuesto.\n3. Fecha de inicio.\n----> ')
            if opcion == '1':
                ordenar_alfabeticamente(proyectos)
            elif opcion == '2':
                ordenar_por_presupuesto(proyectos)
            elif opcion == '3':
                ordenar_por_fecha(proyectos)
            time.sleep(4)

        elif opcion == '9':
            print(ver_id(nombre_archivo))
            time.sleep(2)
            id_proyecto = int(input("Por favor, ingresa el ID del proyecto que quieres retomar: "))
            retomar_proyecto(proyectos, id_proyecto)
            time.sleep(4)

        elif opcion == '10':
            presupuesto = input('Ingrese el presupuesto máximo: $')
            presupuesto = validacion_presupuesto(presupuesto)
            reporte_presupuesto(presupuesto, proyectos)

        elif opcion == '11':
            proyecto_a_buscar = input('Ingrese el nombre del proyecto: ')
            reporte_proyecto(proyectos, proyecto_a_buscar)

        elif opcion == '12':
            escribir_proyectos(nombre_archivo, proyectos)
            proyectos_finalizados_json(proyectos)
            print("Datos guardados. Saliendo del programa.\n")
            break
        
        elif opcion == 'r':
            r_presupuesto_de_proyecto_activo_que_contiene_desarrollo(proyectos)
            time.sleep(4)
            
        elif opcion == 'p':
            p_proyectos_finalizados_menos_3_años(proyectos)
            time.sleep(4)
        

        else:
            print("Opción inválida. Por favor, intente nuevamente.")
        
            
menu()
