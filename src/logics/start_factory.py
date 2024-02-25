from src.models.nomenclature_group_model import group_model
from src.models.measurement_unit_model import unit_model
from src.models.nomenclature_model import nomenclature_model
from src.settings import settings
from src.storage.storage import storage
from src.exceptions import exception_proxy
from src.exceptions import argument_exception
from src.reference import reference

#
# Класс для обработки начало работы приложения
#
class start_factory:
    __oprions: settings = None
    __storage: storage = None
    
    def __init__(self, _options: settings, _storage:storage = None) -> None:
        exception_proxy.validate(_options, settings)
        self.__oprions = _options
        self.__storage = _storage

    def __save(self, key:str, items: list):
        """
            Сохранить данные
        Args:
            key (str): ключ доступ
            items (list): список
        """
       
        exception_proxy.validate(key, str)
        
        if self.__storage == None:
            self.__storage = storage()
            
        self.__storage.data[ key ] = items
    
    @property            
    def storage(self):
        """
             Ссылка на объект хранилище данных
        Returns:
            _type_: _description_
        """
        return self.__storage

    @staticmethod
    def create_nomenclature():
        """
          Фабричный метод Создать список номенклатуры
        """
        
        result = []
        
        
        flour = nomenclature_model("Мука пшеничная")
        flour.group = group_model.create_group()
        flour.unit = unit_model.create_killogram()
        
        result.append(flour)

        sugar = nomenclature_model("Сахар")
        sugar.group = group_model.create_group()
        sugar.unit = unit_model.create_killogram()
        
        result.append(sugar)

        butter = nomenclature_model("Сливочное масло")
        butter.group = group_model.create_group()
        butter.unit = unit_model.create_killogram()
        
        result.append(butter)

        eggs = nomenclature_model("Яйца")
        eggs.group = group_model.create_group()
        eggs.unit = unit_model.create_thing()
        
        result.append(eggs)

        vanilla = nomenclature_model("Ванилин")
        vanilla.group = group_model.create_group()
        vanilla.unit = unit_model.create_gram()
        
        result.append(vanilla)

        powder = nomenclature_model("Сахарная пудра")
        powder.group = group_model.create_group()
        powder.unit = unit_model.create_gram()
        
        result.append(powder)

        cocoa = nomenclature_model("Какао")
        cocoa.group = group_model.create_group()
        cocoa.unit = unit_model.create_gram()
        
        result.append(cocoa)

        cinnamon = nomenclature_model("Корица")
        cinnamon.group = group_model.create_group()
        cinnamon.unit = unit_model.create_gram()
        
        result.append(cinnamon)

        chicken = nomenclature_model("Куриное филе")
        chicken.group = group_model.create_group()
        chicken.unit = unit_model.create_gram()
        
        result.append(chicken)
        
        return result
    
    
    def create(self):
        """
           В зависимости от настроек, сформировать начальную номенклатуру

        Returns:
            _type_: _description_
        """
        result = []
        if self.__oprions.is_first_start == True:
            self.__oprions.is_first_start = False
            return start_factory.create_nomenclature()
        self.__save( storage.nomenclature_key(), result )
        return result

    def build(self):
        if self.__storage == None:
            self.__storage = storage()

        self.__storage.data[storage.nomenclature_key] = start_factory.create_nomenclature()
        self.__storage.data[storage.group_key] = start_factory.create_nomenclature()
        self.__storage.data[storage.unit_key] = start_factory.create_nomenclature()
    