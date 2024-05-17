# Тестове завдання, таймінг 15:05
while True:
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    if num_2 == 0:
        print("Error! You cannot divide by zero.")
        continue
    print(num_1 / num_2)
    answ = input("Do you want to continue? (yes or no) ")
    if answ == "yes":
        continue
    print("Calculate is over")
    break
