import requests

import SQL.user_data
from HEADHUNTER.resume import resume_config
from HEADHUNTER.searching import search

def get_area_id_by_name(area_name):
    for country in requests.get('https://api.hh.ru/areas').json():
        if country['name'] == area_name:
            return country['id']
        for area in country['areas']:
            if area['name'] == area_name:
                return area['id']
            for city in area['areas']:
                if city['name'] == area_name:
                    return city['id']
    return None

def get_metro_id_by_name_and_city(station_name, city_name):
    for city in requests.get("https://api.hh.ru/metro").json():
        if city['name'] == city_name:
            for line in city['lines']:
                for station in line["stations"]:
                    if station['name'] == station_name:
                        return station['id']
    return None
def no_matter_equals_none(resume):
    for i in range(len(resume)):
        if resume[i] == 'Не имеет значения':
            resume[i] = None
    return resume

def get_experience_id(experience):
    for key in resume_config.experience:
        if experience == key:
            experience = resume_config.experience[key]
            return experience
    return None

def get_employment_id(employment):
    for key in resume_config.employment:
        if employment == key:
            employment = resume_config.employment[key]
            return employment
    return None

def get_schedule_id(schedule):
    for key in resume_config.schedule:
        if schedule == key:
            schedule = resume_config.schedule[key]
            return schedule
    return None

def adapt_resume(resume):
    print(resume)
    resume = no_matter_equals_none(resume)
    resume[6] = get_metro_id_by_name_and_city(resume[6], resume[5])
    resume[5] = get_area_id_by_name(resume[5])
    resume[7] = get_experience_id(resume[7])
    resume[8] = get_employment_id(resume[8])
    resume[9] = get_schedule_id(resume[9])
    return resume

def send_processed_resume(resume):
    adapted_resume = adapt_resume(resume)
    for i in range (6):
        resume.append(None)
    SQL.user_data.add_adapted_resume_to_base(tuple(adapted_resume))