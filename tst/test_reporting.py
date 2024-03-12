import unittest
from src.logics.reporting import reporting
from src.models.unit_model import unit_model
from src.storage.storage import storage
from src.logics.csv_reporting import csv_reporting
from src.models.nomenclature_model import nomenclature_model
from src.models.group_model import group_model
from src.logics.markdown_reporting import markdown_reporting
from src.logics.json_reporting import json_reporting

class reporting_test(unittest.TestCase):
    
    
    def test_check_json_reporting_build(self):
        # Подготовка
        data = {}
        list = []
        item = unit_model.create_gram()
        list.append(item)
        key = storage.unit_key()
        data[  key  ] = list 
        report = json_reporting( data )
        
        # Действие
        result = report.create( key )
        
        # Проверки
        assert result is not None
        assert len(result) > 0   
    
    #
    # Проверить статический метод build класса reporting
    #
    def test_check_reporting_build(self):
        # Подготовка
        data = {}
        list = []
        item = unit_model.create_gram()
        list.append(item)
        data[  storage.unit_key()  ] = list 
        
        # Дейстие
        result = reporting.build( storage.unit_key(), data )
        
        # Проверки
        assert result is not None
        assert len(result) > 0
        
        
    #
    # Проверить формированеи отчета в csv формате по единицам измерения
    #    
    def test_check_csv_create_unit_key(self):
        # Подготовка
        data = {}
        list = []
        item = unit_model.create_gram()
        list.append(item)
        key = storage.unit_key()
        data[  key  ] = list 
        report = csv_reporting( data )
        
        # Действие
        result = report.create( key )
        
        # Проверки
        assert result is not None
        assert len(result) > 0
        
        
    #
    # Проверить формирование отчета в csv формате по номенклатуре
    #           
    def test_check_csv_create_nomenclature_key(self):
        # Подготовка
        data = {}
        list = []
        
        unit = unit_model.create_killogram()
        group = group_model.create_default_group()
        item = nomenclature_model("Тушка бройлера", group, unit )
        item.description = "Ингредиент для салата"
        list.append(item)
        
        key = storage.nomenclature_key()
        
        data[  key  ] = list 
        report = csv_reporting(  data )
        
        # Действие
        result = report.create( key )
        
        # Проверки
        assert result is not None
        assert len(result) > 0
           
        file = open("csv_report.csv", "w")
        file.write(result)
        file.close()
        
        
    #
    # Проверить формитирование отчета в markdown формате по ед / измерениям
    #    
    def test_check_markdown_create_unit_key(self):
         # Подготовка
        data = {}
        list = []
        item = unit_model.create_gram()
        list.append(item)
        key = storage.unit_key()
        data[  key  ] = list 
        report = markdown_reporting(  data )
        
        # Действие
        result = report.create( key )
        
        # Проверки
        assert result is not None
        assert len(result) > 0
        
        file = open("markdown_report.md", "w")
        file.write(result)
        file.close()
        