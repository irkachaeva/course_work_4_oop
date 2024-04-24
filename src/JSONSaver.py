import json
import os.path
from src.Vacancy import Vacancy


class JSONSaver:

    def __init__(self):
        self.vacancy = []

    @staticmethod
    def add_vacancy(data):
        global salary_from, salary_to
        tax = 0.87
        vacancies_for_use = []

        for item in data:
            name = item['name']
            if item['salary'] is None:
                salary_from = "Не заполнено"
                salary_to = "Не заполнено"
                salary_currency = "Не заполнено"
            try:
                if item['salary']['gross'] is False:
                    if item['salary']['from'] is not None:
                        salary_from = int(item['salary']['from'] / tax)
                    else:
                        salary_from = int(item['salary']['from'])

                    if item['salary']['to'] is not None:
                        salary_to = int(item['salary']['to'] / tax)
                    else:
                        salary_to = int(item['salary']['to'])

                    if item['salary']['currency'] is None:
                        salary_currency = "Не заполнено"
                    else:
                        salary_currency = item['salary']['currency']
                    if item['snippet']["requirement"] is None:
                        snippet = "Не заполнено"
                    else:
                        snippet = item['snippet']["requirement"]
            except:
                TypeError()

            salary_gross = "ЗП к начислению"
            area = item['area']["name"]
            employer = item['employer']['name']
            experience = item["experience"]['name']
            alternate_url = item['alternate_url']
            type_v = item['type']["name"]

            vacancies = Vacancy(name, salary_from, salary_to, salary_currency, salary_gross, area, employer, experience,
                                snippet, alternate_url, type_v)
            vacancies_for_use.append(vacancies.class_to_dict())

        vacancies_for_use_path = os.path.join(os.getcwd(), 'data', 'vacancies_for_use.json')
        with open(vacancies_for_use_path, "w", encoding="utf8") as f:
            f.write(json.dumps(vacancies_for_use, ensure_ascii=False))

    def delete_vacancy(self):

        """Метод удаления данных из файла"""

        vacancies_for_use_path = os.path.join(os.path.dirname(os.getcwd()), 'data', 'vacancies_for_use.json')
        vacancies_path = os.path.join(os.path.dirname(os.getcwd()), 'data', 'vacancy.json')
        list_vacancies_del = []
        list = json.dumps(list_vacancies_del, ensure_ascii=False)
        with open(vacancies_for_use_path, "w", encoding="utf8") as f:
            f.write(list)
        with open(vacancies_path, "r", encoding="utf8") as file:
            file.write(list)


# test = HeadHunterAPI()
# list = write_vacancies(test.load_vacancies("Водитель"))
#
# vacancies_path = os.path.join(os.path.dirname(os.getcwd()), 'data', 'vacancy.json')
# with (open(vacancies_path, "r", encoding="utf8") as f):  # взяли загруженные вакансии для дальнейшей работы
#     list_vacancies = json.load(f)
#
# J = JSONSaver()
# J.add_vacancy(list_vacancies)
# J.delete_vacancy()
