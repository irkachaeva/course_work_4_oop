from src.HeadHunterAPI import HeadHunterAPI
from src.Vacancy import Vacancy
from src.JSONSaver import JSONSaver


vacancy = input('Введите название вакансии:')
hh_api = HeadHunterAPI()
hh_vacancies = hh_api.load_vacancies(vacancy)

json_saver = JSONSaver()
vacancies_list = json_saver.add_vacancy(hh_vacancies)


# test =[]
# for i in vacancies_list:
#     l = i.__str__()
#     test.append(l)
# print(test)





# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
