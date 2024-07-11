
def ordenar_alfabeticamente(proyectos):
    proyectos = proyectos[:]
    cantidad_proyectos = len(proyectos) 
    ordenar = input('1. De la A a la Z.\n2. De la Z a la A.\n----> ')
    bandera = False

    if ordenar == '1':
        
        for i in range(cantidad_proyectos):
            for j in range(0, cantidad_proyectos-i-1):
                if proyectos[j]['Nombre del Proyecto'].lower() > proyectos[j+1]['Nombre del Proyecto'].lower():
                    proyectos[j], proyectos[j+1] = proyectos[j+1], proyectos[j]
        bandera = True
    
    elif ordenar == '2':
        for i in range(cantidad_proyectos):
            for j in range(0, cantidad_proyectos-i-1):
                if proyectos[j]['Nombre del Proyecto'].lower() < proyectos[j+1]['Nombre del Proyecto'].lower():
                    proyectos[j], proyectos[j+1] = proyectos[j+1], proyectos[j]
        bandera = True
    
    if bandera:
        print('\n- - - -')
        for proyecto in proyectos:
            print(f'Nombre del proyecto: {proyecto["Nombre del Proyecto"]}')
        print('- - - -')
    
    else:
        print('\nOpción no válida. Por favor, seleccione "a" para ascendente o "d" para descendente.\n')


def ordenar_por_presupuesto(proyectos):
    proyectos = proyectos[:]
    cantidad_proyectos = len(proyectos)
    ordenar = input('\n1. De mayor a menor.\n2. De menor a mayor\n----> ')
    bandera = False

    if ordenar == '1':      
        
        for i in range(cantidad_proyectos):
            for j in range(0, cantidad_proyectos-i-1):
                if proyectos[j]['Presupuesto'] < proyectos[j+1]['Presupuesto']:
                    proyectos[j], proyectos[j+1] = proyectos[j+1], proyectos[j]
        bandera = True

    elif ordenar == '2':
    
        for i in range(cantidad_proyectos):
            for j in range(0, cantidad_proyectos-i-1):
                if proyectos[j]['Presupuesto'] > proyectos[j+1]['Presupuesto']:
                    proyectos[j], proyectos[j+1] = proyectos[j+1], proyectos[j]
        bandera = True

    if bandera:
        print('\n- - - -')
        for proyecto in proyectos:
                print(f'{proyecto["Nombre del Proyecto"]} | Presupuesto: ${proyecto["Presupuesto"]:,.2f}')
        print('- - - -')
    
    else:
        print('\nOpción no válida.\n')


def ordenar_por_fecha(proyectos):
    proyectos = proyectos[:]
    cantidad_proyectos = len(proyectos)
    ordenar = input('\n1. De más antiguo al más reciente.\n2. Del más reciente al más antiguo.\n----> ')
    bandera = False
    
    if ordenar == '1':   
        for i in range(cantidad_proyectos):
            for j in range(0, cantidad_proyectos-i-1):
                fecha1 = proyectos[j]['Fecha de inicio']
                fecha2 = proyectos[j+1]['Fecha de inicio']
                if fecha1 > fecha2:
                    proyectos[j], proyectos[j+1] = proyectos[j+1], proyectos[j]
        bandera = True
    
    elif ordenar == '2':
        for i in range(cantidad_proyectos):
            for j in range(0, cantidad_proyectos-i-1):
                fecha1 = proyectos[j]['Fecha de inicio']
                fecha2 = proyectos[j+1]['Fecha de inicio']
                if fecha1 < fecha2:
                    proyectos[j], proyectos[j+1] = proyectos[j+1], proyectos[j]
        bandera = True
    
    if bandera:
        print('\n- - - -')
        for proyecto in proyectos:
            fecha = proyecto["Fecha de inicio"].strftime("%d/%m/%Y")
            print(f'{proyecto["Nombre del Proyecto"]} | Fecha de inicio: {fecha}')
        print('- - - -')
    
    else:
        print('\nOpción no válida.\n')