# Вивід помилки в коді

try:
    print(10 / 1)
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
except AttributeError as err:
    print(type(err))
    print("Error:", err)
else:
    print("There was no error.")
finally:
    print("Continue...")

# або

try:
    print(10 / 0)
except Exception as err:
    print(type(err))
    print("Error:", err)
else:
    print("There was no error.")
finally:
    print("Continue...")
