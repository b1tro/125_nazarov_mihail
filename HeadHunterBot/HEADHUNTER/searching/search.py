import requests
import SQL.user_data
URL = 'https://api.hh.ru/vacancies'
class Searching():
    number = 0
    page = 0
    def load_vacancies(user_id, page, vacancy_number):
        print(f"Страница: {page}, номер: {vacancy_number}")
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
            "period": None,
            "page": None,
            "premium": None,
            "per_page": "20"
        }

        user_adapted_resume_data = SQL.user_data.send_adapted_resume(user_id)
        for key,property in zip(params, user_adapted_resume_data ):
            # if property is None:
            #     params[key] = None
            #     continue
            params[key] = property
        params['page'] = page
        results = requests.get(url=URL, params=params).json()
        try:
            check = results['items'][0]['name']
        except IndexError:
             vacancy_information = "Не найдено ни одной вакансии. Попробуйте поменять какие-либо параметры, проверьте орфографические ошибки."
             return vacancy_information

        try:
            territory = "станция метро " + (results['items'][vacancy_number]['address']['metro']['station_name'])
        except (IndexError, TypeError, AttributeError) as errors: #TypeError
            territory = "не указано"

        try:
            profit = f"{results['items'][vacancy_number]['salary']['from']} - {results['items'][vacancy_number]['salary']['to']} "
            profit = profit.replace("None", "")
            profit +=  results['items'][vacancy_number]['salary']['currency']
        except (IndexError, TypeError, AttributeError) as errors:
            profit = "не указана"

        try:
           requiement = results['items'][vacancy_number]['snippet']['requirement']
           requiement = requiement.replace("None", "")
        except (IndexError, TypeError, AttributeError) as errors:
            requiement = "не указаны"

        try:
            responsibility = results['items'][vacancy_number]['snippet']['responsibility']
            responsibility = responsibility.replace("None", "")
        except (IndexError, TypeError, AttributeError) as errors:
            responsibility = "не указаны"

        try:
            vacancy_information = f"""
        {results['items'][0]['name']}
    
        <b>Требования:</b> {requiement}
        <i>Подробнее по ссылке</i>
        
        <b>Обязанности:</b> {responsibility} 
        <i>Подробнее по ссылке</i>
        
        <b>Зарплата: </b> {profit} 
        
        <b>Территориально:</b> {territory}
        
        <b>Работодатель:</b> {results['items'][vacancy_number]['employer']['name']}
        
        <b>Ссылка:</b> {results['items'][vacancy_number]['alternate_url']}
        
        <b>Опубликовано:</b> {results['items'][vacancy_number]['published_at'][:9]}
        """
            vacancy_information = vacancy_information.replace("<highlighttext>", "")
            vacancy_information = vacancy_information.replace("</highlighttext>", "")
            return vacancy_information
        except IndexError:
            vacancy_information = "Кажется, ты долистал до последней вакансии.. Возможно, стоит поменять какие-то параметры в резюме."
            return vacancy_information


searching = Searching
def get_number():
    searching.number+=1
    return searching.number

def get_page():
    if (searching.number%19==0) and (searching.number !=0):
        searching.page+=1
        searching.number=0
    return searching.page

def get_current_number():
    return searching.number

def get_current_page():
    return searching.page


