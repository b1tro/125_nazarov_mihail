import requests
def find_metro_id_by_name_and_city(station_name,city_name):
    for city in requests.get("https://api.hh.ru/metro").json():
        if city['name'] == city_name:
            for line in city['lines']:
                for station in line["stations"]:
                    if station['name'] == station_name:
                        return station['id']

def find_area_id_by_name(area_name):
    for country in requests.get('https://api.hh.ru/areas').json():
        if country['name'] == area_name:
            return country['id']
        for area in country['areas']:
            if area['name'] == area_name:
                return area['id']
            for city in area['areas']:
                if city['name'] == area_name:
                    return city['id']