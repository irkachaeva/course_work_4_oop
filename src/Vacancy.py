class Vacancy:
    def __init__(self, name, salary_from, salary_to,salary_currency,salary_gross, area, employer, experience, snippet, alternate_url, type_v):
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


    def class_to_dict(obj):
        return obj.__dict__

    def __str__(self):
        ''' строковое отображение'''
        return f'Вакансия: {self.name}\nГород: {self.area}\nКомпания-pаботодатель: {self.employer}\nТребования: {self.snippet}\nЗарплата:\nот: {self.salary_from}\nдо: {self.salary_to}\nВалюта: {self.salary_currency}\nСсылка на вакансию:{self.alternate_url}\n\n'

    def compare_vacancies(self, other):
        if self.salary_from == 'Не заполнено' and self.salary_to == 'Не заполнено' or other.salary_to == 'Не заполнено' and other.salary_from == 'Не заполнено':
            return 'Сравнение невозможно'
        elif self.salary_from == 'Не заполнено' and other.salary_from == 'Не заполнено':
            return self.salary_to >= other.salary_to # два до
        elif self.salary_to == 'Не заполнено' and other.salary_to == 'Не заполнено':
            return self.salary_from >= other.salary_from # два от
        elif self.salary_from == 'Не заполнено' and other.salary_to == 'Не заполнено':
            return self.salary_to >= other.salary_from # до с от
        elif self.salary_to == 'Не заполнено' and other.salary_from == 'Не заполнено':
            return self.salary_from >= other.salary_to #от с до


