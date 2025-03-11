from src.functions import *


class FunctionHandler:

    def __init__(self, func: [str, callable]):
        if isinstance(func, str):
            try:
                func_obj = globals()[func]
            except KeyError:
                raise ValueError(f"Function '{func}' not found in globals.")
            if not callable(func_obj):
                raise ValueError(f"'{func} is not callable'")
            self.func = func_obj
        elif callable(func):
            self.func = func
        else:
            raise ValueError("The argument must be a string or a callable")

    def execute(self, *args, **kwargs):
        return self.func(*args, **kwargs)