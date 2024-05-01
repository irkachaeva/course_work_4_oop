import pytest
from src.Vacancy import Vacancy
import json
import os.path


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


@pytest.fixture
def vacancy_list_from_api():
    vacancies_path = os.path.join(os.path.dirname(os.getcwd()), 'data', 'test_vacancies.json')
    with (open(vacancies_path, "r", encoding="utf8") as f):  # взяли загруженные вакансии для дальнейшей работы
        vacancy_list_from_api = json.load(f)
    return vacancy_list_from_api


def test_get_list_vacancies(vacancy_list_from_api):
    assert repr(Vacancy.get_list_vacancies(vacancy_list_from_api)) == ('[Вакансия: Курьер\n'
 'Город: Москва\n'
 'Компания-pаботодатель: ФГУП РСУ Управления делами Президента Российской '
 'Федерации\n'
 'Требования: умение использовать технические средства (карты, навигатор) для '
 'прокладывания оптимального маршрута. - знание правил учета, хранения и '
 'доставки деловых бумаг, пакетов, писем...\n'
 'Зарплата:\n'
 'от: 48275\n'
 'до: 58620\n'
 'Валюта: RUR\n'
 'Ссылка на вакансию:https://hh.ru/vacancy/97825632\n'
 '\n'
 ']')
