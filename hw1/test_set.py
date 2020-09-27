import pytest


class TestSet:
    # Негативный тест "сложения" двух множеств
    def test_set_addition(self):
        a = {1, 2, 3}
        b = {4, 5, 6}
        with pytest.raises(TypeError):
            assert a + b == {1, 2, 3, 4, 5, 6}

    # Проверка эквивалентности двух множеств
    def test_set_equivalence(self):
        a = {1, 2, 2}
        b = {1, 2, 2}
        assert a == b

    # Проверка наличия элемента
    @pytest.mark.parametrize('i', range(1, 3))
    def test_set_availability(self, i):
        a = {0, 1, 2, 3, 4, 5}
        assert i in a

    # Проверка удаления элемента множества
    @pytest.mark.parametrize('i', range(1, 3))
    def test_set_delete(self, i):
        a = {0, 1, 2, 3, 4, 5}
        a.add(i)
        assert i in a

    # Проверка пересечения двух множеств
    def test_set_crossing(self):
        a = {1, 2, 3, 4, 6}
        b = {3, 4, 5}
        a &= b
        assert a == {3, 4}
