"""..."""


# Create your Place class in this file
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

    def mark_visited(self):
        """Mark the place as visited."""
        self.visited = True

    def mark_unvisited(self):
        """Mark the place as unvisited."""
        self.visited = False

    def is_important(self):
        """Check if the place is considered important."""
        return self.priority <= 2


def run_tests():
    """Test Place class."""
    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malaga", "Spain", 1, False)
    print(new_place)
    assert new_place.name == "Malaga"
    assert new_place.country == "Spain"
    assert new_place.priority == 1
    assert not new_place.visited

    # Test mark_visited() and mark_unvisited()
    print("Test mark_visited() and mark_unvisited():")
    new_place.mark_visited()
    print(new_place)
    assert new_place.visited
    new_place.mark_unvisited()
    print(new_place)
    assert not new_place.visited

    # Test is_important()
    print("Test is_important():")
    important_place = Place("Sydney", "Australia", 2, False)
    print(important_place.is_important())  # True
    unimportant_place = Place("Paris", "France", 3, False)
    print(unimportant_place.is_important())  # False


run_tests()
