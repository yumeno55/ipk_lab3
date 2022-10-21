import main.my_lib
import pytest

# Тест калькулятора, принимающего два числа и операцию (+, -, *, /)
class TestCalc():
    # Тестируем программу на корректных данных. Функция возвращает результирующее число
    def test_on_correct_args(self):
        assert main.my_lib.calc(4, 7, '*') == 28

    # Тестируем программу при делении на 0. Функция вызывает исключение ZeroDivisionError
    def test_on_zero_div(self):
        with pytest.raises(ZeroDivisionError):
            main.my_lib.calc(2, 0, '/')

    # Тестируем программу на некорректных данных. Функция вызывает исключение TypeError
    def test_on_incorrect_args(self):
        with pytest.raises(TypeError):
            main.my_lib.calc('2', 4, '/')