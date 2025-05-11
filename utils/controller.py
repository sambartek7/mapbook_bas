def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user['name']}, z miejscowości {user['location']} opublikował {user['posts']} postów")


def add_user(users_data: list) -> None:
    new_name = input('podaj imie nowego uzytkownika: ')
    new_location = input('podaj nową lokalizację: ')
    new_post = int(input('podaj ilość postów: '))
    users_data.append({"name": new_name, "location": new_location, "posts": new_post})


def remove_user(users_data: list) -> None:
    uzytkownik_do_usunięcia = input('podaj uzytkownika do usunięcia: ')
    for user in users_data[:]:  # kopia listy na potrzeby usuwania
        if user['name'] == uzytkownik_do_usunięcia:
            users_data.remove(user)


def update_user(users_data: list) -> None:
    uzytkownik_do_edycji = input('podaj uzytkownika do edycji: ')
    for user in users_data:
        if user['name'] == uzytkownik_do_edycji:
            user['name'] = input('Podaj nowe imie uzytkownika: ')
            user['location'] = input('Podaj nową lokalizację: ')
            user['posts'] = int(input('Podaj nową liczbę postów: '))


def dms_to_decimal(dms: str) -> float:
    import re
    degrees = re.search(r"(\d+)[°]", dms)
    minutes = re.search(r"(\d+)[′']", dms)
    seconds = re.search(r"(\d+)[″\"]", dms)
    direction = re.search(r"[NSEW]$", dms)

    d = int(degrees.group(1)) if degrees else 0
    m = int(minutes.group(1)) if minutes else 0
    s = int(seconds.group(1)) if seconds else 0
    dec = d + m / 60 + s / 3600

    if direction and direction.group() in ['S', 'W']:
        dec *= -1

    return dec


def get_coordinates(city: str) -> list:
    import requests
    from bs4 import BeautifulSoup

    url = f'https://pl.wikipedia.org/wiki/{city}'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        print(f"Nie udało się pobrać danych dla {city}")
        return [0.0, 0.0]

    response_html = BeautifulSoup(response.text, 'html.parser')
    lat_el = response_html.select_one('.latitude')
    lon_el = response_html.select_one('.longitude')

    if not lat_el or not lon_el:
        print(f"Nie znaleziono współrzędnych dla {city}")
        return [0.0, 0.0]

    try:
        latitude = dms_to_decimal(lat_el.text)
        longitude = dms_to_decimal(lon_el.text)
        return [latitude, longitude]
    except Exception as e:
        print(f"Błąd konwersji współrzędnych dla {city}: {e}")
        return [0.0, 0.0]


def get_map(users_data: list) -> None:
    import folium
    mapa = folium.Map(location=(52.23, 21.00), zoom_start=6)
    for user in users_data:
        coordinates = get_coordinates(user['location'])
        folium.Marker(
            location=(coordinates[0], coordinates[1]),
            popup=f"Twój znajomy {user['name']}, <br/> miejscowość: {user['location']} <br/> opublikował {user['posts']} postów"
        ).add_to(mapa)
    mapa.save('mapa.html')


