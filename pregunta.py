"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re


def ingest_data():

    cluster = []
    cant = []
    porc = []
    princ = []
    claves = ''

    with open('clusters_report.txt', 'r') as file:
        lines = file.readlines()
    lines = lines[4:]

    for linea in lines:
        linea = linea.strip()
        linea = re.split('\s+', linea)
        if(linea[0].isdigit()):
            numericos = linea[:linea.index('%')]
            cluster.append(int(numericos[0]))
            cant.append(int(numericos[1]))
            porc.append(float(numericos[2].replace(',','.')))
            if len(claves) != 0:
                princ.append(claves.replace('.','').strip())
            claves = ' '.join(linea[linea.index('%')+1:])+' '
        else:

            claves = claves + ' '.join(linea)+' '

    princ.append(claves.replace('.','').strip())
    data = {'cluster': cluster, 'cantidad_de_palabras_clave': cant, 'porcentaje_de_palabras_clave': porc, 'principales_palabras_clave':princ}
    df = pd.DataFrame(data)
    return df

print('\n------------------------------------Hecho por Juan Pablo Buitrago Diaz CC 1000.206.552-------------------------------------\n')


