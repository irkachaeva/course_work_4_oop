from src.HeadHunterAPI import HeadHunterAPI
from src.Vacancy import Vacancy
from src.JSONSaver import JSONSaver
import json
import os.path


def get_vacancies(vacancy, city):
    """ блок обработки данных для формирования ответа на запрос"""

    hh_api = HeadHunterAPI()
    data = hh_api.load_vacancies(vacancy)
    list_classes = Vacancy.get_list_vacancies(data, city)
    return list_classes


def sort_vacancies(list_classes):
    """
    Функция сортирует список объектов по зарплате
    от большего к меньшему
    """
    # try:
    sorted_list = sorted(list_classes, reverse=True)
    return sorted_list
    # except TypeError:
    #     pass


def get_top_vacancies(list_classes: list[object, ...] | object | None, top_n: str) -> list[object, ...] | object:
    """
    Функция возвращает количество элементов, которое укажет пользователь в параметре (top_n)
    если параметр (top_n) не указан, функция вернет изначальный список (list_classes)
    """
    try:
        if top_n:
            if int(top_n) == 0:
                raise IndexError(f"\n\nВы передали некорректное значение - {top_n}\n"
                                 f"Ошибка: невозможно вернуть {top_n} вакансий")

            else:
                try:
                    if int(top_n) > len(list_classes):
                        if len(list_classes) != 11 and len(list_classes) % 10 == 1:
                            raise IndexError(f"\n\nПо указанным параметрам мы нашли только {len(list_classes)} "
                                             f"вакансию")
                        elif 2 <= len(list_classes) <= 4:
                            raise IndexError(f"\n\nПо указанным параметрам мы нашли только {len(list_classes)} "
                                             f"вакансии")
                        else:
                            raise IndexError(f"\n\nПо указанным параметрам мы нашли только {len(list_classes)} "

                                             f"вакансий")
                except IndexError as a:
                    print(a)

                finally:
                    return list_classes[:int(top_n)]
        else:
            return list_classes
    except TypeError:
        pass
    except IndexError as a:
        print(a)


def get_vacancies_by_salary(list_classes: list[object, ...], vacancy, salary_from, city):
    """
    Функция сортирует список объектов по указанному диапазону зарплат,если указанный диапазон не найден, возвращается сообщение, что нужно указать другой диапазон
    """
    list_filtered_classes = []
    try:
        if salary_from != "" and city !="" or salary_from != "" and city == "":
            for el in list_classes:
                if el.salary_from >= int(salary_from) and el.area == city:
                    list_filtered_classes.append(el)

        if len(list_filtered_classes) < 1:
            raise NameError(f"\nПо данным условиям \n"
                                    f"(Вакансия: {vacancy} ЗП от - {salary_from}, в населенном пункте {city}. )\n"
                                    f"не найдено ни одного совпадения ...")

        if salary_from == "" and city != "":
            for el in list_classes:
                if el.area == city:
                    list_filtered_classes.append(el)

        if len(list_filtered_classes) < 1:
            raise NameError(f"\nПо данным условиям \n"
                            f"(Вакансия: {vacancy}, в населенном пункте {city} )\n"
                            f"не найдено ни одного совпадения ...")

        if salary_from == "" and city == "":
            for el in list_classes:
                list_filtered_classes.append(el)

        if len(list_filtered_classes) < 1:
            raise NameError(f"\nПо данным условиям \n"
                            f"не найдено ни одного совпадения ...")

        else:
            return list_classes
    except NameError as a:
        print(a)
    return list_filtered_classes


def get_top_vacancies(list_classes: list[object, ...] | object | None, top_n: str) -> list[object, ...] | object:
    """
    Функция возвращает только то количество элементов которое укажет пользователь в параметре (top_n)
    если параметр (top_n) не указан
    функция вернет изначальный список (list_classes)

    если переданный параметр (top_n) больше
    чем количество элементов в списке
    пользователю вернется список всех элементов
    и сообщение о том что в списке нет указанного количества элементов

    """
    try:
        if top_n:
            if int(top_n) == 0:
                raise IndexError(f"\n\nВы передали некорректное значение - {top_n}\n"
                                 f"Ошибка: невозможно вернуть {top_n} вакансий")

            else:
                try:
                    if int(top_n) > len(list_classes):
                        if len(list_classes) != 11 and len(list_classes) % 10 == 1:
                            raise IndexError(f"\n\nПо указанным параметрам мы нашли только {len(list_classes)} "
                                             f"вакансию")
                        elif 2 <= len(list_classes) <= 4:
                            raise IndexError(f"\n\nПо указанным параметрам мы нашли только {len(list_classes)} "
                                             f"вакансии")
                        else:
                            raise IndexError(f"\n\nПо указанным параметрам мы нашли только {len(list_classes)} "

                                             f"вакансий")
                except IndexError as a:
                    print(a)

                finally:
                    return list_classes[:int(top_n)]

        else:
            return list_classes

    except TypeError:
        pass
    except IndexError as a:
        print(a)


def print_vacancies(list_classes: list[object, ...] | object | None) -> None:
    """
    Функция печатает список объектов
    """
    try:
        for elem in list_classes:
            print(elem)
    except TypeError:
        pass


def get_start():
    city = input("Введите название города (оставьте Enter, если город не важен):").title()
    vacancy = input("Введите название вакансии: ").title()
    if not isinstance(vacancy, str) or len(vacancy.strip()) == 0:
            raise("Назване вакансии не может быть пустым")

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    if top_n == "" or top_n == 0:
        print("Вы ничего не ввели. по умолчанию покажу топ 5 вакансий")
        top_n = 5
    else:
        top_n
    print("Введите зарплатный диапазон для поиска")
    salary_from = int(input("от: "))
    if salary_from == "":
        print("Ты не ввел параметры по зарплате.\nЯ покажу тебе самые высокооплачиваемые вакансии:")
    else:
        print(f'Подождите...\n')
    return city, vacancy, top_n, salary_from

