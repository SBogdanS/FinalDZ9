def error_handler(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return "No user with this name"
        except ValueError:
            return "Give me name and phone please: "
        except IndexError:
            return "Enter user name: "

    return inner


def hello_handler():
    user_text = input("Hello, how I can help you?\n").lower().split()
    com = user_text[0]
    func = greting(com)
    if func:
        return func()


# добавить пользователя
@error_handler
def add_handler(*args, **kwargs):
    name, phone = args
    USERS.update({name: phone})
    return f"{name} was add"


# изменить пользователя
@error_handler
def change_handler(*args, **kwargs):
    name, phone = args
    ind_name = USERS.get(name)
    if ind_name == None:
        return f"This contat:{name}, not in list"
    else:
        USERS.update({name: phone})
    return f"{name} was change"


# отоброзить пльзвателя
@error_handler
def phone_handler(*args):
    name = args[0]
    for i in USERS.keys():
        if name == i:
            return f"{i}: {USERS[i]}\n"


def show_all_handler():
    all_user = ""
    for i in USERS.keys():
        all_user += f"{i}: {USERS[i]}\n"
    return all_user


def exit_handler():
    print("Good bye!")
    return exit()


USERS = {
    "Ivan": "98 955 65 45",
    "Joao": "98555 98 75",
    "Kira": "98 5454 56 1",
    "Leandro": "95 123456 45",
    "Kiril": "93 2165 2 33",
    "Zaur": "91 984532 2",
    "Maks": "98 9545 21 21",
    "Telmo": "98 00 22 11 3",
}

FUNC = {
    "hello": hello_handler,
    "add": add_handler,
    "change": change_handler,
    "phone": phone_handler,
    "show": show_all_handler,
    "exit": exit_handler,
}


def greting(comend):
    return FUNC[comend]


@error_handler
def main():
    while True:
        user_text = input("Enter you comand: ").lower()
        if user_text in ["good bye", "exit", "close", "hello", "show all"]:
            if user_text in ["good bye", "exit", "close"]:
                com = "exit"
            else:
                user_text = user_text.split()
                com = user_text[0]
            func = greting(com)
            print(func())
            continue

        user_text = user_text.split()
        if len(user_text) == 2:
            com = user_text[0]
            nome = user_text[1].title()
            func = greting(com)
            print(func(nome))
            continue
        elif len(user_text) == 3:
            com = user_text[0]
            nome = user_text[1].title()
            tel = user_text[2]
            func = greting(com)
            print(func(nome, tel))
            continue
        print("*****This comande not find.Еry another command!")


if __name__ == "__main__":
    main()

    # user_text = input("Enter you comand: ").lower()
    # if user_text in ["good bye", "exit", "close"]:
    #     com = "exit"
    #     func = greting(com)
    #     print(func())
    # elif user_text in ["show all"]:
    #     com = "show"
    #     func = greting(com)
    #     print(func())
    #     continue
    # elif user_text in ["hello"]:
    #     func = greting(user_text)
    #     print(func())
    #     continue
