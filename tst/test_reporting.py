import unittest
from src.reporting.reporting import csv_reporting
from src.storage.storage import storage
from models.unit_model import unit_model

class reporting_test(unittest.TestCase):
    def test_reporting(self):

        # Создаем новый storage
        strg = storage()

        # Создаем 3 единицы измерения
        u1 = unit_model ("Test 1")
        u2 = unit_model ("Test 2")
        u3 = unit_model ("Test 3")

        # Записываем единицы измерения в storage
        strg.data[strg.unit_key()] = [u1, u2, u3]

        # Генерируем текст csv файла
        rep = csv_reporting()
        csv = csv_reporting.create(strg.unit_key())

        # Проверяем, что в получившемся csv 3 строки
        assert len(csv.split("\n"))