import requests
import SQL.user_data
URL = 'https://api.hh.ru/vacancies'

def load_vacancies(user_id, page):
    params = {
        "text": None,
        "salary": None,
        "area": None,
        "metro": None,
        "experience": None,
        "employment": None,
        "schedule": None,
        "vacancy_search_order": None,
        "vacancy_search_fields": None,
        "only_with_salary": None,
        "period": "30",
        "page": "30",
        "premium": None,
    }

    user_adapted_resume_data = SQL.user_data.send_adapted_resume(user_id)
    for key,property in zip(params, user_adapted_resume_data ):
        if property is None:
            params[key] = None
            continue
        params[key] = property
    params['page'] = page
    results = requests.get(url=URL, params=params).json()
    vacancy_information = f"""
{results['items'][0]['name']}

<b>Требования:</b> {results['items'][0]['snippet']['requirement']}
<i>Подробнее по ссылке</i>

<b>Обязанности:</b> {results['items'][0]['snippet']['responsibility']} 
<i>Подробнее по ссылке</i>

<b>Территориально:</b> {results['items'][0]['address']['metro']['station_name']}

<b>Работодатель:</b> {results['items'][0]['employer']['name']}

<b>Ссылка:</b> {results['items'][0]['alternate_url']}

<b>Опубликовано:</b> {results['items'][0]['published_at'][:9]}
"""
    return vacancy_information
