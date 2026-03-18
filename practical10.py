def make_choice(num):
    print("1. Binary")
    print("2. Octal")
    print("3. Hexadecimal")
    print("4. Exit")

    choice = int(input("Convert into (1/2/3/4): "))

    if choice == 1:
        print("Binary =", bin(num))
    elif choice == 2:
        print("Octal =", oct(num))
    elif choice == 3:
        print("Hexadecimal =", hex(num))
    elif choice == 4:
        print("Exiting...")
        return False  
    else:
        print("Invalid choice")
        return True  

print("--------Base Conversion Program-----------")
num = int(input("Enter a number: "))
while True:
    if make_choice(num) == False:
        break
