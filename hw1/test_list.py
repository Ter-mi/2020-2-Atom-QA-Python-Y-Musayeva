import pytest


class TestList:
    # Проверка метода len
    def test_list_len(self):
        a = list()
        assert len(a) == 0

    # Проверка создания списка
    def test_list_create(self):
        a = list()
        assert a == list()

    # Негативный тест умножения списков
    def test_list_multiple(self):
        a = [0, 1]
        b = [0, 1, 2]
        with pytest.raises(TypeError):
            assert a * b

    # Проверка метода append
    @pytest.mark.parametrize('i', range(0, 3))
    def test_list_append(self, i):
        a = [1]
        b = i
        a.append(b)
        assert a == [1, i]

    # Негативный тест эквивалентности списков
    def test_list_equivalence(self):
        a = list()
        b = [1, 2, 0]
        with pytest.raises(AssertionError):
            assert a == b

    # Негативный тест обращения списка
    def test_list_reverse(self):
        a = [0, 1, 2]
        a = a[::-1]
        with pytest.raises(AssertionError):
            assert a == [2, 0, 1]

    # Проверка копирования списка
    def test_list_copy(self):
        a = [0, 1, 2]
        b = list(a)
        assert b == [0, 1, 2]
