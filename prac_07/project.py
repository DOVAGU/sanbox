"""
7/5/2023
MENG QINGWEI
"""
from datetime import datetime

class Project:
    """Represent a project with various attributes."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a project from the given values."""
        self.name = name
        self.start_date = datetime.strptime(start_date, '%d/%m/%Y').date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __repr__(self):
        """Return string representation of a Project."""
        return f"{self.name}, Priority={self.priority}, Start Date={self.start_date.strftime('%d/%m/%Y')}, Completion={self.completion_percentage}%"

    def is_complete(self):
        """Determine if the project is complete."""
        return self.completion_percentage == 100
