import sys
print(sys.argv)
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)  # вмикає кольори на Windows та автоматично скидає стиль

def print_tree(dir_path: Path, prefix: str = "") -> None:
    """
    Рекурсивно виводить дерево файлів/папок для dir_path.
    prefix — префікс для “гілок” дерева.
    """
    try:
        entries = list(dir_path.iterdir())
    except PermissionError:
        print(prefix + Fore.YELLOW + "└── [Permission denied]")
        return
    except OSError as e:
        print(prefix + Fore.YELLOW + f"└── [OS error: {e}]")
        return

    # Папки спершу, потім файли; сортуємо за назвою (case-insensitive)
    entries.sort(key=lambda p: (not p.is_dir(), p.name.lower()))

    for i, entry in enumerate(entries):
        is_last = (i == len(entries) - 1)
        # Обираємо гілку в залежності від того, чи це останній елемент в папці 
        branch = "└── " if is_last else "├── "
        # Обробка символічних посилань окремо від файлів і директорій
        if entry.is_symlink():
            color = Fore.MAGENTA
            label = entry.name + " -> " + str(entry.resolve(strict=False))
            print(prefix + branch + color + label + Style.RESET_ALL)
            # не заходимо в symlink як директорію, щоб уникнути циклів
            continue
        # Обробка директорій і файлів окремо
        if entry.is_dir():
            color = Fore.CYAN  # колір для директорій
            print(prefix + branch + color + entry.name + Style.RESET_ALL)
            # розширюємо префікс вертикальною лінією якщо не останній
            extension = "    " if is_last else "│   "
            # рекурсивний виклик для підпапки 
            print_tree(entry, prefix + extension)
        else:
            color = Fore.GREEN  # колір для файлів
            print(prefix + branch + color + entry.name + Style.RESET_ALL)

def main() -> int:
    # Отримуємо шлях з аргументів командного рядка
    if len(sys.argv) != 2:
        print(Fore.YELLOW + "Використання: python hw03.py /шлях/до/директорії" + Style.RESET_ALL)
        return 2

    raw_path = sys.argv[1]
    path = Path(raw_path).expanduser().resolve()

    # Перевірки
    if not path.exists():
        print(Fore.RED + f"Помилка: шлях не існує: {path}" + Style.RESET_ALL)
        return 1

    if not path.is_dir():
        print(Fore.RED + f"Помилка: це не директорія: {path}" + Style.RESET_ALL)
        return 1

    # Виводимо “корінь”
    print(Fore.CYAN + path.name + Style.RESET_ALL)
    print_tree(path)
    return 0

if __name__ == "__main__":
    sys.exit(main())