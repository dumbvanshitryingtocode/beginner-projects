# Starting the program
while True:
    # Display category
    print("Unit converter")
    print("1. Length")
    print("2. Weight")
    print("3. Time")
    print("4. Currency")
    print("5. Exit")

    # Ask to select category
    choice = int(input("Select a category (1-5): "))

    # Select the conversion units
    if choice == 5:
        print("Exiting the program...")
        break
    elif choice == 1:
        units = {"km": 1000, "m": 1, "cm": 0.01, "mm": 0.001,
                 "mi": 1609.34, "yd": 0.9144, "ft": 0.3048, "in": 0.0254}
    elif choice == 2:
        units = {"kg": 1, "g": 0.001, "mg": 0.000001,
                 "lb": 0.453592, "oz": 0.0283495}
    elif choice == 3:
        units = {"s": 1, "min": 60, "h": 3600, "d": 86400}
    elif choice == 4:
        units = {"USD": 1, "EUR": 0.85, "Rs": 73.5, "GBP": 0.75,
                 "JPY": 110.0, "CAD": 1.25}
    else:
        print("Invalid choice. Please select a valid category.")
        continue

    print("Available units:", ", ".join(units))
    from_unit = input("Convert from: ").strip()
    to_unit = input("Convert to: ").strip()

    if from_unit not in units or to_unit not in units:
        print("Invalid unit.")
        continue

    value = float(input(f"Enter value in {from_unit}: "))
    base_value = value * units[from_unit]
    result = base_value / units[to_unit]
    print(f"Result: {result} {to_unit}")




