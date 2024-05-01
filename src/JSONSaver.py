import json
import os.path
from src.Vacancy import Vacancy


class JSONSaver:
    def __init__(self, path):
        self.path = path

    def load_vacancies(self):
        with (open(self.path, "r", encoding="utf8") as f):  # взяли загруженные вакансии для дальнейшей работы
            vacancy_list_from_api = json.load(f)
        return vacancy_list_from_api

    def write_vacancies(self, data):
        with open(self.path, "w", encoding="utf-8") as file:
            add_vacancies = []
            for vacancy in data:
                add_vacancies.append(vacancy.__dict__)
            json.dump(add_vacancies, file, ensure_ascii=False, indent=4)
            return



