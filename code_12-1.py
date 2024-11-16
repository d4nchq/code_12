import json

#початкові дані про багаж 10 пасажирів.
baggage_data = [
    {"Surname": "Ivanov", "Items": 3, "Weight": 15},
    {"Surname": "Petrov", "Items": 1, "Weight": 7},
    {"Surname": "Sidorov", "Items": 5, "Weight": 30},
    {"Surname": "Kovalenko", "Items": 2, "Weight": 4},
    {"Surname": "Bondarenko", "Items": 3, "Weight": 6},
    {"Surname": "Tkachenko", "Items": 4, "Weight": 18},
    {"Surname": "Popov", "Items": 2, "Weight": 22},
    {"Surname": "Shevchenko", "Items": 1, "Weight": 2},
    {"Surname": "Lysenko", "Items": 3, "Weight": 26},
    {"Surname": "Melnyk", "Items": 2, "Weight": 10}
]

#зберігаємо початкові дані у JSON файл.
with open("baggage_data.json", "w") as file:
    json.dump(baggage_data, file)

#функція для відображення вмісту JSON-файлу.
def view_data():
    with open("baggage_data.json", "r") as file:
        data = json.load(file)
        print(json.dumps(data, indent=4))

#функція для додавання нового запису.
def add_record():
    surname = input("Введіть прізвище пасажира: ")
    items = int(input("Введіть кількість речей: "))
    weight = float(input("Введіть загальну вагу багажу: "))

    with open("baggage_data.json", "r+") as file:
        data = json.load(file)
        data.append({"Surname": surname, "Items": items, "Weight": weight})
        file.seek(0)
        json.dump(data, file, indent=4)

#функція для видалення запису за прізвищем.
def delete_record():
    surname = input("Введіть прізвище пасажира для видалення: ")

    with open("baggage_data.json", "r+") as file:
        data = json.load(file)
        data = [record for record in data if record["Surname"] != surname]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=4)

#функція для пошуку записів за кількістю речей > 2.
def search_by_items():
    with open("baggage_data.json", "r") as file:
        data = json.load(file)
        result = [record["Surname"] for record in data if record["Items"] > 2]
        print("Пасажири з більше ніж 2 речами:", result)

#функція для підрахунку пасажирів за категоріями ваги багажу.
def categorize_by_weight():
    with open("baggage_data.json", "r") as file:
        data = json.load(file)
        less_than_5 = len([record for record in data if record["Weight"] < 5])
        between_5_and_25 = len([record for record in data if 5 <= record["Weight"] <= 25])
        more_than_25 = len([record for record in data if record["Weight"] > 25])

        results = {
            "Менше 5 кг": less_than_5,
            "Від 5 до 25 кг": between_5_and_25,
            "Більше 25 кг": more_than_25
        }

        #зберігаємо результати в новий JSON файл.
        with open("categorized_baggage.json", "w") as output_file:
            json.dump(results, output_file, indent=4)
        print("Результат категоризації збережено в 'categorized_baggage.json'")

#діалогове меню для користувача.
def main():
    while True:
        print("\nОберіть опцію:")
        print("1 - Вивести вміст JSON файлу")
        print("2 - Додати новий запис")
        print("3 - Видалити запис")
        print("4 - Пошук пасажирів з більше ніж 2 речами")
        print("5 - Категоризація пасажирів за вагою багажу")
        print("6 - Вихід")
        
        choice = input("Введіть номер опції: ")
        
        if choice == "1":
            view_data()
        elif choice == "2":
            add_record()
        elif choice == "3":
            delete_record()
        elif choice == "4":
            search_by_items()
        elif choice == "5":
            categorize_by_weight()
        elif choice == "6":
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()