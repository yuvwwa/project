from src.models.measurement_unit_model import unit_model
from src.logics.start_factory import start_factory
from src.settings_manager import settings_manager

import unittest

#
# Набор автотестов для проверки работы фабричного метода
# #
class factory_test(unittest.TestCase):

    #
    # Проверка создания ед. измерения
    #
    def test_check_factory(self):
        # Подготовка
        unit = unit_model.create_killogram()
        
        # Действие
        
        # Проверки
        assert unit is not None
        
    # 
    # Проверка создание начальной номенклатуры
    #    
    def test_check_create_nomenclature(self):
        # Подготовка
        items = start_factory.create_nomenclature()
        
        # действие
        
        # Прверки
        assert len(items) > 0 
        
        
    #      
    # Проверка работы класса start_factory
    #
    def test_check_start_factor(self):
        # Подготовка
        manager = settings_manager()
        factory = start_factory( manager.settings )
        
        
        # Действие
        result = factory.create()
        
        
        # Проверка
        if manager.settings.is_first_start == True:
            assert len(result) > 0
            return
        
        
        assert len(result) == 0    