"""
7/5/2023
MENG QINGWEI
"""
import csv
from datetime import datetime

class Project:
    """Represent information about a project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a Project from the given values."""
        self.name = name
        self.start_date = datetime.strptime(start_date, '%d/%m/%Y')
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __repr__(self):
        """Return string representation of a Project."""
        return f"{self.name} (Priority: {self.priority}) - {self.completion_percentage}% complete"


def load_projects():
    """Load projects from a data file."""
    filename = input("Enter filename to load projects from: ")
    projects = []
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file, delimiter='\t')
            next(reader) # skip header row
            for row in reader:
                project = Project(*row)
                projects.append(project)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return projects


def save_projects(projects):
    """Save projects to a data file."""
    filename = input("Enter filename to save projects to: ")
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file, delimiter='\t')
            writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
            for project in projects:
                writer.writerow([project.name, project.start_date.strftime('%d/%m/%Y'), project.priority, project.cost_estimate, project.completion_percentage])
    except IOError:
        print(f"Error writing to file '{filename}'.")


def display_projects(projects):
    """Display incomplete and complete projects, sorted by priority."""
    incomplete_projects = sorted([project for project in projects if project.completion_percentage < 100], key=lambda x: x.priority)
    complete_projects = sorted([project for project in projects if project.completion_percentage == 100], key=lambda x: x.priority)
    print("\nINCOMPLETE PROJECTS:")
    for project in incomplete_projects:
        print(project)
    print("\nCOMPLETE PROJECTS:")
    for project in complete_projects:
        print(project)

def filter_projects_by_date(projects):
    """Filter and display projects starting after a given date, sorted by date."""
    date_string = input("Enter start date (dd/mm/yyyy): ")
    try:
        date = datetime.strptime(date_string, '%d/%m/%Y')
        filtered_projects = sorted([project for project in projects if project.start_date > date], key=lambda x: x.start_date)
        print(f"\nProjects starting after {date_string}:")
        for project in filtered_projects:
            print(project)
    except ValueError:
        print(f"Invalid date: {date_string}. Format should be dd/mm/yyyy.")

def add_new_project(projects):
    """Add a new project to the list."""
    name = input("Enter project name: ")
    start_date = input("Enter start date (dd/mm/yyyy): ")
    priority = input("Enter priority: ")
    cost_estimate = input("Enter cost estimate: ")
    completion_percentage = input("Enter completion percentage: ")
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)

def filter_projects_by_date(projects):
    """Filter and display projects starting after a given date, sorted by date."""
    date_string = input("Enter start date (dd/mm/yyyy): ")
    try:
        date = datetime.strptime(date_string, '%d/%m/%Y')
        filtered_projects = sorted([project for project in projects if project.start_date > date], key=lambda x: x.start_date)
        print(f"\nProjects starting after {date_string}:")
        for project in filtered_projects:
            print(project)
    except ValueError:
        print(f"Invalid date: {date_string}. Format should be dd/mm/yyyy.")

def update_project(projects):
    """Update an existing project's completion percentage and/or priority."""
    print("Update a project:")
    display_projects(projects)
    project_choice = int(input("Choose a project to update (number): "))
    project = projects[project_choice - 1]
    print(f"Updating {project.name}:")
    new_completion = input(f"Current completion percentage is {project.completion}. Enter new value (or leave blank): ")
    if new_completion:
        project.completion = int(new_completion)
    new_priority = input(f"Current priority is {project.priority}. Enter new value (or leave blank): ")
    if new_priority:
        project.priority = int(new_priority)


def main():
    """Main program loop."""
    print("Welcome to Project Management!")
    projects = []
    filename = input("Enter a file to load projects from (or leave blank for none): ")
    if filename:
        projects = load_projects(filename)
    while True:
        print()
        print("MENU:")
        print("1 - Load projects")
        print("2 - Save projects")
        print("3 - Display projects")
        print("4 - Filter projects by date")
        print("5 - Add new project")
        print("6 - Update project")
        print("7 - Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            filename = input("Enter a file to load projects from: ")
            projects = load_projects(filename)
        elif choice == "2":
            filename = input("Enter a file to save projects to: ")
            save_projects(projects, filename)
        elif choice == "3":
            display_projects(projects)
        elif choice == "4":
            date_str = input("Enter a date to filter by (DD/MM/YYYY): ")
            filtered_projects = filter_projects_by_date(projects, date_str)
            display_projects(filtered_projects)
        elif choice == "5":
            add_new_project(projects)
        elif choice == "6":
            update_project(projects)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
