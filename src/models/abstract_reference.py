import uuid
from abc import ABC
from src.error_proxy import error_proxy
from src.argument_exception import argument_exception

class abstract_reference:
    __id: uuid.UUID
    __name:str = ""

    def __init__(self, name:str = None) -> None:
        self.name = name
        self.__id = uuid.uuid4()

    @property
    def error(self):
        """
            Работа с ошибками 
        """
        return self.__error

    @property
    def id(self):
        """
            Уникальный код
        """
        return self.__error

    @property
    def name(self):
        return self.__name.strip()
    
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise argument_exception("Неверный аргумент!")
        
        if not (len(value) >= 1 and len(value) <= 50):
            raise argument_exception("Несоответствующая длина аргумента")
        
        self.__name = value.strip()