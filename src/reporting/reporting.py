from src.storage.storage import storage
from src.settings import settings
from src.models.nomenclature_group_model import group_model
from src.models.measurement_unit_model import unit_model
from src.models.nomenclature_model import nomenclature_model

class reporting:

    def __init(self, settings):
        self.__settings = settings

    def create(key, models) -> str:  #абстрактный метод create
        pass

class json_reporting (reporting):

    def __init(self, settings):
        self.__settings = settings

    def create(key) -> str:
        pass

class markdown_reporting (reporting):

    def __init(self, settings):
        self.__settings = settings

    def create(key) -> str:
        pass

class csv_reporting (reporting):

    def __init(self, settings):
        self.__settings = settings

    #формируем строку в формате csv
    def create(key) -> str:
        models = storage().data[key]
        csv = ""
        #добавляем заголовок
        if key == storage.unit_key():
            csv += "/n" + "base_unit, coefficient"
        elif key == storage.group_key():
            csv += "name"
        elif key == storage.nomenclature_key():
            csv += "group, unit"
            
        for model in models:
            if key == storage.unit_key():
                csv += f"\n{model.base_unit}, {model.coefficient}"
            elif key == storage.group_key():
                csv += f"\n{model.name}"
            elif key == storage.nomenclature_key():
                csv += f"\n{model.group}, {model.unit}"
        return csv