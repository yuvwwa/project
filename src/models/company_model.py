from src.models.abstract_reference import abstract_reference

class company_model(abstract_reference):
    #объявляем, что у нас есть инн, бик, счет, вид собственности
    __inn = 0 #инн
    __bik = 0 #бик
    __bill = 0 #счет
    __owner = 0 #вид собственности

#конструктор
    
    def __init__ (self, name, data):
        """
            Конструктор
            Args:
            name: Имя
            data: Данные настроек 

        """
        self.__inn=data.inn
        self.__bik=data.bik
        self.__bill=data.bill
        self.__owner=data.owner
        #super - обращение к родительскому классу
        super().__init__(name)
         
#создаем свойства 
        
    @property
    def bik(self):
        """ БИК """
        return self.__bik
    
    @property
    def bill(self):
        """ Счет """
        return self.__bill
    
    @property
    def inn(self):
        """ ИНН """
        return self.__inn
    
    @property
    def owner(self):
        """ Вид собственности """
        return self.__owner