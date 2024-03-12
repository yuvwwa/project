from models.unit_model import unit_model
from src.logics.start_factory import start_factory
from src.settings_manager import settings_manager
from src.storage.storage import storage
from models.group_model import group_model
from src.models.nomenclature_model import nomenclature_model

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
    def test_check_start_factory(self):
        # Подготовка
        manager = settings_manager()
        factory = start_factory( manager.settings )
        
        
        # Действие
        result = factory.create()
        
        
        # Проверка
        if manager.settings.is_first_start == True:
            assert len(result) > 0      
        
        assert len(result) == 0    
        assert not factory.storage is None
        
        assert storage.nomenclature_key() in factory.storage.data
        assert storage.group_key() in factory.storage.data
        assert storage.unit_key() in factory.storage.data

    def test_check_create(self):
        storage_create= storage()   
        
        assert len(storage_create.data[storage.nomenclature_key()]) > 0
        assert len(storage_create.data[storage_create.unit_key()]) > 0
        assert len(storage_create.data[storage_create.group_key()]) > 0
        assert len(storage_create.data[storage_create.ingridient_key()]) > 0
        assert len(storage_create.data[storage_create.receipe_key()]) > 0