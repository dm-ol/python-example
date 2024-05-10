# Тернарний оператор на Python — це всього лиш коротший спосіб записати інструкції if та if...else.

# Normal

def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    if last_char == '?':
        return 'question'
    return 'normal'

# Ternary


def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    return 'question' if last_char == '?' else 'normal'


print(get_type_of_sentence('Hodor'))
print(get_type_of_sentence('Hodor?'))


# Normal

player_points = 90

if player_points > 50:
    print("Наступний рівень")
else:
    print("Повторити рівень")

# Ternary

print("Наступний рівень") if player_points > 50 else print("Повторити рівень")
