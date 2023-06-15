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
                #print('insertando',claves,'en princ\n')
                princ.append(claves.replace('.','').strip())
                #print("Nuevo princ es",princ,'\n')
            claves = ' '.join(linea[linea.index('%')+1:])+' '
            #print("Claves es",claves)
        else:

            claves = claves + ' '.join(linea)+' '

    #print('insertando',claves,'en princ\n')
    princ.append(claves.replace('.','').strip())
    data = {'cluster': cluster, 'cantidad_de_palabras_clave': cant, 'porcentaje_de_palabras_clave': porc, 'principales_palabras_clave':princ}
    df = pd.DataFrame(data)
            
            
    
    #print(cluster,"Su largo es",len(cluster))
    #print(cant,"Su largo es",len(cant))
    #print(porc,"Su largo es",len(porc))
    #print(princ,"Su largo es",len(princ))
    #print(df)
    return df

print('\n-----------------------Hecho por Juan Pablo Buitrago Diaz CC 1000.206.552------------------------\n')


respuestas_Correctas = ["maximum power point tracking, fuzzy-logic based control, photo voltaic (pv), photo-voltaic system, differential evolution algorithm, evolutionary algorithm, double-fed induction generator (dfig), ant colony optimisation, photo voltaic array, firefly algorithm, partial shade",
                        "support vector machine, long short-term memory, back-propagation neural network, convolution neural network, speed wind prediction, energy consumption, wind power forecasting, extreme learning machine, recurrent-neural-network (rnn), radial basis function (rbf) networks, wind farm",
                        "smart grid, wind power, reinforcement learning, energy management, energy efficiency, solar energy, deep reinforcement learning, demand-response (dr), internet of things, energy harvester, q-learning",
                        "wind turbine, fault diagnosis, biodiesel, failure detection, response-surface methodology, condition monitoring, load forecasting, energy consumption forecast, anomalies detection, optimization-based algorithm, supervisory control and data acquisition"]

for i in range (0,4):
    if(ingest_data().principales_palabras_clave.to_list()[i] == respuestas_Correctas[i]):
        print(ingest_data().principales_palabras_clave.to_list()[i])
        print(respuestas_Correctas[i])
        print('son iguales\n')
    else:
        print(ingest_data().principales_palabras_clave.to_list()[i])
        print(respuestas_Correctas[i])
        print('no son iguales\n')