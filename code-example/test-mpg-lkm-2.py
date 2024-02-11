# Приклад коду з можливістю вибору
def liters_100km_to_miles_gallon(litres):
    gallons = litres / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    litres = 3.785411784
    return litres / km100

def convert_fuel_consumption():
    print("Виберіть тип конвертування:")
    print("1. л/100км до миль на галон")
    print("2. миль на галон до л/100км")
    choice = int(input("Введіть номер опції (1 або 2): "))
    
    if choice == 1:
        litres = float(input("Введіть витрату пального у літрах на 100 км: "))
        result = liters_100km_to_miles_gallon(litres)
        print(f"Результат конвертування: {round(result, 2)} mpg")
    elif choice == 2:
        miles = float(input("Введіть витрату пального у милях на галон: "))
        result = miles_gallon_to_liters_100km(miles)
        print(f"Результат конвертування: {round(result, 2)} л/100км")
    else:
        print("Неправильний вибір опції.")

convert_fuel_consumption()
