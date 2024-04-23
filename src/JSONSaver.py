import json
import os
from src.HeadHunterAPI import HeadHunterAPI
from src.Vacancy import Vacancy
from json import JSONEncoder
from abc import ABC, abstractmethod


class JSONSaver:

    def __init__(self):
        self.vacancy = []


    @staticmethod
    def add_vacancy(data):
        vacancies_for_use = []
        tax = 0.87
        """Метод для добавления вакансий в файл"""

        with open("../data/vacancy.json", "w", encoding="utf8") as f: #сохранили вакансии в исходную выгрузку
            vacancy_json = json.dumps(data, ensure_ascii=False)
            f.write(vacancy_json)

        with (open("../data/vacancy.json", "r", encoding="utf8") as f): #взяли загруженные вакансии для дальнейшей работы
            list_vacancies = json.load(f)

            """приводим к классу вакансии и забисываем в очищенный файл для дальнейшей работы"""

        for hh_vacancy in list_vacancies:
            name = hh_vacancy['name']

            if hh_vacancy['salary'] is None:
                salary_from = "Не заполнено"
                salary_to = "Не заполнено"
                salary_currency = "Не заполнено"
                salary_gross = "Не заполнено"
            else:
                if hh_vacancy['salary']['from'] is None:
                    salary_from = "Не заполнено"
                else:
                    if hh_vacancy['salary']['gross'] is False:
                        salary_from = int(hh_vacancy['salary']['from']/tax)
                    else:
                        salary_from = int(hh_vacancy['salary']['from'])

                if hh_vacancy['salary']['to'] is None:
                    salary_to = "Не заполнено"
                else:
                    if hh_vacancy['salary']['gross'] is False:
                        salary_to = int(hh_vacancy['salary']['to']/tax)
                    else:
                        salary_to = int(hh_vacancy['salary']['to'])
                if hh_vacancy['salary']['currency'] is None:
                    salary_currency = "Не заполнено"
                else:
                    salary_currency = hh_vacancy['salary']['currency']
            salary_gross = "ЗП к начислению"
            area = hh_vacancy['area']["name"]
            employer = hh_vacancy['employer']['name']
            experience = hh_vacancy["experience"]['name']
            snippet = hh_vacancy['snippet']["requirement"]
            alternate_url = hh_vacancy['alternate_url']
            type_v = hh_vacancy['type']["name"]
            vacancies = Vacancy(name, salary_from, salary_to, salary_currency, salary_gross, area, employer, experience,
                                snippet, alternate_url, type_v)
            vacancies_for_use.append(vacancies.class_to_dict())

        with open("../data/vacancies_for_use.json", "w", encoding="utf8") as f:
            f.write(json.dumps(vacancies_for_use, ensure_ascii=False))

    def delete_vacancy(self):
            """Метод удаления данных из файла"""
            list_vacancies_del = []
            list = json.dumps(list_vacancies_del, ensure_ascii=False)
            with open("../data/vacancies_for_use.json", "w", encoding="utf8") as f:
                f.write(list)
            with open("../data/vacancy.json", "r", encoding="utf8") as file:
                file.write(list)


test = HeadHunterAPI()
list = test.load_vacancies("Водитель")
J = JSONSaver()
J.add_vacancy(list)



