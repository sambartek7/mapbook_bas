from tkinter import *

import tkintermapview

root = Tk()

root.title('mapbook_bas')
root.geometry('1200x700')

ramka_lista_obiektow = Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_obiektow = Frame(root)
ramka_mapa = Frame(root)

ramka_lista_obiektow.grid(row=0, column=0, padx=50)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0)
ramka_mapa.grid(row=2, column=0, columnspan=2)
#ramka_lista_obiektow

label_lista_obiektow = Label(ramka_lista_obiektow, text='Lista znajomych')
label_lista_obiektow.grid(row=0, column=0)

listbox_lista_obiektów = Listbox(ramka_lista_obiektow)
listbox_lista_obiektów.grid(row=1, column=0, columnspan=3)

button_pokaz_szczegoly = Button(ramka_lista_obiektow, text='Pokaż szczegóły')
button_pokaz_szczegoly.grid(row=3, column=0)

button_usun_obiekt = Button(ramka_lista_obiektow, text='Usuń obiekt')
button_usun_obiekt.grid(row=3, column=1)

button_edytuj_obiekt = Button(ramka_lista_obiektow, text='Edytuj obiekt')
button_edytuj_obiekt.grid(row=3, column=2)

#ramka_formularz

label_formularz = Label(ramka_formularz, text='Formularz')
label_formularz.grid(row=0, column=1, columnspan=2)

label_imie = Label(ramka_formularz, text='Imie')
label_imie.grid(row=1, column=0, sticky=W)

label_nazwisko = Label(ramka_formularz, text='Nazwisko')
label_nazwisko.grid(row=2, column=0, sticky=W)

label_miejscowosc = Label(ramka_formularz, text='Miejscowość')
label_miejscowosc.grid(row=3, column=0, sticky=W)

label_posty = Label(ramka_formularz, text='Liczba Postów')
label_posty.grid(row=4, column=0, sticky=W)

entry_imie = Entry(ramka_formularz)
entry_imie.grid(row=1, column=1)

entry_nazwisko = Entry(ramka_formularz)
entry_nazwisko.grid(row=2, column=1)

entry_miejscowosc = Entry(ramka_formularz)
entry_miejscowosc.grid(row=3, column=1)

entry_posty = Entry(ramka_formularz)
entry_posty.grid(row=4, column=1)

button_dodaj_obiekt = Button(ramka_formularz, text='Dodaj')
button_dodaj_obiekt.grid(row=5, column=0, columnspan=2)

#ramka_szczegoly_obiektu

label_szczegoly_obiektu = Label(ramka_szczegoly_obiektow, text='Szczegóły użytkownika:')
label_szczegoly_obiektu.grid(row=0, column=0)

label_imie_szczegoly_obiektu = Label(ramka_szczegoly_obiektow, text='Imie:')
label_imie_szczegoly_obiektu.grid(row=1, column=0)

label_imie_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektow, text='.....')
label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=1)

label_nazwisko_szczegoly_obiektu = Label(ramka_szczegoly_obiektow, text='Nazwisko:')
label_nazwisko_szczegoly_obiektu.grid(row=1, column=2)

label_nazwisko_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektow, text='.....')
label_nazwisko_szczegoly_obiektu_wartosc.grid(row=1, column=3)

label_miejscowosc_szczegoly_obiektu_wartosc=Label(ramka_szczegoly_obiektow, text='Miejscowość')
label_miejscowosc_szczegoly_obiektu_wartosc.grid(row=1, column=4)

label_miejscowosc_szczegoly_obiektu_wartosc=Label(ramka_szczegoly_obiektow, text='.....')
label_miejscowosc_szczegoly_obiektu_wartosc.grid(row=1, column=5)

label_posty_szczegoly_obiektu_wartosc=Label(ramka_szczegoly_obiektow, text='Postów')
label_posty_szczegoly_obiektu_wartosc.grid(row=1, column=6)

label_posty_szczegoly_obiektu_wartosc=Label(ramka_szczegoly_obiektow, text='.....')
label_posty_szczegoly_obiektu_wartosc.grid(row=1, column=7)

#ramka_mapa

map_widget=tkintermapview.TkinterMapView(ramka_mapa, width=800, height=600)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.set_position(52.23, 21.00)
map_widget.set_zoom(6)



root.mainloop()








