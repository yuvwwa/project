from src.models.abstract_reference import abstract_reference
from src.argument_exception import argument_exception
from src.models.measurement_unit_model import measurement_unit_model
from src.models.nomenclature_group_model import nomenclature_group_model

class nomenclature_model(abstract_reference):
    __full_name = ""
    __measurement_unit = None
    __nomenclature_group = None

    #создаем свойства
    #создаем сеттеры. присваеваем значения 

    @property
    def full_name(self):
        """ полное имя """
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        #проверка
        if not isinstance(value, str):
            raise argument_exception ("Несоответсвие типа аргумента")
        
        if not len(value) < 256:
            raise argument_exception ("Превышена длина аргумента")
        
        self.__full_name = value
    
    @property
    def measurement_unit(self):
        """ Единица измерения """
        return self.__measurement_unit
    
    @measurement_unit.setter
    def measurement_unit(self, value):
        #проверка
        if not isinstance(value, measurement_unit_model):
            raise argument_exception ("Несоответсвие типа аргумента")
        
        self.__measurement_unit = value
    
    @property
    def nomenclature_group(self):
        """ Группа номенклатуры """
        return self.__nomenclature_group
    
    @nomenclature_group.setter
    def nomenclature_group(self, value):
        #проверка
        if not isinstance(value, nomenclature_group_model):
            raise argument_exception ("Несоответсвие типа аргумента")
        
        self.__nomenclature_group = value
    
    #конструктор
    def __init__ (self, name):
        super().__init__(name)