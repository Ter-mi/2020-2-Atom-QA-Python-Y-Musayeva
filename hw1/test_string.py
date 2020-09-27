import pytest


class TestString:
    # Проверка сравнения разных строк
    def test_string_equivalence(self):
        a = 'HOMMIII'
        b = 'HOMMV'
        with pytest.raises(AssertionError):
            assert a == b

    # Проверка операции конкатенации
    def test_string_concatenation(self):
        a = 'League of'
        b = ' legends'
        assert a + b == 'League of legends'

    # Проверка сложения string с другими типами данных
    def test_string_addition_of_different_types(self):
        a = 'Lol'
        b = 5
        c = {1, 2}
        with pytest.raises(TypeError):
            assert a + b
        with pytest.raises(TypeError):
            assert a + c

    # Проверка умножения string на другие типы данных
    def test_string_multiple_of_different_types(self):
        a = 'Lol'
        b = list()
        c = dict()
        with pytest.raises(TypeError):
            assert a * b
        with pytest.raises(TypeError):
            assert a * c

    # Проверка наличия элемента в строке
    @pytest.mark.parametrize('a', ('L', 'e', 'a', 'g', 'u', 'e', 's', 'u', 'p', 'p', 'o', 'r', 't'))
    def test_string_presence(self, a):
        assert a in 'Leaguesupport'

    # проверка метода len
    def test_string_len(self):
        a = 'SennaADK'
        assert len(a) == 8

    # проверка деления строки на число
    def test_string_dividing_on_number(self):
        a = 'Soraka Support'
        with pytest.raises(TypeError):
            assert a / 2
