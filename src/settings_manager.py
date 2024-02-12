import os
import json
import uuid
import pathlib
from src.settings import settings

class settings_manager(object):
    __file_name = "settings.json"
    __unique_number = None
    __data = {}
    __settings = settings()

    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance
    
    def __convert(self):
        if len(self.__data) == 0:
            raise Exception("Невозможно создать объект типа settings.py")
        #Проверяем, есть ли такие данные
        fields=self.data.keys()
        for field in fields:
            setattr(self.settings,field,self.data[field])
            print(getattr(self.settings,field)) 
    
    def __init__(self) -> None:
        self.__unique_number =  uuid.uuid4()

    def open(self, file_name: str) -> bool:
        if not isinstance(file_name, str):
            raise Exception("ERROR: Неверный аргумент file_name!")

        if file_name == "":
            raise Exception("ERROR: Неверный аргумент file_name")
        
        self.__file_name = file_name.strip()

        try:
            self.__open()
            self.__convert()
        except:
            return False
        return True
    
    @property
    def data(self):
        return self.__data
    
    @property
    def number(self)-> str:
        return str(self.__unique_number.hex)
    
    
    def __open(self):
        #Берем корневую папку проекта и добавляем к ней наш путь
        file_path=pathlib.Path.cwd()
        settings_file = "%s/%s" % (file_path, self.__file_name)
        if not os.path.exists(settings_file):
            raise Exception("Невозможно загрузить настройки!", settings_file)

        with open(settings_file, "r") as read_file:
            self.__data = json.load(read_file)
    @property
    def settings(self):
        return self.__settings
    
    @number.setter
    def number(self, value: int) -> str:
        self.__unique_number = value
    
