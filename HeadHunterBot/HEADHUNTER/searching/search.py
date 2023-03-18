import requests
URL = 'https://api.hh.ru/vacancies'

parametrs = {
    "area": None,
    "metro": None,
    "experience": None,
    "employment": None,
    "schedule": None,
    "vacancy_search_order": None,
    "vacancy_search_fields": None,
    "only_with_salary": None,
    "period": None,
    "page": None,
    "premium": None
}

results = requests.get(url=URL, params=parametrs)
# print(results.json())



