import pandas as pd
from fontTools.merge.util import first
import math




def calculate_distance(first_city,second_city):
    #FUNCION QUE UTILIZAREMOS PARA EL CALCULO DE LAS DISTANCIAS ENTRE CIUDADES
    distance = (second_city[0] - first_city[0])**2 + (second_city[1] - first_city[1])**2
    return math.sqrt(distance)


def dataframe_builder(nodes,visited_dataframe):
    #RECIBE UN DICCIONARIO PYTHON CON LAS CIUDADES Y SUS COORDENADAS
    #CREA UN DATAFRAME PANDAS CON CADA UNA DE LAS CIUDADES Y LA DISTANCIA A LA QUE SE ENCUENTRA DEL RESTO DE CIUDADES
    #MANDA ESTOS DATOS A UN FICHERO distances.CSV EN LA CARPETA DATA
    for city in nodes.keys():
        city_list = []
        for city2 in nodes.keys():
            distancia = calculate_distance(list(nodes[city]), list(nodes[city2]))
            city_list.append(distancia)

        dataframe_distances[city] = city_list
        visited_dataframe[city] = (False,False)

    dataframe_distances.to_csv('data/distances.csv')

class Bidirectional_algorithm():
    def __init__(self,dataframe_distances, visited_dataframe ):
        self.dataframe_distances = dataframe_distances
        self.visited_dataframe = visited_dataframe
        self.current_city_first = ""
        self.current_city_second = ""

    def city_runner(self):
        #PREGUNTA POR LA CIUDAD A LA QUE QUEREMOS IR PRIMERO
        #FILTRAMOS EL DATAFRAME QUITANDO LA PROPIA CIUDAD EN LA QUE ESTAMOS
        #EN ESA CIUDAD CALCULA LA CIUDAD MÁS CERCANA
        #VAMOS FILTRANDO EL DATAFRAME PARA QUE ELIMINE LA CIUDAD QUE ACABAMOS DE RECORRER
        #DE MANERA QUE IREMOS ORDENANDO LA LISTA DE MENOR A MAYOR DISTANCIA, COGIENDO LA DE MENOR DISTANCIA
        #ESTO OCURRIRÁ MIENTRAS QUE EL NUMERO DE CIUDADES A LAS QUE HEMOS ACCEDIDO SEA MENOR QUE EL TOTAL
        number_visited = 0
        first_city = True
        self.city_traveled_list = []

        self.current_city_first = input("Enter a city to start")
        self.visited_dataframe.loc['Runner 1', self.current_city_first] = True

        print(f"Primero en visitar {self.current_city_first} \n {self.visited_dataframe}")
        number_visited +=1

        #FILTERED DATAFRAME ELIMINATING SELF CITY
        self.all_cities = self.dataframe_distances.columns
        number_cities = len(self.all_cities)
        column = dataframe_distances[self.current_city_first]
        column = column[column != 0]

        while number_visited < number_cities:

            #KEEPS FILTERIGN DATAFRAME TO AVOID VISITED CITIES
            for city in self.city_traveled_list:
                column = column[column.index != city]
            column = column.sort_values()
            print(f"Buscamos la ciudad más cercana\n -----------------------------------------------\n{column}")


            min_distance_value = column.iloc[0]
            min_distance_name = column.index[0]

            if self.visited_dataframe[min_distance_name]['Runner 1'] == False:
                self.visited_dataframe.loc['Runner 1', min_distance_name] = True
                print(f"Runner 1 Visitando {min_distance_name} \n {self.visited_dataframe}")
                self.current_city_first = min_distance_name
                self.city_traveled_list.append(min_distance_name)

                number_visited += 1
            else:
             print(f"{min_distance_name} ya ha sido visitada por Runner 1")
             break


nodes = {
    'huelva' : (20,50),
    'sevilla' : (10,20),
    'valencia': (20,30),
    'mursia' : (30,70),
    'cordoba': (40,80),
    'osuna' : (20,40),
    'badajoz' : (30,50)
}

distances = {
    'huelva' : [],
    'sevilla' : [],
    'valencia': [],
    'mursia' : []
}
dataframe_distances = pd.DataFrame(index = nodes.keys(), columns=nodes.keys())
visited_dataframe = pd.DataFrame(index = ("Runner 1", "Runner 2"), columns = nodes.keys())

dataframe_builder(nodes,visited_dataframe)
print(f"{dataframe_distances} \n --------------------------------------------------------" )
print(visited_dataframe)
bidir_algorithm = Bidirectional_algorithm(dataframe_distances,visited_dataframe)
bidir_algorithm.city_runner()