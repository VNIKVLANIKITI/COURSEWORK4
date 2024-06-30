def filter_vacancies(vacancies, keywords):
    return [vacancy for vacancy in vacancies if
            any(key.lower() in vacancy['description'].lower() for key in keywords)]


def get_vacancies_by_salary(vacancies, salary_range):
    if not salary_range:
        return vacancies
    salary_values = salary_range.split('-')
    if len(salary_values) == 1:
        min_salary = max_salary  = int(salary_values[0])
    elif len(salary_values) == 2:
        min_salary, max_salary  = map(int, salary_values)
    else:
        print("Неверный формат диапазона зарплат.")
        return vacancies

    return [vacancy for vacancy in vacancies if
            vacancy.get('salary_from', 0) >= min_salary and vacancy.get('salary_from',
                                                                            float('inf')) <= max_salary]


def sort_vacancies(vacancies):
    return sorted(vacancies, key=lambda vacancy: vacancy.get('salary_from', 0), reverse=True)


def get_top_vacancies(vacancies, upper_bound):
    return vacancies[:upper_bound]


def print_vacancies(vacancies):
    if vacancies:
        for index, vacancy in enumerate(vacancies, start=1):
            print(f"Вакансия {index}:")
            print(f"Название: {vacancy.get('name', 'Не указано')}")
            print(f"Зарплата от: {vacancy.get('salary_from', 'Не указана')}")
            print(f"Описание: {vacancy.get('description', 'Отсутствует')}")
            print(f"Ссылка: {vacancy.get('alternate_url', 'Не указана')}")
            print()
    else:
        print("Нет подходящих вакансий")

