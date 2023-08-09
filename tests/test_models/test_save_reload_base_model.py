#!/usr/bin/python3
import os
import sys

# Get the absolute path to the directory containing this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Calculate the absolute path to the project's root directory (two levels up)
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))

# Add the project root directory to the Python path
sys.path.append(project_root)
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
