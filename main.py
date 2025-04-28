from utils.contoller import get_user_info
from utils.model import users


def main():
    get_user_info(users)
    while True:
        print("=============menu==============")
        print("0 - zamknij aplikacje")
        print("1 - wyświetl co u znajomych")
        print("2- dodaj nowego użytkownika")
        print("3- usun użytkownika")
        print("3- edytuj uzytkownika")
        print("============menu==============")

        choice = input("Wybierz opcje menu")

        if choice ="0":
            break
        if choice ="1":
            get_user_info(users)





        if _name_ = "_main_":
            main()