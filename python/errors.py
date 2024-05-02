# ZeroDivisionError

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(type(e))
    print("Error:", e)
print("Continue...")
