from src.HeadHunterAPI import HeadHunterAPI
from src.Vacancy import Vacancy
from src.JSONSaver import JSONSaver


def get_vacancies(vacancy):
    """ блок обработки данных для формирования ответа на запрос"""

    hh_api = HeadHunterAPI()
    data = hh_api.load_vacancies(vacancy)
    json_saver = JSONSaver()
    vacancy_list = json_saver.add_vacancy(data)
    return vacancy_list


def sorting(vacancies_list, top_n, salary_from, salary_to, city):
    filtred_vacancies = []
    for item in vacancies_list:
        if city != "":
            if item['area'] == city:
                if item["salary_from"] == "" and item["salary_to"] == "":
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






