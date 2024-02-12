from src.settings import settings
from src.settings_manager import settings_manager
import unittest

class test_settings(unittest.TestCase):

    def test_check_first_name(self):
        #подготовка
        item=settings()
        #действие
        item.first_name="k "
        #проверка
        assert item.first_name=="k"
    
    def test_check_open_settings(self):
        manager = settings_manager()

        result = manager.open("/tst/settings.json")

        assert result != False

    def test_check_create_manager(self):
        manager1 = settings_manager()
        manager2 = settings_manager()

        print(manager1.number)
        print(manager2.number)

        assert(manager1.number == manager2.number)

    def test_check_manager_convert(self):
        manager = settings_manager()
        manager.open("tst/settings.json")
        
        fields=manager.data.keys()
        print(fields)
        for field in fields:
            print(getattr(manager.settings,field))
            print(manager.data[field])
            assert getattr(manager.settings,field)==manager.data[field]


