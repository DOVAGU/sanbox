"""
Emails
Estimate: 20 minutes
Actual:   25 minutes
"""
def extract_name(email):
    parts = email.split("@")
    name = parts[0]
    name_parts = name.split(".")
    full_name = " ".join([part.title() for part in name_parts])
    return full_name


email_to_name = {}
email = input("Email: ")
while email != "":
    name = extract_name(email)
    prompt = f"Is your name {name}? (Y/n) "
    check_name = input(prompt)
    if check_name.lower() == "n":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
