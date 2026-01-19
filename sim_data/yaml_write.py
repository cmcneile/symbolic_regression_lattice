# https://www.geeksforgeeks.org/reading-and-writing-yaml-file-in-python/

import yaml

# Data to be written to the YAML file
data = {
    'name': 'Amit',
    'age': 25,
    'city': 'Mumbai',
    'skills': ['Python', 'Data Analysis', 'Machine Learning']
}

# Writing the data to a YAML file
with open('data.yaml', 'w') as file:
    yaml.dump(data, file)

print("Data has been written to 'data.yaml'")

