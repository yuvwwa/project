class settings:
    __first_name=""
    __inn=""
    __bill=""
    __cor_bill=""
    __bik=""
    __main_name=""
    __owner=""

#имя 
    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, value:str):
        if not isinstance(value, str):
            raise Exception("error")
        
        self.__first_name = value.strip()
    
#инн
    @property
    def inn(self):
        return self.__inn
    
    @inn.setter
    def inn(self, value:str):
        if not isinstance(value, str):
            raise Exception("error")

        value = value.strip()
        
        if len(value) != 12:
            raise Exception("ERROR: должно быть 12 символов!")
        
        self.__inn = value.strip()

#счёт
    @property
    def bill(self):
        return self.__bill
    
    @bill.setter
    def bill(self, value:str):
        if not isinstance(value, str):
            raise Exception("error")
        
        if len(value) != 11:
            raise Exception("ERROR: должно быть 11 символов!")
        
        self.__bill = value.strip()

#счёт
    @property
    def cor_bill(self):
        return self.__cor_bill
    
    @cor_bill.setter
    def cor_bill(self, value:str):
        if not isinstance(value, str):
            raise Exception("error")
        
        if len(value) != 11:
            raise Exception("ERROR: должно быть 11 символов!")
        
        self.__cor_bill = value.strip()

#бик
    @property
    def bik(self):
        return self.__bik
    
    @bik.setter
    def bik(self, value:str):
        if not isinstance(value, str):
            raise Exception("error")
        
        if len(value) != 9:
            raise Exception("ERROR: должно быть 9 символов!")
        
        self.__bik = value.strip()

#наименование
    @property
    def main_name(self):
        return self.__main_name
    
    @main_name.setter
    def main_name(self, value:str):
        if not isinstance(value, str):
            raise Exception("error")
        
        self.__main_name = value.strip()

#вид собственности 
    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, value:str):
        if not isinstance(value, str):
            raise Exception("error")
        
        if len(value) != 5:
            raise Exception("ERROR: должно быть 5 символов!")
        
        self.__owner = value.strip()
