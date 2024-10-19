# При поверхневому копіюванні створюється новий об'єкт, але його внутрішні елементи (якщо вони є об'єктами)
# залишаються посиланнями на ті самі об'єкти, що в оригіналі (копіюються лише посилання об'єкти, але не самі об'єкти).

import copy

original_list = [1, 2, [3, 4]]
shallow_copied_list = copy.copy(original_list)

print(original_list)  # [1, 2, [3, 4]]
print(shallow_copied_list)  # [1, 2, [3, 4]]


# Перевіримо, чи є списки одними і тими ж об'єктами
print(original_list is shallow_copied_list)  # False
# True (вкладений список — той самий об'єкт)
print(original_list[2] is shallow_copied_list[2])

# Зауважте, що зміни у вкладених об'єктах будуть помітні як в оригіналі, так і в його поверхневій копії.
