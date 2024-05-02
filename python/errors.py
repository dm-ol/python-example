# Вивід помилки в коді

try:
    print(a10 / 0)
except ZeroDivisionError as err:
    print(type(err))
    print("Error:", err)
except TypeError as err:
    print(type(err))
    print("Error:", err)
except SyntaxError as err:
    print(type(err))
    print("Error:", err)
except NameError as err:
    print(type(err))
    print("Error:", err)
except ValueError as err:
    print(type(err))
    print("Error:", err)
print("Continue...")
