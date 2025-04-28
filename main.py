users:list=[
    {"name":"Mateusz","location":"Węgorzewo","posts": 100},
    {"name": "Wiktoria", "location": "Chełm", "posts": 6},
    {"name": "Sabina", "location": "Opole", "posts": 110},
    {"name": "Weronika", "location": "Tomaszów Mazowiecki", "posts": 300},
    {"name": "Julia", "location": "Zyrardów", "posts": 50},

]

print(f"Witaj {users[0]["name"]}")

for user in users:
    print(f"Twój znajomy {user["name"]} z {user["location"]} opublikował {user["posts"]} postów")