#CLASS FOR READING FILES AND SAVE NODES DISTANCES

class FileReader:
    def __init__(self,path):
        self.path = path
        self.nodes_list = []

    def get_nodes(self,):
        with open(self.path,'r') as f:
            self.lines = f.readlines()
            node_counter = 1
            for line in self.lines:
                if line.startswith(str(node_counter)):
                    node_distance = line.split(",")
                    self.nodes_list.append(node_distance)
                else:
                    break


reader = FileReader('nodes.txt')
reader.get_nodes()

