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

def get_coordinates(city:str)->list:

    url=f'https://pl.wikipedia.org/wiki/{city}'
    responce=requests.get(url).text
    responce_html = BeautifulSoup(responce, 'html.parser')
    longitude = float(responce_html.select('.longitude')[1].text)
    latitude = float(responce_html.select('.latitude')[1].text)
    return [latitude, longitude]

def get_map(users_data:list)->None:
    import folium
    map = folium.Map(location=[52.23, 21.00],zoom_start=6)
    for user in users_data:
        coordinates = get_coordinates(user['location'])

        folium.Marker(
            location=[coordinates[0], coordinates[1]],
            popup=f"Twój znajomy {user['name']},< br/> z miejscowość: {user['location']}< br/> opublikował {user['posts']} postów").add_to(
            map)
    map.save("map.html")