import math
import pandas as pd
import filereader
import sys
import numpy as np

class exhaustivePode():
    def __init__(self, dataframe_distances):
        self.dataframe_distances = dataframe_distances
        print(self.dataframe_distances)

    def distance_pode(self):
        #DEFINIMOS DISTANCIA MAXIMA PARA LA PODA

        #UTILIZAREMOS UN FACTOR K PARA AUMENTAR LA CANTIDAD DE CIUDADES O NO
        k_factor = 0.5

        #CALCULAMOS LA MEDIA DE DISTANCIAS CALCULADAS IGNORANDO LAS IGUALES A 0
        mean_distance = self.dataframe_distances.values[self.dataframe_distances.values > 0].mean()

        #CALCULAMOS LA DESVIACIÓN TÍPICA PARA LAS DISTANCIAS IGNORANDO LAS IGUALES A 0
        std_deviation = self.dataframe_distances.values[self.dataframe_distances.values > 0].std()

        #COMPUATAMOS EL MAXIMO COMO K * (MEAN + STD)
        self.max_distance_pode = mean_distance + std_deviation*k_factor

    def cities_exhaustive(self):
        self.starting_city = str(int(np.random.randint(1,len(self.dataframe_distances.index)-1,1)))
        print(f"Starting city {self.starting_city}")
        self.all_cities = len(self.dataframe_distances.index)
        self.current_iterations = 0
        self.cities_runned = []

        print(f"First city {self.starting_city}")
        self.current_iterations +=1
        self.cities_runned.append(self.starting_city)

        #FILTRAMOS EL DATAFRAME PARA OBTENER LAS DISTANCIAS PARA SOLO UNA CIUDAD
        column = self.dataframe_distances[self.starting_city]

        #ELIMINAMOS LA DISTANCIA DE LA CIUDAD CONSIGO MISMA
        column = column[column != 0]

        #ORDENAMOS LAS DISTANCIAS
        column = column[column != 0].sort_values()

        #ITERAMOS SIEMPRE QUE EL NUMERO DE ITERACCIONES SEA MENOR QUE EL TOTAL DE CIUDADES
        while self.current_iterations < self.all_cities:

            #FILTRAMOS PARA NO CALCULAR CON LAS CIUDADES YA RECORRIDAS
            for city in self.cities_runned:
                column = column[column.index != city]
            column= column.sort_values()


            #OBTENEMOS NOMBRE Y DISTANCIA PARA LA CIUDAD MÁS CERCANA
            self.current_city_distance = column.iloc[0]
            self.current_city_name = column.index[0]

            if self.current_city_distance >= self.max_distance_pode:
                print(f"Maxima distancia definida alcanzada para ir a la ciudad {self.current_city_name} | {self.current_city_distance}."
                      f"Volvemos a {self.starting_city}")
                break


            print(f"Next city to move {self.current_city_name}")
            
            self.current_iterations += 1
            self.cities_runned.append(self.current_city_name)

    def filecreator(self, fileroute, nodes):
        with open(fileroute, "w") as f:
            f.write("NAME : " + self.starting_city + ".opt.tour \nTYPE : TOUR\nDIMENSION : " + str(
                self.all_cities) + "\nSOLUTION : \n")
            counter = 1
            for city in self.cities_runned:
                content = str(counter) + " " + city + " " + str(nodes[city]) + "\n"
                f.write(content)
                counter += 1
            f.close()


def calculate_distance(first_city,second_city):
    #FUNCION QUE UTILIZAREMOS PARA EL CALCULO DE LAS DISTANCIAS ENTRE CIUDADES
    distance = (second_city[0] - first_city[0])**2 + (second_city[1] - first_city[1])**2
    return math.sqrt(distance)


def dataframe_builder(nodes):
    #RECIBE UN DICCIONARIO PYTHON CON LAS CIUDADES Y SUS COORDENADAS
    #CREA UN DATAFRAME PANDAS CON CADA UNA DE LAS CIUDADES Y LA DISTANCIA A LA QUE SE ENCUENTRA DEL RESTO DE CIUDADES
    #MANDA ESTOS DATOS A UN FICHERO distances.CSV EN LA CARPETA DATA
    for city in nodes.keys():
        city_list = []
        for city2 in nodes.keys():
            distancia = calculate_distance(list(nodes[city]), list(nodes[city2]))
            city_list.append(distancia)

        dataframe_distances[city] = city_list


    dataframe_distances.to_csv('data/distances.csv')




nodes = {
    'huelva' : (20,50),
    'sevilla' : (10,20),
    'valencia': (20,30),
    'mursia' : (30,70),
    'cordoba': (40,80),
    'osuna' : (20,40),
    'badajoz' : (30,50)
}

if __name__ == "__main__":
    filename = sys.argv[1]


filename = './data/dataset_amc_1920/berlin52.tsp/berlin52.tsp'
print("Starting exhaustive pode script")
nodes_dict = filereader.read_files(filename)
dataframe_distances = pd.DataFrame(index = nodes_dict.keys(), columns=nodes_dict.keys())
visited_dataframe = pd.DataFrame(index = ("Runner 1", "Runner 2"), columns = nodes_dict.keys())

dataframe_builder(nodes_dict)
bidir_algorithm = exhaustivePode(dataframe_distances)
bidir_algorithm.distance_pode()
bidir_algorithm.cities_exhaustive()

bidir_algorithm.filecreator('./data/exhaustivepode_results.txt', nodes_dict)
print(f"El corredor  ha llegado a las ciudades \n {bidir_algorithm.cities_runned}")
#TODO SUBIR FICHEROS A NUBE TRAS EJECUCION

