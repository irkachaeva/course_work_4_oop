import pytest
from src.Vacancy import Vacancy


@pytest.fixture
def vacancy():
    return Vacancy("Курьер",
                   "Не указано",
                   102000,
                   "RUR",
                   False,
                   "Москва",
                   "Фёсти",
                   "Нет опыта",
                   "Действующий статус самозанятого или готовность его оформить. Опыт не важен.",
                   "https://hh.ru/vacancy/94227184",
                   "Открытая")

def test_str(vacancy):
    assert str(vacancy) == 'Вакансия: Курьер\nГород: Москва\nКомпания-pаботодатель: Фёсти\nТребования: Действующий статус самозанятого или готовность его оформить. Опыт не важен.\nЗарплата:\nот: Не указано\nдо: 102000\nВалюта: RUR\nСсылка на вакансию:https://hh.ru/vacancy/94227184\n\n'
