def print_report(months, incomes):
    """Prints income report for a given number of months."""
    print("\nIncome Report\n-------------")
    total = 0

    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income

    print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

def main():
    """Get income data and display income report."""
    income_list = []
    num_months = int(input("How many months? "))
    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        income_list.append(income)
    print_report(num_months, income_list)

main()