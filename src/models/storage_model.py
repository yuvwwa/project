from src.models.abstract_reference import abstract_reference

#создаем пустой класс "склад"

class storage_model(abstract_reference):
    def __init__ (self, name):
        super().__init__(name)