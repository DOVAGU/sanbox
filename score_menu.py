def get_score():
    while True:
        try:
            score = float(input("Enter score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score, please enter a score between 0 and 100")
        except ValueError:
            print("Invalid input, please enter a number")

def print_result(score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

def show_stars(score):
    print("*" * int(score))

def main():
    score = None
    while True:
        print("\nMENU")
        print("====")
        print("G)et a valid score")
        print("P)rint result")
        print("S)how stars")
        print("Q)uit")

        choice = input("Enter your choice: ").lower()

        if choice == "g":
            score = get_score()
        elif choice == "p":
            if score is not None:
                print_result(score)
            else:
                print("Please enter a valid score first")
        elif choice == "s":
            if score is not None:
                show_stars(score)
            else:
                print("Please enter a valid score first")
        elif choice == "q":
            print("Farewell!")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()
