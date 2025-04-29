def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user['name']}, z miejscowości: {user['location']} opublikował {user['posts']} postów")


def add_user(users_data: list) -> None:
    new_name = input('podaj imie nowego użytkownika:')
    new_location = input('podaj lokalizację użytkownika:')
    new_posts = int(input('podaj liczbę postów nowego użytkownika'))
    users_data.append({"name": new_name, "location": new_location, "posts": new_posts})

def remove_user(users_data: list) -> None:
    uzytkownik_do_usuniecia = input('podaj uzytkownika do usuniecia: ')

    for user in users_data:
        if user['name'] == uzytkownik_do_usuniecia:
            users_data.remove(user)

def update_user(users_data: list)->None:

    uzytkownik_do_edycji = input('podaj uzytkownika do edycji: ')
    for user in users_data:
        if user['name'] == uzytkownik_do_edycji:
            user['name']=input('podaj nowe imie uzytkownika: ')
            user['location'] =input('podaj nowa lokalizacje uzytkownika: ')
            user['posts'] =int(input('podaj nowa liczbe postów: '))