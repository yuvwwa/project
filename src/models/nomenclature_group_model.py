from src.reference import reference

#модель группы номенклатуры
class group_model(reference):

    def create_group():
        """
        Фабричный метод. Создать группу по умолчанию

        Returns:
            _type_: _description_
        """
        item = group_model("Ингридиенты")
        return item
    
    