while current_state != "in drawer":


    current_input = input("You can click press (c), hold press (n), or release (r): ")

if current_input == "black":
    if current_input == "c":
        print("Black, c")
    elif current_input == "n":
        print("Black, n")
    elif current_input == "r":
        print("Black, r")
    elif current_input == "d":
        print("Black, d")
    else:
        print(f"I don't recognize the input '{current_input}'")
elif current_input == "white":
    if current_input == "c":
        current_state = "black"
    elif current_input == "n":
        current_state = "red"
    elif current_input == "r":
        current_state = "in drawer"
    elif current_input == "d":
        current_state = "blue"