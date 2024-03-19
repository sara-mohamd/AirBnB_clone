#!/usr/bin/python3

from datetime import datetime as dt
from models.base_model import BaseModel
from models import storage


obj1 = BaseModel()
obj1.name = "Sara's base"

# storage.new(obj1)
# all_objs = storage.all()
print(obj1)

# date = dt.now()
# print(date.strftime("%Y-%m-%dT%H:%M:%S.%f"))
