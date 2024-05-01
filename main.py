from src import utils
import os.path
from src.utils import get_start
from src.utils import get_vacancies
from src.JSONSaver import JSONSaver
from src.utils import get_vacancies_by_salary
from src.utils import sort_vacancies
from src.utils import get_top_vacancies
from src.utils import print_vacancies


user_options = get_start()

city = user_options[0]
vacancy = user_options[1]
top_n = user_options[2]
salary_from = user_options[3]

list_classes = get_vacancies(vacancy, city)

path = os.path.join(os.getcwd(), 'data', 'vacancy.json')
JSONSaver(path).write_vacancies(list_classes)

ranged_vacancies = get_vacancies_by_salary(list_classes, vacancy, salary_from, city)
sorted_vacancies = sort_vacancies(ranged_vacancies)
top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
print_vacancies(top_vacancies)



# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
