from src.reference import reference
from src.models.nomenclature_model import nomenclature_model
from src.models.measurement_unit_model import unit_model
from src.exceptions import exception_proxy
from src.exceptions import argument_exception

# 
# Класс описание одной строки рецепта
#
class receipe_model(reference):
    __ingridients = list()
    __steps = list()

    def __init__(self, name):
        super().__init__(name)

    @property
    def ingridients(self):
        return self.__ingridients
    
    @ingridients.setter
    def ingridients(self, ingridients:list):
        if not isinstance(ingridients, list):
            raise argument_exception ("Несоответсвие типа аргумента")
        self.__ingridients = ingridients

    @property
    def steps(self):
        return self.__steps
    
    @steps.setter
    def steps(self, steps:list):
        if not isinstance(steps, list):
            raise argument_exception ("Несоответсвие типа аргумента")
        self.__ingridients = steps

    @staticmethod
    def create(name, ingredients:list=None, steps:list=None):
        receipe = receipe_model(name)
        
        receipe.ingredients = ingredients if ingredients is not None else list()
        receipe.steps = steps if steps is not None else list()

        return receipe