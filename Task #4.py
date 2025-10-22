
def parse_input(user_input: str):
    """
    Розбиває введений рядок користувача на команду і аргументи.
    Повертає кортеж (command: str, args: list[str]).
    """
    user_input = user_input.strip()
    if not user_input:
        return "", []
    cmd, *args = user_input.split()
    return cmd.lower(), args


def add_contact(args, contacts: dict) -> str:
    """add <username> <phone> — Add a new contact"""
    if len(args) != 2:
        return "Usage: add <username> <phone>"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts: dict) -> str:
    """change <username> <new_phone> — Update an existing contact's phone"""
    if len(args) != 2:
        return "Usage: change <username> <new_phone>"
    name, new_phone = args
    if name not in contacts:
        return f"Contact '{name}' not found."
    contacts[name] = new_phone
    return "Contact updated."


def show_phone(args, contacts: dict) -> str:
    """phone <username> — Show contact's phone number"""
    if len(args) != 1:
        return "Usage: phone <username>"
    name = args[0]
    if name not in contacts:
        return f"Contact '{name}' not found."
    return contacts[name]


def show_all(contacts: dict) -> str:
    """all — Show all saved contacts"""
    if not contacts:
        return "No contacts found."
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)


def show_help(commands: dict) -> str:
    """help — Show available commands"""
    lines = ["Available commands:"]
    for cmd, func in commands.items():
        doc = func.__doc__.strip() if func.__doc__ else ""
        lines.append(f"  {doc}")
    lines.append("  close / exit — Exit the bot")
    return "\n".join(lines)


def main():
    contacts = {}

    # словник відповідності команд до функцій
    commands = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
        "help": None,  # буде оброблено окремо
    }

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "help":
            print(show_help(commands))
        elif command in commands:
            func = commands[command]
            if command in ("add", "change", "phone"):
                print(func(args, contacts))
            else:
                print(func(contacts))
        elif command == "":
            continue
        else:
            print("Invalid command. Type 'help' to see available commands.")


if __name__ == "__main__":
    main()