def convert_temp():
    choice = input("Enter to convert (C)elsius or (F)ahrenheit?: ").upper()
    temp = float(input("Enter temperature: "))

    if choice == "C":
        result = (temp - 32) * 5/9
        print(f"{temp}°F is {result:.2f}°C")
    elif choice == "F":
        result = (temp * 9/5) + 32
        print(f"{temp}°C is {result:.2f}°F")
    else:
        print("Invalid input. Please enter 'C' or 'F'.")

convert_temp()    