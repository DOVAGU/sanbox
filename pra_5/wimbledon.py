"""
Wimbledon
Estimate: 20 minutes
Actual:   30 minutes
"""

import csv


def read_file(filename):
    champions = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # skip header row
        for row in reader:
            champions.append([row[0], row[1], int(row[2])])
    return champions


def get_champion_counts(champions):
    counts = {}
    for champ in champions:
        name = champ[0]
        if name in counts:
            counts[name] += champ[2]
        else:
            counts[name] = champ[2]
    return counts


def display_champions(champion_counts):
    print("Wimbledon Champions:")
    for name, count in champion_counts.items():
        print(f"{name} {count}")


def get_countries(champions):
    countries = set()
    for champ in champions:
        countries.add(champ[1])
    return sorted(countries)


def display_countries(countries):
    print("These {} countries have won Wimbledon: ".format(len(countries)))
    print(", ".join(countries))


def main():
    champions = read_file("wimbledon.csv")
    champion_counts = get_champion_counts(champions)
    display_champions(champion_counts)
    countries = get_countries(champions)
    display_countries(countries)


if __name__ == '__main__':
    main()
