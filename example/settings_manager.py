import os
import json
import uuid
from settings import settings

class settings_manager(object):
    __file_name = "settings.json"
    __unique_number = None
    __data = {}
    __setting = settings()

def __init__(self) -> None:
    self.__unique_number=uuid.uuid4()

def convert(self):
    if len(self.__data) == 0:
       raise Exception("error")
    fields = dir(self.__settings.__class__)
    # Проверяем, есть ли такие данные
    for field in fields:
        if not field in self.__data.keys():
            continue
        setattr(self.__settings, field, self.__data[field])

def __new__(cls):
    if not hasattr(cls,'instance'):
        cls.instance=super(settings_manager, cls).__new__(cls)
    return cls.instance

def open(self, file_name: str) -> bool:
    if not isinstance(file_name, str):
        raise Exception("error")
    if file_name=="":
        raise Exception("error")
    self.__file_name=file_name.strip()
    try:
        self.__open()
    except:
        return False
    
    return True

def __open(self):
    file_path=os.path.split(__file__)
    settings_file="%s/%s" % (file_path[0], self.__file_name)
    if not os.path.exists(settings_file):
        raise Exception("error")
    with open (settings_file, "r") as read_file:
        self.__data=json.load(read_file)

@property
def data(self) -> {}:
    return self.__data

@property
def number(self) -> str:
    return str(self.__unique_number.hex)

@property
def settings(self):
    return self.__settings

@number.setter
def number(self, value: int) -> None:
    self.__unique_number = value