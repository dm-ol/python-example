# У модулі calendar є функція month(), яка поверне календар зазначеного місяця у вигляді рядка,
# як показано у прикладі. А функція calendar() видасть цілий рік.

import calendar

july = calendar.month(2024, 7)

print(july)

print(type(july))
# <class 'str'>
