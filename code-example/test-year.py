year = int(input("Введіть рік: "))

if year < 1582:
    print("Не в межах григоріанського календарного періоду")
else:
    if year % 4 != 0:
        print("Звичайний рік")
    elif year % 100 != 0:
        print("Високосний рік")
    elif year % 400 != 0:
        print("Звичайний рік")
    else:
        print("Високосний рік")
