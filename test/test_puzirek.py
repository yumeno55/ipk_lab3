import main.my_lib
import pytest

# Тест функции, сортирующей список пузырьком
class TestPuzirek():
    # Тест функции на неупорядоченных значениях. Функция возвращает отсортированный список
    def test_on_correct_unsorted_arr(self):
        assert main.my_lib.puzirek([2, 5, 1, 4]) == [1, 2, 4, 5]

    # Тест функции на упорядоченных значениях. Функция возвращает отсортированный список
    def test_on_correct_sorted_arr(self):
        assert main.my_lib.puzirek([1, 2, 3, 5]) == [1, 2, 3, 5]

    # Тест функции на некорректных данных. Функция вызывает исключение TypeError
    def test_on_int(self):
        with pytest.raises(TypeError):
            main.my_lib.puzirek(12)

    # Тест функции на пустом списке. Функция возвращает пустой список
    def test_on_empty_arr(self):
        assert main.my_lib.puzirek([]) == []

    # Тест функции на одинаковых значениях. Функция возвращает тот же список
    def test_on_equal_values(self):
        assert main.my_lib.puzirek([2, 2, 2, 2]) == [2, 2, 2, 2]