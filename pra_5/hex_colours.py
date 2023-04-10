COLOR_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "blanchedalmond": "#ffebcd",
    "blueviolet": "#8a2be2",
    "burlywood": "#deb887",
    "cadetblue": "#5f9ea0"
}

while True:
    color_name = input("Enter a color name: ").lower()
    if color_name == "":
        break
    try:
        print(f"{color_name.capitalize()} has code {COLOR_CODES[color_name]}")
    except KeyError:
        print("Invalid color name")
