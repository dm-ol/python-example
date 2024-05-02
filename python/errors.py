# ZeroDivisionError

try:
    print(10 / 0)
except ZeroDivisionError as err:
    print(type(err))
    print("Error:", err)
print("Continue...")
