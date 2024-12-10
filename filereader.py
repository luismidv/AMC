#CLASS FOR READING FILES AND SAVE NODES DISTANCES
import re
def read_files(data):
    nodes_dict = {}
    with open(data,'r') as f:
        lines = f.readlines()
        nodes = (lines[6:-2])

    for line in nodes:
        splitted_line = line.split(" ")
        x_cord = splitted_line[1]
        y_cord = splitted_line[2]
        y_cord = re.sub(r'[^\d.-]', '', y_cord)
        nodes_dict[splitted_line[0]] = (float(x_cord),float(y_cord))
    return nodes_dict


read_files('./data/dataset_amc_1920/berlin52.tsp/berlin52.tsp')

