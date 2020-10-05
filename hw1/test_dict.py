import pytest


class TestDict:
    # Проверка метода clear
    def test_dictionary_clear(self):
        a = {1: 'Lol', 2: 'Dota', 3: 'CS', 4: 'HOMM'}
        a.clear()
        assert a == dict()

    # Проверка метода len
    def test_dictionary_len(self):
        a = dict()
        assert len(a) == 0

    # Негативный тест метода pop
    def test_dictionary_pop(self):
        a = {1: 'Lol', 2: 'Dota', 3: 'CS', 4: 'HOMM'}
        assert a.get(1) == 'Lol'
        a.pop(1)
        with pytest.raises(AssertionError):
            assert a.get(1) == 'Lol'

    # Проверка метода update
    def test_dictionary_update(self):
        a = {1: 'Lol'}
        a.update({2: 'HOMM'})
        assert a.get(2) == 'HOMM'

    # Негативный тест умножения словарей
    def test_dictionary_multiple(self):
        a = {1: 'Lol', 2: 'Dota', 3: 'CS', 4: 'HOMM'}
        b = {1: 'Doom', 2: 'SeriousSam'}
        with pytest.raises(TypeError):
            a *= b

    # Проверка поиска по ключу
    @pytest.mark.parametrize('i', range(1, 5))
    def test_dictionary_search_key(self, i):
        a = {1: 'Lol', 2: 'Dota', 3: 'CS', 4: 'HOMM'}
        assert a[i]
