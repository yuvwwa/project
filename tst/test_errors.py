from src.error_proxy import error_proxy
import unittest
from src.argument_exception import argument_exception
from src.operation_exception import operation_exception

class test_settings(unittest.TestCase):

    def test_check_set_error_text(self):
        error = error_proxy("Test", "Test")
        assert error.is_error == True

    def test_check_set_exception(self):
        error = error_proxy()
        try:
            result = 1/0
        except Exception as ex:
            error.set_error(ex)
        
        assert error.is_error == True

    def test_check_argument_exception(self):
        try:
            raise argument_exception("Test")
        except argument_exception as ex:
            assert ex.error.is_error
            return
        assert 1!=1

    def test_check_operation_exception(self):
        try:
            raise operation_exception("Test")
        except operation_exception as ex:
            assert ex.error.is_error
            return
        assert 1!=1