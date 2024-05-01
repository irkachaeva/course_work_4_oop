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
                        if Vacancy.check_data_int(item['salary'].get('from')) > 0:
                            salary_from = int(Vacancy.check_data_int(item['salary'].get('from')) / Vacancy.tax)
                        else:
                            salary_from = Vacancy.check_data_int(item['salary'].get('from'))
                        if item['salary']['to'] is not None:
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
                        if Vacancy.check_data_int(item['salary'].get('from')) > 0:
                            salary_from = int(Vacancy.check_data_text(item['salary'].get('from')) / Vacancy.tax)
                        else:
                            salary_from = Vacancy.check_data_text(item['salary'].get('from'))
                        if item['salary']['to'] is not None:
                            salary_to = int(Vacancy.check_data_text(item['salary'].get('to')) / Vacancy.tax)
                        else:
                            salary_to = Vacancy.check_data_text(item['salary'].get('to'))
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
        return f'Вакансия: {self.name}\nГород: {self.area}\nКомпания-pаботодатель: {self.employer}\nТребования: {self.snippet}\nЗарплата к начислению:\nот: {self.salary_from}\nдо: {self.salary_to}\nВалюта: {self.salary_currency}\nСсылка на вакансию:{self.alternate_url}\n\n'

    def __repr__(self):
        return f'Вакансия: {self.name}\nГород: {self.area}\nКомпания-pаботодатель: {self.employer}\nТребования: {self.snippet}\nЗарплата:\nот: {self.salary_from}\nдо: {self.salary_to}\nВалюта: {self.salary_currency}\nСсылка на вакансию:{self.alternate_url}\n\n'

    def __lt__(self, other):
        """Метод сравнения вакансий между собой по зарплате и валидации данных по зарплате"""

        if self.salary_from is not None and other.salary_from is not None:
            if self.salary_from < other.salary_from:
                return self
            else:
                return other
        if self.salary_to is not None and other.salary_to is not None:
            if self.salary_to < other.salary_to:
                return self
            else:
                return other
        return 'Зарплата не указана'

    def __gt__(self, other):

        """Метод сравнения вакансий между собой по зарплате и валидации данных по зарплате"""

        if self.salary_from is not None and other.salary_from is not None:
            if self.salary_from > other.salary_from:
                return self
            else:
                return other
        if self.salary_to is not None and other.salary_to is not None:
            if self.salary_to > other.salary_to:
                return self
            else:
                return other
        return 'Зарплата не указана'

    def get_salary_from(self):
        return self.salary_from

    def get_salary_to(self):
        return self.salary_to