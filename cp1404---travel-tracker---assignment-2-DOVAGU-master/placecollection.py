"""..."""


# Create your PlaceCollection class in this file

import csv
from operator import attrgetter

class PlaceCollection:
    def __init__(self):
        self.places = []

    def load_places(self, filename):
        self.places = []
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    name, country, priority, visited = row
                    self.places.append(Place(name, country, int(priority), visited == "v"))
        except FileNotFoundError:
            print(f"{filename} not found")

    def save_places(self, filename):
        try:
            with open(filename, 'w') as file:
                writer = csv.writer(file)
                for place in self.places:
                    visited = "v" if place.is_visited else "n"
                    writer.writerow([place.name, place.country, place.priority, visited])
        except IOError:
            print(f"Error saving {filename}")

    def add_place(self, place):
        self.places.append(place)

    def get_number_of_unvisited_places(self):
        return len([place for place in self.places if not place.visited])

    def sort_places(self, key):
        self.places.sort(key=key)

    def mark_place_visited(self, place):
        """Toggle the visited status of the given place."""
        place.visited = not place.visited


class Place:
    """Represent a place."""

    def __init__(self, name="", country="", priority=0, visited=False):
        """Initialize a Place instance."""
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = visited

    def __str__(self):
        """Return a string representation of the Place."""
        return f"Place: {self.name}, Country: {self.country}, Priority: {self.priority}, Visited: {self.visited}"


def run_tests():
    """Test PlaceCollection class."""
    place_collection = PlaceCollection()

    # Test loading places
    print("Test loading places:")
    place_collection.load_places('places_backup.csv')
    print(place_collection.places)

    # Test adding a new Place with values
    print("Test adding new place:")
    place_collection.add_place(Place("Sydney", "Australia", 4, False))
    print(place_collection.places)

    # Test sorting places
    print("Test sorting - priority:")
    place_collection.sort_places(key=lambda place: place.priority)
    print(place_collection.places)

    # Test marking place as visited
    print("Test marking place as visited:")
    place_collection.mark_place_visited(place_collection.places[0])
    print(place_collection.places)

run_tests()
