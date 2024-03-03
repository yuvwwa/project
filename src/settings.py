from src.exceptions import exception_proxy

#
# Класс для описания настроек
#
class settings():
    _inn = 0
    _short_name = ""
    _first_start = True
    _report_format = ""
    
    @property
    def report_format(self):
        """
            report_format
        Returns:
            int: 
        """
        return self._report_format
    
    #добавляем csv, markdown, json
    @report_format.setter
    def report_format(self, value: str):
        value = value.lower()
        if value not in ["csv", "markdown", "json"]:
            raise exception_proxy("Error")

    @property
    def inn(self):
        """
            ИНН
        Returns:
            int: 
        """
        return self._inn
    
    @inn.setter
    def inn(self, value: int):
        exception_proxy.validate(value, int)
        self._inn = value
         
    @property     
    def short_name(self):
        """
            Короткое наименование организации
        Returns:
            str:
        """
        return self._short_name
    
    @short_name.setter
    def short_name(self, value:str):
        exception_proxy.validate(value, str)
        self._short_name = value
        
        
    @property    
    def is_first_start(self):
        """
           Флаг Первый старт
        """
        return self._first_start    
            
    @is_first_start.setter        
    def is_first_start(self, value: bool):
        self._first_start = value
