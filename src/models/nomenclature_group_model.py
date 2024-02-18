from src.models.abstract_reference import abstract_reference

#создаем пустой класс "группа номенклатура"

class nomenclature_group_model(abstract_reference):
    def __init__ (self, name):
        super().__init__(name)