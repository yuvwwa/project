from src.error_proxy import error_proxy
from src.argument_exception import argument_exception

class operation_exception(argument_exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)