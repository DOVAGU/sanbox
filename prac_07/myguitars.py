class Guitar:
    """Represent information about a guitar."""

    def __init__(self, name, year, cost):
        """Construct a Guitar from the given values."""
        self.name = name
        self.year = year
        self.cost = cost

    def __repr__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """Return True if this guitar is older than the other guitar."""
        return self.year < other.year

guitars = []
with open('guitars.csv', 'r') as file:
    for line in file:
        name, year, cost = line.strip().split(',')
        guitar = Guitar(name, int(year), float(cost))
        guitars.append(guitar)

for guitar in guitars:
    print(guitar)

guitars.sort()
print("Sorted by year:")
for guitar in guitars:
    print(guitar)
