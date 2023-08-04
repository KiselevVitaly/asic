import inspect
import time


class Log():
    def __init__(self, logger) -> None:
        self.logger = logger

    def __call__(self, func):
        def decorated(*args, **kwargs):
            dt = time.ctime(time.time())
            # func_name_ = inspect.stack()[1][3]
            self.logger.info(f'{dt} Функция {func.__name__}({args} {kwargs})')
            res = func(*args, **kwargs)
            return res
        return decorated
