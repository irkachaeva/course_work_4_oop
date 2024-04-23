
from src.utils import get_vacancies
from src.utils import sorting

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

print(sorted)
#сохранили в файл отфильтрованные вакансии
        #data = sorting(vacancies_list, top_n, salary_from, salary_to, city)




# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
