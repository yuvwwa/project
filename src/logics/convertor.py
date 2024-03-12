import abc
from src.errors import error_proxy
from src.exceptions import exception_proxy

# 
# Абстрактный класс для конвертации данных в json
#
class convertor(error_proxy):
    
    @abc.abstractmethod
    def serialize(self, field: str, object) -> dict:
        """
            Сконвертировать объект в словарь
        Args:
            source (_type_): Любой тип данных
        """
        exception_proxy.validate(field, str)
        self.clear()
         