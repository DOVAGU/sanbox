"""
Name:meng qingwei
Date started:22/4/2023
GitHub URL:
"""
import csv
import random

FILENAME = "places.csv"


def main():
    print("Travel Tracker 1.0 - by meng qingwei")
    places = load_places()
    print(f"{len(places)} places loaded from {FILENAME}")

    while True:
        print("\nMenu:")
        print("L - List places")
        print("R - Recommend random place")
        print("A - Add new place")
        print("M - Mark a place as visited")
        print("Q - Quit")

        choice = input(">>> ").upper()

        if choice == "L":
            list_places(places)
        elif choice == "R":
            recommend_place(places)
        elif choice == "A":
            add_place(places)
        elif choice == "M":
            mark_place_visited(places)
        elif choice == "Q":
            save_places(places)
            print(f"{len(places)} places saved to {FILENAME}")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")


def load_places():
    places = []
    try:
        with open(FILENAME) as file:
            reader = csv.reader(file)
            for row in reader:
                name, country, priority, visited = row
                places.append({"name": name, "country": country,
                               "priority": int(priority), "visited": visited == "v"})
    except FileNotFoundError:
        print(f"{FILENAME} not found, creating new file...")
        file = open(FILENAME, "w")
        file.close()
    return places


def list_places(places):
    places.sort(key=lambda x: (x["visited"], -x["priority"]))
    for i, place in enumerate(places):
        mark = "*" if place["visited"] else " "
        print(f"{mark}{i+1}. {place['name']} in {place['country']} {place['priority']}")
    unvisited_count = len([p for p in places if not p["visited"]])
    print(f"{len(places)} places. You still want to visit {unvisited_count} places.")


def recommend_place(places):
    unvisited_places = [p for p in places if not p["visited"]]
    if unvisited_places:
        random_place = random.choice(unvisited_places)
        print(f"Not sure where to visit next?\nHow about... {random_place['name']} in {random_place['country']}?")
    else:
        print("No places left to visit!")


def add_place(places):
    name = input("Name: ").strip()
    while not name:
        print("Input can not be blank")
        name = input("Name: ").strip()

    country = input("Country: ").strip()
    while not country:
        print("Input can not be blank")
        country = input("Country: ").strip()

    priority = input("Priority: ")
    while not priority.isdigit():
        print("Invalid input; enter a valid number")
        priority = input("Priority: ")

    places.append({"name": name, "country": country,
                   "priority": int(priority), "visited": False})
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker")


def mark_place_visited(places):
    unvisited_places = [p for p in places if not p["visited"]]
    if not unvisited_places:
        print("No unvisited places")
        return

    list_places(places)
    while True:
        choice = input("Enter the number of a place to mark as visited\n>>> ")
        if not choice.isdigit():
            print("Invalid input; enter avalid number")
        continue
        choice = int(choice)
        if choice < 1 or choice > len(places):
            print("Invalid place number")
            continue

        place = places[choice - 1]
        if place["visited"]:
            print(f"You have already visited {place['name']}")
        else:
            place["visited"] = True
            print(f"{place['name']} in {place['country']} visited!")
        break

def save_places(places):
    with open(FILENAME, "w") as file:
        writer = csv.writer(file)
        for place in places:
            writer.writerow([place["name"], place["country"],place["priority"], "v" if place["visited"] else "n"])

if __name__ == "__main__":
    main()

