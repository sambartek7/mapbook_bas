def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy  {user["Name"]}, z miejscowości {user["location"]} opublikował {user["posts"]} postów")


def add_user(users_data: list) -> None:
    new_name = input('podaj imie nowego uzytkownika: ')
    new_location = input('podaj nową lokalizację: ')
    new_post = int(input('podaj ilość postów: '))
    users_data.append({"Name": new_name, "location": new_location, "posts": new_post})


def remove_user(users_data: list) -> None:
    uzytkownik_do_usunięcia = input('podaj uzytkownika do usunięcia: ')

    for user in users_data:
        if user['Name'] == uzytkownik_do_usunięcia:
            users_data.remove(user)



def update_user(users_data: list) -> None:


    uzytkownik_do_edycji = input('podaj uzytkownika do edycji: ')
    for user in users_data:
        if user['Name'] == uzytkownik_do_edycji:
            user['Name'] = input('Podaj nowe imie uzytkownika: ')
            user['location'] = input('Podaj nową lokalizację: ')
            user['posts'] = int(input('Podaj nową liczbę postów: '))

def get_coordinates(city:str)->list:

    import requests
    from bs4 import BeautifulSoup

    url=f'https://pl.wikipedia.org/wiki/{city}'
    response = requests.get(url).text
    response_html = BeautifulSoup(response, 'html.parser')
    longitude=float(response_html.select('.longitude')[1].text. replace(',','.'))
    latitude=float(response_html.select('.latitude')[1].text. replace(',','.'))
    return [latitude,longitude]

def get_map(users_data:list)->None:
    import folium
    map = folium.Map(location=(52.23, 21.00), zoom_start=6)
    for user in users_data:
        coordinates=get_coordinates(user['location'])

        folium.Marker(
            location=(coordinates[0],coordinates[1]),
            popup=f"Twój znajomy  {user["Name"]}, <br/> miejscowość: {user["location"]} <br/> opublikował {user["posts"]} postów").add_to(map)
    map.save('mapa.html')

