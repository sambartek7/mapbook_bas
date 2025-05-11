from utils.controller import get_user_info, add_user, remove_user, update_user, get_map
from utils.model import users  # Zakładam, że plik model.py zawiera listę `users`

def main():
    while True:
        print("\n========== MENU ============")
        print("0 - zamknij aplikację")
        print("1 - wyświetl co u znajomych")
        print("2 - dodaj nowego użytkownika")
        print("3 - usuń użytkownika")
        print("4 - edytuj użytkownika")
        print("5 - przygotuj mapę znajomych")
        print("============================")

        choice = input("Wybierz opcję menu: ")
        if choice == '0':
            print("Zamykanie aplikacji...")
            break
        elif choice == '1':
            get_user_info(users)
        elif choice == '2':
            add_user(users)
        elif choice == '3':
            remove_user(users)
        elif choice == '4':
            update_user(users)
        elif choice == '5':
            get_map(users)
        else:
            print("Niepoprawny wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()








