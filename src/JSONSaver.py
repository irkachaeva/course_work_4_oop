import json
import os
from src.HeadHunterAPI import HeadHunterAPI
from src.Vacancy import Vacancy
from json import JSONEncoder
from abc import ABC, abstractmethod


class JSONSaver(JSONEncoder):

    def __init__(self):
        self.vacancy = []

    @staticmethod
    def add_vacancy(vacancy):
        vacancies_for_use = []
        """Метод для добавления вакансий в файл"""

        with open("../data/vacancy.json", "w", encoding="utf8") as f:
            vacancy_json = json.dumps(vacancy, ensure_ascii=False)
            f.write(vacancy_json)

        with (open("../data/vacancy.json", "r", encoding="utf8") as f):
            list_vacancies = json.load(f)

            """приводим к классу вакансии и забисываем в очищенный файл для дальнейшей работы"""

            for hh_vacancy in list_vacancies:
                name = hh_vacancy['name']
                try:
                    salary_from = hh_vacancy['salary']['from']
                    salary_to = hh_vacancy['salary']['to']
                    salary_currency = hh_vacancy['salary']['currency']
                    salary_gross = hh_vacancy['salary']['gross']
                except:
                    TypeError()
                finally:
                    "Не указано"
                area = hh_vacancy['area']["name"]
                employer = hh_vacancy['employer']['name']
                experience = hh_vacancy["experience"]['name']
                snippet = hh_vacancy['snippet']["requirement"]
                alternate_url = hh_vacancy['alternate_url']
                type_v = hh_vacancy['type']["name"]
                vacancies = Vacancy(name, salary_from, salary_to, salary_currency, salary_gross, area, employer, experience, snippet, alternate_url, type_v)
                vacancies_for_use.append(vacancies.class_to_dict())

            with open("../data/vacancies_for_use.json", "w", encoding="utf8") as f:
                f.write(json.dumps(vacancies_for_use, ensure_ascii=False))

    def delete_vacancy(self, vacancy):
         pass

test = HeadHunterAPI()
list = test.load_vacancies("курьер")
J = JSONSaver()
J.add_vacancy(list)



