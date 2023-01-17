import os
import pandas as pd


current_dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(current_dir_path, os.pardir))


def read_raw_data():
    with open(parent_dir_path + '\\data\\testing\\raw\\data.json', 'r') as file:
        raw_text = file.readline()
        
    data = eval(raw_text)
    keys = []
    values = []
    for keyvalues in data.items():
        keys.append(keyvalues[0])
        values.append(keyvalues[1])
    return keys, [tuple(values)]

filepath = parent_dir_path + '\\data\\testing\\harmonized\\data.txt'
def write_to_harmonized(column_names, data, filepath):
    with open(filepath, 'w') as file:
        file.write(str(column_names) + '\n')
        for row in data:
            file.write(str(row))

        

keys, data = read_raw_data()
write_to_harmonized(keys, data, filepath)