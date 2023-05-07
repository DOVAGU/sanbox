FILENAME = "subject_data.txt"

def main():
    data = get_data()
    display_subject_details(data)

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = []
    for line in input_file:
        line = line.strip() # Remove the \n
        parts = line.split(',') # Separate the data into its parts
        parts[2] = int(parts[2]) # Make the number an integer (ignore PyCharm's warning)
        subject_data.append(parts) # Append the parts to the subject_data list
        input_file.close()
        return subject_data # Return the nested list

def display_subject_details(data):
    """Displays details of each subject"""
    for subject in data:
        subject_code = subject[0]
        lecturer = subject[1]
        num_students = subject[2]
print(f"{subject_code} is taught by {lecturer} and has {num_students} students")

main()