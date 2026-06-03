import pytest
from src.app import main_func

def test_main_func():  # Хороша практика — давати тестам зрозумілі назви
    # Викликаємо функцію з дужками (), щоб перевірити її результат
    assert main_func() == "<h1>Hello world</h1>"