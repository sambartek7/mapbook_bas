from tkinter import *

import tkintermapview

users: list = []


class User:
    def __init__(self,name:str, surname:str, location:str, posts:str):
        self.name=name
        self.surname=surname
        self.location=location
        self.posts=posts
        self.coordinates=self.get_coordinates()
        self.marker=map_widget.set_marker(self.coordinates[0], self.coordinates[1])


    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup

        url = f'https://pl.wikipedia.org/wiki/{self.location}'
        response = requests.get(url).text
        response_html = BeautifulSoup(response, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        return [latitude, longitude]


def add_user():
    name = entry_name.get()
    surname = entry_nazwisko.get()
    location = entry_miejscowosc.get()
    post = entry_liczba_postow.get()
    users.append(User(name=name, surname=surname, location=location, posts =post))
    print(users)
    show_users()
    entry_name.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_liczba_postow.delete(0, END)
    entry_name.focus()


def show_users():
    listbox_lista_obiektow.delete(0, END)
    for idx, user in enumerate(users):
        listbox_lista_obiektow.insert(idx,
                                      f'{idx + 1} {user.name} {user.surname} {user.location} {user.posts}')



def remove_user():
    i = listbox_lista_obiektow.index(ACTIVE)
    print(i)
    users[i].marker.delete()
    users.pop(i)
    show_users()


def edit_user():
    i = listbox_lista_obiektow.index(ACTIVE)
    print(users[i])
    entry_name.insert(0, users[i].name)
    entry_nazwisko.insert(0, users[i].surname)
    entry_miejscowosc.insert(0, users[i].location)
    entry_liczba_postow.insert(0, users[i].posts)
    button_dodaj_obiekt.config(text="Zapisz", command=lambda: update_user(i))


def update_user(i):
    name = entry_name.get()
    surname = entry_nazwisko.get()
    location = entry_miejscowosc.get()
    post = entry_liczba_postow.get()
    users[i].name = name
    users[i].surname = surname
    users[i].location = location
    users[i].posts = post
    users[i].coordinates=users[i].get_coordinates()
    users[i].marker.delete()
    users[i].marker = map_widget.set_marker(users[i].coordinates[0],users[i].coordinates[1])
    show_users()
    button_dodaj_obiekt.config(text="Dodaj", command=add_user)
    entry_name.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_liczba_postow.delete(0, END)
    entry_name.focus()


def show_user_details():
    i = listbox_lista_obiektow.index(ACTIVE)
    label_imie_szczegoly_obiektu_wartosc.config(text=users[i].name)
    label_nazwisko_szczegoly_obiektu_wartosc.config(text=users[i].surname)
    label_miejscowosc_szczegoly_obiektu_wartosc.config(text=users[i].location)
    label_posty_szczegoly_obiektu_wartosc.config(text=users[i].posts)
    map_widget.set_zoom(12)
    map_widget.set_position(users[i].coordinates[0],users[i].coordinates[1])



root = Tk()

root.title('mr_mapbook')
root.geometry('1200x700')

ramka_lista_obiektow = Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_obiektow = Frame(root)
ramka_mapa = Frame(root)

ramka_lista_obiektow.grid(row=0, column=0, padx=50)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0, columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)

# ramka_lista_obiektow

label_lista_obiektow = Label(ramka_lista_obiektow, text='Lista znajomych')
label_lista_obiektow.grid(row=0, column=0)

listbox_lista_obiektow = Listbox(ramka_lista_obiektow)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)

button_pokaz_szczegoly = Button(ramka_lista_obiektow, text='Pokaż szczegóły', command=show_user_details)
button_pokaz_szczegoly.grid(row=3, column=0)

button_usun_obiekt = Button(ramka_lista_obiektow, text='Usuń obiekt', command=remove_user)
button_usun_obiekt.grid(row=3, column=1)

button_edytuj_obiekt = Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_user)
button_edytuj_obiekt.grid(row=3, column=2)

# ramka_formularz

label_formularz = Label(ramka_formularz, text='Formularz')
label_formularz.grid(row=0, column=1, columnspan=2)

label_name = Label(ramka_formularz, text='Imie')
label_name.grid(row=1, column=0, sticky=W)

label_nazwisko = Label(ramka_formularz, text='Nazwisko')
label_nazwisko.grid(row=2, column=0, sticky=W)

label_miejscowosc = Label(ramka_formularz, text='Miejscowość')
label_miejscowosc.grid(row=3, column=0, sticky=W)

label_posty = Label(ramka_formularz, text='Posty')
label_posty.grid(row=4, column=0, sticky=W)

entry_name = Entry(ramka_formularz)
entry_name.grid(row=1, column=1)
entry_nazwisko = Entry(ramka_formularz)
entry_nazwisko.grid(row=2, column=1)
entry_miejscowosc = Entry(ramka_formularz)
entry_miejscowosc.grid(row=3, column=1)
entry_liczba_postow = Entry(ramka_formularz)
entry_liczba_postow.grid(row=4, column=1)

button_dodaj_obiekt = Button(ramka_formularz, text='Dodaj', command=add_user)
button_dodaj_obiekt.grid(row=5, column=0, columnspan=2)

# ramka_szczegoly_obiektów

label_szczegoly_obiektow = Label(ramka_szczegoly_obiektow, text='Szczegóły użytkownika:')
label_szczegoly_obiektow.grid(row=0, column=0)

label_imie_szczegoly_obiektu = Label(ramka_szczegoly_obiektow, text='Imię:')
label_imie_szczegoly_obiektu.grid(row=1, column=0)

label_imie_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektow, text='.....')
label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=1)

label_nazwisko_szczegoly_obiektu = Label(ramka_szczegoly_obiektow, text='Nazwisko:')
label_nazwisko_szczegoly_obiektu.grid(row=1, column=2)

label_nazwisko_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektow, text='.....')
label_nazwisko_szczegoly_obiektu_wartosc.grid(row=1, column=3)

label_miejscowosc_szczegoly_obiektu = Label(ramka_szczegoly_obiektow, text='Miejscowość:')
label_miejscowosc_szczegoly_obiektu.grid(row=1, column=4)

label_miejscowosc_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektow, text='.....')
label_miejscowosc_szczegoly_obiektu_wartosc.grid(row=1, column=5)

label_posty_szczegoly_obiektu = Label(ramka_szczegoly_obiektow, text='Postów:')
label_posty_szczegoly_obiektu.grid(row=1, column=6)

label_posty_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektow, text='.....')
label_posty_szczegoly_obiektu_wartosc.grid(row=1, column=7)

# ramka_mapa

map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1200, height=450)
map_widget.grid(row=0, column=0, columnspan=2)

map_widget.set_position(52.23, 21.00)
map_widget.set_zoom(6)


def add_user():
    name = entry_name.get()
    print(name)


root.mainloop()
