# Напишіть програму, яка відображає ці зміни і дозволяє попрактикуватися з поняттям списків. Ваше завдання:
# крок 1: створіть порожній список з назвою beatles;
# крок 2: за допомогою методу append() додайте до списку наступних учасників гурту: John Lennon, Paul McCartney та George Harrison;
# крок 3: за допомогою циклу for та методу append() запропонуйте користувачеві додати до списку наступних учасників гурту: Stu Sutcliffe та Pete Best;
# крок 4: за допомогою команди del видаліть зі списку Stu Sutcliffe та Pete Best;
# крок 5: з допомогою методу insert() додайте Ringo Starr на початок списку.
# крок 1
beatles = [] # Створення порожнього списку.
print("Крок 1:", beatles)

# крок  2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Крок 2:", beatles)

# крок 3
add_members = ["Stu Sutcliffe", "Pete Best"]
for member in add_members:
    beatles.append(member)
print("Крок 3:", beatles)

# крок  4
del beatles[3:5]
print("Крок 4:", beatles)

# крок 5
beatles.insert(0, "Ringo Starr")
print("Крок 5:", beatles)

# перевірка довжини списку
print("The Fab", len(beatles))