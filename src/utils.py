from src.HeadHunterAPI import HeadHunterAPI
from src.Vacancy import Vacancy
from src.JSONSaver import JSONSaver
import json
import os.path


def write_vacancies(data):
    vacancies_path = os.path.join(os.getcwd(), 'data', 'vacancy.json')
    with open(vacancies_path, "r", encoding="utf-8") as f:
        for it in data:
            for key, value in it.items():
                if value is None:
                    it[key] = "Не заполнено"

    with open(vacancies_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return


def get_vacancies(vacancy):
    """ блок обработки данных для формирования ответа на запрос"""

    hh_api = HeadHunterAPI()
    data = hh_api.load_vacancies(vacancy)

    write_vacancies(data)

    vacancies_path = os.path.join(os.getcwd(), 'data', 'vacancy.json')
    with (open(vacancies_path, "r", encoding="utf8") as f):  # взяли загруженные вакансии для дальнейшей работы
        list_vacancies = json.load(f)

    json_saver = JSONSaver()
    vacancy_list = json_saver.add_vacancy(list_vacancies)
    return vacancy_list


def sorting(vacancies_list, top_n, salary_from, salary_to, city):
    filtred_vacancies = []
    for item in vacancies_list:
        if city != "":
            if item['area'] is not None and item['area'] == city:
                if item["salary_from"] == "Не заполнено" and item["salary_to"] == "Не заполнено":
                    filtred_vacancies.append(item)

                if item["salary_from"] >= salary_from and item["salary_to"] >= salary_to:
                    filtred_vacancies.append(item)
        print("Я ничего не нашел")
        break

    """Сортируем и получаем запрошенное количество вакансий для вывода по зарплате"""

    sorted_list_to = sorted(filtred_vacancies, key=lambda x: x['salary_to'], reverse=True)
    sorted_list = sorted(sorted_list_to, key=lambda x: x['salary_from'], reverse=True)
    sorted_vac = sorted_list[:top_n]

    return sorted_vac

def get_start():
    city = input("Введите название города (оставьте Enter, если город не важен):").title()
    vacancy = input("Введите название вакансии: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    if top_n == "" or top_n == 0:
        print("Вы ничего не ввели. по умолчанию покажу топ 5 вакансий")
        top_n = 5
    else:
        top_n
    print("Введите зарплатный диапазон для поиска")
    salary_from = input("от: ")
    salary_to = input("до: ")
    if salary_from == "" and salary_to == "":
        print("Хм. ты не ввел параметры по зарплате.\nТогда я покажу тебе самые высокооплачиваемые вакансии!")
    else:
        print(f'Я нашел топ {top_n} вакансий, подождите секунду:')

    vacancies_list = get_vacancies(vacancy)
    sorted = sorting(vacancies_list, top_n, salary_from, salary_to, city)

    return print(sorted)




