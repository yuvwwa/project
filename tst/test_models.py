import unittest
from src.models.abstract_reference import abstract_reference
from src.models.nomenclature_model import nomenclature_model
from src.models.nomenclature_group_model import nomenclature_group_model
from src.models.measurement_unit_model import measurement_unit_model
from src.models.storage_model import storage_model
from src.models.company_model import company_model
from src.settings_manager import settings_manager

class test_models(unittest.TestCase):
    #пустые тесты для склада и группы номенклатуры
    def test_storage_model(self):
        pass

    def test_nomenclature_group_model(self):
        pass

    def test_nomenclature_model(self):
        #создаем новую номенклатуру
        nomenclature = nomenclature_model("Test")

        # строка с полным именем
        full_name = "Test"
        #присваиваем полное имя номенклатуры значение имени фулл_нэйм
        nomenclature.full_name = full_name
        #проверка
        assert nomenclature.full_name == full_name

        #строка с единицей измерения
        measurement_unit = "Test"
        #конструктор. передаем name "test"
        measurement_unit = measurement_unit_model("test")
        nomenclature.measurement_unit = measurement_unit
        #проверка
        assert nomenclature.measurement_unit == measurement_unit

        #строка с группой номенклатуры
        nomenclature_group = "Test"
        #конструктор. передаем name "test"
        nomenclature_group = nomenclature_group_model("test")
        nomenclature.nomenclature_group = nomenclature_group
        #проверка
        assert nomenclature.nomenclature_group == nomenclature_group

    def test_measurement_unit_model(self):
        #создаем грамм и килограмм 
        g = measurement_unit_model("Грамм")
        kg = measurement_unit_model("Килограмм")
        #ставим базовую единицу измерения килограмму грамм
        kg.base_measurement_unit = g
        #ставим базовый коэффициент 1000
        kg.base_coefficient = 1000
        #проверка
        assert kg.base_measurement_unit == g
        assert kg.base_coefficient == 1000

    def test_abstract_reference(self):
        #подготовка
        name = "eman"
        #действие
        abs = abstract_reference(name)
        #проверка
        assert abs.name == name

    def company_model(self): 
        #сoзданили новый settings_manager
        set = settings_manager()
        #открываем файл settings.json
        set.open ("/tst/settings.json")
        #созданием переменную, в которую записываем новый объект компании
        company = company_model ("Название", set.settings)
        #проверяем, что company - модель компании
        assert isinstance(company, company_model)
        #проверяем, что инн, бик, счет и вид собственности такие же, как в настройках
        assert company.inn == set.inn 
        assert company.bik == set.bik 
        assert company.bill == set.bill 
        assert company.owner == set.owner