import json
import os
from src.HeadHunterAPI import HeadHunterAPI
from src.Vacancy import Vacancy
from abc import ABC, abstractmethod


class JSONSaver:

    def __init__(self):
        self.hh_vacancies =[]
        self.vacancy = []


    @staticmethod
    def add_vacancy(vacancy):
        vacancies_for_use = []
        """Метод для добавления вакансий в файл"""

        with open("../data/vacancy.json", "w", encoding="utf8") as f:
            vacancy_json = json.dumps(vacancy, ensure_ascii=False)
            f.write(vacancy_json)

        with open("../data/vacancy.json", "r", encoding="utf8") as f:
            list_vacancies = json.load(f)

            for hh_vacancy in list_vacancies:
                name = hh_vacancy['name']
                salary = hh_vacancy['salary']
                area = hh_vacancy['area']
                employer = hh_vacancy['employer']
                experience = hh_vacancy['experience']
                snippet = hh_vacancy['snippet']
                alternate_url = hh_vacancy['alternate_url']
                type_v = hh_vacancy['type']
                vacancies = Vacancy(name, salary, area, employer, experience, snippet, alternate_url, type_v)
                vacancies_for_use.append(vacancies.class_to_dict())
            with open("../data/vacancies_for_use.json", "w", encoding="utf8") as f:
                f.write(json.dumps(vacancies_for_use, ensure_ascii=False))


    def delete_vacancy(self, vacancy):
         pass

test = HeadHunterAPI()
list = test.load_vacancies("курьер")
J = JSONSaver()
J.add_vacancy(list)
print(J)


