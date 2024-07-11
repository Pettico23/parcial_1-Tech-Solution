import csv
import json
from datetime import datetime

def parse_csv(nombre_archivo):
    
    proyectos = []
    
    
    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
        
        lector = csv.DictReader(archivo)
        
        for linea in lector:
            
            linea['Fecha de inicio'] = linea['Fecha de inicio'].replace('-','/')
            linea['Fecha de inicio'] = datetime.strptime(linea['Fecha de inicio'], '%d/%m/%Y') #● Fecha de Inicio y Fecha de Fin: Deben ser fechas válidas en el formato "DD/MM/AAAA".
            linea['Fecha de Fin'] = linea['Fecha de Fin'].replace('-','/')
            linea['Fecha de Fin'] = datetime.strptime(linea['Fecha de Fin'], '%d/%m/%Y')
            linea['id'] = int(linea['id'])
            linea['Presupuesto'] = float(linea['Presupuesto'].replace('$', '').replace(',', ''))
            proyectos.append(linea)
        
            

    return proyectos

def ver_id(nombre_archivo): #id del archo y los pasa a un mensaje
    mensaje = ""
    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:

        lector = csv.DictReader(archivo)

        for l in lector:
            id = int(l['id'])
            nombre = l["Nombre del Proyecto"]
            mensaje += f"{id}: {nombre} \n"
    return mensaje

def escribir_proyectos(nombre_archivo, proyectos):
    
    with open(nombre_archivo, mode='w', encoding='utf-8', newline='') as file:
        claves = ['id', 'Nombre del Proyecto', 'Descripción', 'Fecha de inicio', 'Fecha de Fin', 'Presupuesto', 'Estado']
        writer = csv.DictWriter(file, fieldnames=claves)
        writer.writeheader()
        
        for proyecto in proyectos:
            if isinstance(proyecto['Fecha de inicio'], str):
                proyecto['Fecha de inicio'] = datetime.strptime(proyecto['Fecha de inicio'], '%d/%m/%Y')
            if isinstance(proyecto['Fecha de Fin'], str):
                proyecto['Fecha de Fin'] = datetime.strptime(proyecto['Fecha de Fin'], '%d/%m/%Y')
            
            proyecto['Fecha de inicio'] = proyecto['Fecha de inicio'].strftime('%d/%m/%Y')
            proyecto['Fecha de Fin'] = proyecto['Fecha de Fin'].strftime('%d/%m/%Y')
            
            if isinstance(proyecto['Presupuesto'], str):
                proyecto['Presupuesto'] = float(proyecto['Presupuesto'].replace(',', '').replace('$', ''))

            proyecto['Presupuesto'] = f"${proyecto['Presupuesto']:,.2f}"

            writer.writerow(proyecto)


