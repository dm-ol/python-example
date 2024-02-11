# Ця програма обчислює гіпотенузу c.
# a і b — довжини катетів.
try:
    a = float(input("Довжина першого катета:"))
    b = float(input("Довжина другого катета:"))
except ValueError:
    print("Помилка: Будь ласка введіть числове значення.")
    quit()
c = (a ** 2 + b ** 2) ** 0.5  # Ми використовуємо ** замість квадратного кореня.
print("Довжина гіпотенузи:", round(c, 2)) # Округляємо до 2 знаків після коми
