import os
from datetime import datetime


def log(filename=None):
    """Декоратор для логирования результата функции"""

    def decorators(func):
        def wrapper(*args, **kwargs):
            time = datetime.now()
            try:
                result = func(*args, **kwargs)
                result_str = f"{func.__name__} ok"
            except Exception as e:
                e_type = type(e).__name__
                result_str = f"{func.__name__} error: {e_type}. Inputs:({args},{kwargs}). {e}"
                result = None
            if filename:
                file = os.path.join(os.path.dirname(__file__), "..", "data", filename)
                # Относительный путь к файлу:
                # os.path.dirname(file) - текущее положение в проекте
                # +
                #  ".." - подъем в корень проекта
                # +
                # "data" - заходим в папку data
                # +
                # filename - заходим в наш файл
                with open(file, "w", encoding="UTF-8") as f:
                    f.write(result_str)
            else:
                print(result_str)
            return result

        return wrapper

    return decorators
