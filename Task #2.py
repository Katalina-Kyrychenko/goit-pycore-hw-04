from helper import check_file_status
from constants import FileStatus

def get_cats_info(path):
    status = check_file_status(path)
    if status == FileStatus.NOT_FOUND or status == FileStatus.NOT_A_FILE:
        raise FileNotFoundError(f"The file at {path} does not exist.")

    cats = []

    # Відкриваємо файл у безпечному режимі
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            # Видаляємо зайві пробіли та перенос рядка
            line = line.strip()

            # Пропускаємо порожні рядки, якщо є
            if not line:
                continue

            # Розділяємо рядок на частини
            parts = line.split(",")

            # Переконуємось, що в рядку рівно 3 частини
            if len(parts) != 3:
                print(f"Неправильний формат рядка: {line}")
                continue

            cat_id, name, age = parts

            # Формуємо словник для кожного кота
            cat_dict = {
                "id": cat_id,
                "name": name,
                "age": age
            }

            # Додаємо словник до загального списку
            cats.append(cat_dict)

    return cats

cats_info = get_cats_info("./cats.txt")
print(cats_info)