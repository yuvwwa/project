class settings:
    #имена из файла settings.json делаем пустыми 
    __first_name=""
    __BIK=None
    __INN=None
    __bill=None
    __correspond=None
    __main_name=""
    __owner=""

    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, value: str):
        if not isinstance(value,str):
            raise Exception("Некорректный аргумент")
        
        self.__first_name = value.strip

    # BIK
    @property
    def BIK(self):
        return self.__BIK
    
    @BIK.setter
    def BIK(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент")
        
        if len(value) != 9:
            raise Exception("ERROR: Длина БИК не равна 9!")
        
        self.__BIK = value.strip()

    # ИНН
    @property
    def INN(self):
        return self.__INN
    
    @INN.setter
    def INN(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент")
        
        if len(value) != 12:
            raise Exception("ERROR: Длина ИНН не равна 12!")
        
        self.__INN = value.strip()

    # Счет
    @property
    def bill(self):
        return self.__bill
    
    @bill.setter
    def bill(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент")

        if len(value) != 11:
            raise Exception("ERROR: Длина счёта не равна 11!")
        
        self.__bill = value.strip()

    #Коpреспондентский счет
    @property
    def correspond(self):
        return self.__correspond
    
    @correspond.setter
    def bill(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент")
        
        if len(value) != 11:
            raise Exception("ERROR: Длина счёта не равна 11!")
        
        self.__correspond = value.strip

    #Наименование компании
    @property
    def main_name(self):
        return self.__main_name
    
    @main_name.setter
    def main_name(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент")
        
        self.__main_name = value.strip

    #Собственник
    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент")
        
        if len(value) != 5:
            raise Exception("ERROR: Длина названия не равна 5!")
        
        self.__owner = value.strip