from src.models.abstract_reference import abstract_reference
from src.argument_exception import argument_exception
from numbers import Number

class measurement_unit_model(abstract_reference):
    #базовая единица измерения (грамм для килограмма)
    __base_measurement_unit = None
    #базовый коэффициент
    __base_coefficient = None

    #создаем свойства
    #создаем сеттеры. присваеваем значения 

    @property
    def base_measurement_unit(self):
        """ Базовая единица измерения """
        return self.__base_measurement_unit

    @base_measurement_unit.setter
    def base_measurement_unit(self, value):
        #проверка
        if not isinstance(value, measurement_unit_model):
            raise argument_exception ("Несоответсвие типа аргумента")
        
        self.__base_measurement_unit = value
    
    @property
    def base_coefficient(self):
        """ Базовый кэффициент """
        return self.__base_coefficient
    
    @base_coefficient.setter
    def base_coefficient(self, value):
        #проверка
        if not isinstance(value, Number):
            raise argument_exception ("Несоответсвие типа аргумента")
        
        self.__base_coefficient = value

        