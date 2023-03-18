def get_resume_data(data: dict):
    for key in data:
        if data[key] == "Не имеет значения":
            data[key] = None

