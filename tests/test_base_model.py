#!/usr/bin/python3
import os
import sys
# Get the absolute path to the directory containing this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Calculate the absolute path to the project's root directory (one level up)
project_root = os.path.abspath(os.path.join(current_dir, ".."))

# Add the project root directory to the Python path
sys.path.append(project_root)

#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
