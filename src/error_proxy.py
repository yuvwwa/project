class error_proxy:
    _error_text=""
    _error_source=""

    def __init__(self, error_test: str="", error_source: str=""):
        self.error_source = error_source
        self.error_text = error_test

    @property
    def error_text(self):
        return self.__error_text
    @error_text.setter
    def error_text(self, value:str):
        if not isinstance(value, str):
            raise Exception("Некорректно передан аргумент!")
        if (value.strip()==""):
            self.__is_error = False
            return
        self.__error_text = value.strip()
        self.__is_error = True

    @property
    def error_source(self):
        return self.__error_source
    @error_source.setter
    def error_source(self, value:str):
        if not isinstance(value, str):
            raise Exception("Некорректно передан аргумент!")
        if (value.strip()==""):
            self.__is_error = False
            return
        self.__error_source = value.strip()
        self.__is_error = True

    @property
    def is_error(self):
        """
        Флаг. Есть ошибка.
        """
        return self.__is_error
    
    def set_error(self, exception: Exception):
        """
        
        """
        if not isinstance(exception, Exception):
            self.error_text="Некорректно переданы аргументы!"
            self.error_source="set_error"
            return
        if exception is not None:
            self.error_text = f"Ошибка {str(exception)}"
            self.error_source = f"Исключение {type(exception)}"
            return
