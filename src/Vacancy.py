class Vacancy:
    tax = 0.87
    vacancies_for_use = []

    def __init__(self, name, salary_from, salary_to, salary_currency, salary_gross, area, employer, experience, snippet, alternate_url, type_v):
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_currency = salary_currency
        self.salary_gross = salary_gross
        self.area = area
        self.employer = employer
        self.experience = experience
        self.snippet = snippet
        self.alternate_url = alternate_url
        self.type_v = type_v

        """объекты на уровне класса"""

    def class_to_dict(obj):
        """
        :return: возвращает объекты класса в качестве словаря
        """
        return obj.__dict__

    @staticmethod
    def check_data_text(value):
        """Проверка наличия пустых значений в тексте"""
        if value is not None:
            return value
        return "Не заполнено"

    @staticmethod
    def check_data_int(value):
        """Проверка наличия пустых значений в числах"""
        if value is not None:
            return value
        return 0

    @classmethod
    def get_list_vacancies(cls, list_vacancies, city: str = ""):
        """класс-метод для работы с вакансиями, полученными из даннх json api hh"""

        for item in list_vacancies:
            if item['area'].get("name") == city and city != "":
                name = Vacancy.check_data_text(item['name'])
                if item['salary'] is None:
                    salary_from = 0
                    salary_to = 0
                    salary_currency = "Не заполнено"

                else:
                    if isinstance(item['salary'], dict):
                        if item['salary'].get('gross') is False:
                            salary_from = int(Vacancy.check_data_int(item['salary'].get('from')) / Vacancy.tax)
                        else:
                            salary_from = Vacancy.check_data_int(item['salary'].get('from'))
                        if item['salary'].get('gross') is False:
                            salary_to = int(Vacancy.check_data_int(item['salary'].get('to')) / Vacancy.tax)
                        else:
                            salary_to = Vacancy.check_data_int(item['salary'].get('to'))
                        salary_currency = item['salary'].get('currency')

                salary_gross = "ЗП к начислению"
                area = item['area'].get("name")
                employer = item['employer']['name']
                snippet = Vacancy.check_data_text(item['snippet']["requirement"])
                experience = Vacancy.check_data_text(item["experience"]['name'])
                alternate_url = Vacancy.check_data_text(item['alternate_url'])
                type_v = item['type']["name"]
                vacancy = cls(name, salary_from, salary_to,
                              salary_currency, salary_gross,
                              area, employer, experience,
                              snippet, alternate_url, type_v)
                Vacancy.vacancies_for_use.append(vacancy)

            elif city == "":
                name = Vacancy.check_data_text(item['name'])
                if item['salary'] is None:
                    salary_from = 0
                    salary_to = 0
                    salary_currency = "Не заполнено"

                else:
                    if isinstance(item['salary'], dict):
                        if item['salary'].get('gross') is False:
                            salary_from = int(Vacancy.check_data_int(item['salary'].get('from')) / Vacancy.tax)
                        else:
                            salary_from = Vacancy.check_data_int(item['salary'].get('from'))
                        if item['salary'].get('gross') is False:
                            salary_to = int(Vacancy.check_data_int(item['salary'].get('to')) / Vacancy.tax)
                        else:
                            salary_to = Vacancy.check_data_int(item['salary'].get('to'))
                        salary_currency = item['salary'].get('currency')

                salary_gross = "ЗП к начислению"
                area = item['area'].get("name")
                employer = item['employer']['name']
                snippet = Vacancy.check_data_text(item['snippet']["requirement"])
                experience = Vacancy.check_data_text(item["experience"]['name'])
                alternate_url = Vacancy.check_data_text(item['alternate_url'])
                type_v = item['type']["name"]
                vacancy = cls(name, salary_from, salary_to,
                              salary_currency, salary_gross,
                              area, employer, experience,
                              snippet, alternate_url, type_v)
                Vacancy.vacancies_for_use.append(vacancy)
        return Vacancy.vacancies_for_use


    def __str__(self):
        ''' строковое отображение'''
        if self.salary_from == 0:
            salary_from = "Информация не указана"
        else:
            salary_from = self.salary_from
        if self.salary_to == 0:
            salary_to = "Информация не указана"
        else:
            salary_to = self.salary_from
        return (f'Вакансия: {self.name}\n'
                f'Город: {self.area}\n'
                f'Компания-pаботодатель: {self.employer}\n'
                f'Требования: {self.snippet}\n'
                f'Зарплата:\nот: {salary_from}\nдо: {salary_to}\n'
                f'Валюта: {self.salary_currency}\n'
                f'Ссылка на вакансию:{self.alternate_url}\n'
                f'Статус вакансии:{self.type_v}\n')

    def __repr__(self):
        return (f'Вакансия: {self.name}\n'
                f'Город: {self.area}\n'
                f'Компания-pаботодатель: {self.employer}\n'
                f'Требования: {self.snippet}\n'
                f'Зарплата:\nот: {self.salary_from}\nдо: {self.salary_to}\n'
                f'Валюта: {self.salary_currency}\n'
                f'Ссылка на вакансию:{self.alternate_url}\n'
                f'Статус вакансии:{self.type_v}\n')

    def __lt__(self, other):
        """
        Метод сравнения вакансий между собой по зарплате - какой из объектов больше
        """
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        """
        Метод сравнения вакансий между собой по зарплате - какой из объектов меньше
        """
        return self.salary_from < other.salary_from

    def __eq__(self, other):
        """
        Метод сравнения вакансий между собой по зарплате - равны ли два объекта
        """
        return self.salary_from == other.salary_from
