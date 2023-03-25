import random

def get_score():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        if score < 50:
            print("Bad")
        elif score < 90:
            print("Passable")
        else:
            print("Excellent")

def main():
    while True:
        print("Main Menu:")
        print("(G)et score")
        print("(R)andom score")
        print("(Q)uit")
        choice = input("Enter your choice: ").upper()
        if choice == "G":
            get_score()
        elif choice == "R":
            score = random.randint(0, 100)
            print("Random score:", score)
            get_score()
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
