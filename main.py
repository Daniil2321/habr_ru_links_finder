import requests, random, socket, webbrowser

run = True

def is_connect():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError as e:
        return False

def main():
    file = open("../links.txt", "a")
    CONNL = 0  # Count Of Not Normal Links
    cicles = True

    while cicles:
        cicle = int(input("Enter the number of cicles: "))
        if cicle != 0:
            cicles = False

    for i in range(cicle):
        id = random.randint(111111, 999999)
        link = f"https://habr.com/ru/articles/{id}/"
        try:
            check = requests.get(link, timeout=5)
            if check.status_code == 404:
                CONNL += 1
            elif check.status_code == 200 or 302:
                print(link)
                file.write(link + "\n")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    print(f"Number of broke links: {CONNL}")
    file.close()

def open_links():
    if is_connect() == True:
        file = open("../links.txt")
        for line in file:
            webbrowser.open(line, new=2)
        file.close()

def check_var():
    file = open("../links.txt")
    for line in file:
        check = requests.get(line)
        print(f"Check status code: {check.status_code}, link: {line}")
    file.close()
def view_links():
    file = open("../links.txt")
    for line in file:
        print(line)
    file.close()

while run:
    if is_connect() == True:
        choice = input("What would you like to do? ")
        if choice == "Find links":
            main()
        elif choice == "Open links":
            open_links()
        elif choice == "Check links":
            check_var()
        elif choice == "View links":
            view_links()
        elif choice == "Exit":
            run = False
        else:
            pass
    elif is_connect() == False:
        print("Conection down")
        run = False

#SOME LINK https://habr.com/ru/articles/324130/   https://habr.com/ru/articles/509846/