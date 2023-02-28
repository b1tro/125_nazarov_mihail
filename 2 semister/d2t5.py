import os
def print_docs(directory):
    i = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            print("Файл здесь: ")
            print(file)
        for dir in dirs:
            print("\nВыбранная папка: ", dir)
directory = r'D:/GitHub/125_nazarov_mihail/125_nazarov_mihail/2 semister/d2t5'

print_docs(directory)
