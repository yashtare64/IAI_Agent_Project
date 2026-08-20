from datetime import datetime


def show_date_time():
    now = datetime.now()
    print("\nCurrent Date:", now.strftime("%d-%m-%Y"))
    print("Current Time:", now.strftime("%I:%M:%S %p"))


def calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)

    if b != 0:
        print("Division:", a / b)
    else:
        print("Cannot divide by zero")


def even_odd():
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")


def temperature():
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9 / 5) + 32
    print("Temperature in Fahrenheit:", f)


def main():
    while True:
        print("\n===== SIMPLE UTILITY AGENT =====")
        print("1. Show Date & Time")
        print("2. Calculator")
        print("3. Even or Odd")
        print("4. Temperature Converter")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_date_time()
        elif choice == "2":
            calculator()
        elif choice == "3":
            even_odd()
        elif choice == "4":
            temperature()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice")


if _name_ == "_main_":
    main()