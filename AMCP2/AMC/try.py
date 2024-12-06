import pandas as pd

nodes = {
    'huelva' : (20,50),
    'sevilla' : (10,20),
    'valencia': (20,30),
    'mursia' : (30,70)
}

data = pd.DataFrame(nodes)
print(data)
column = data['huelva'].sort_values()
print(column[1])
