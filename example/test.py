from settings import settings
from settings_manager import settings_manager
import unittest


class test_settings(unittest.TestCase):

    def test_check_first_name(self):
        #подготовка
        item=settings()
        #действие
        item.first_name="a "
        #проверка
        assert item.first_name=="a"

    def test_check_open_settings(self):
        manager=settings_manager()
        result=manager.open("../exampe/settings.json")
        print(manager.data)
        assert result == True

    def test_check_create_manager(self):
        manager1=settings_manager()
        manager2=settings_manager()
        print(str(manager1.number))
        print(str(manager2.number))
        assert manager1.number==manager2.number

    def test_check_open_convert(self):
        manager=settings_manager()
        manager.open("../exampe/setttings.json")
        settings = manager.settings
        data = manager.data
        v = [i for i in dir(settings) if not i.startswith("_") and getattr(settings, i) != data[i] ]
        assert len(v) == 0
        manager.convert()

unittest.main()
