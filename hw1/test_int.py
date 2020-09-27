import pytest


class TestInt:
    # Проверка сложения
    def test_int_addition(self):
        a = 5
        b = 5
        assert a + b == 10

    # Проверка операторов <>=
    def test_int_sign(self):
        a = 5
        assert a > 0
        a = 0
        assert a == 0
        a = -1
        assert a < 0

    # Проверка сложения int с другими типами данных
    def test_int_addition_of_different_types(self):
        a = 'HOMM'
        b = dict()
        with pytest.raises(TypeError):
            assert a + 2
        with pytest.raises(TypeError):
            assert 100500 + b

    # Проверка операции взятия остатка от деления
    @pytest.mark.parametrize('i', range(0, 5))
    def test_int_remainder_of_division(self, i):
        assert i % 1 == 0

    # Проверка деления на нуль
    @pytest.mark.parametrize('i', range(0, 6))
    def test_int_division_by_zero(self, i):
        with pytest.raises(ZeroDivisionError):
            assert i / 0
