# False value in Python. Нуль є значенням false

print(bool(0))  # int value False
print(bool(0.0))  # float value False
print(bool(0j))  # complex value False

# False is False

print(bool(False))

# None is False

print(bool(None))

# Empty types is False

print(bool({}))  # Empty dict
print(bool(()))  # Empty tuple
print(bool([]))  # Empty list
print(bool(""))  # Empty str
print(bool(set()))  # Empty set
print(bool(range(0)))  # Empty range
