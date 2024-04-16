import requests
from abc import ABC, abstractmethod


class ApiABS(ABC):
    @abstractmethod
    def load_vacancies(self, *args):
        pass


class HeadHunterAPI(ApiABS):

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params['page'] != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            data = response.json()
            vacancies = data.get('items', [])
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies


# api = HeadHunterAPI()
# keyword = ("Оператор склада")
# vacancies = api.load_vacancies(keyword)
# print(vacancies)
