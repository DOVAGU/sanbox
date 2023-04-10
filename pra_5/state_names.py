
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
for code, name in CODE_TO_NAME.items():
    print("{:<4s} is {}".format(code, name))

while True:
    state_code = input("Enter state code: ").upper()
    try:
        print("{} is {}".format(state_code, CODE_TO_NAME[state_code]))
    except KeyError:
        print("Invalid state code")
    if state_code == "":
        break

