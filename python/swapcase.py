# Метод swapcase() перетворює всі символи верхнього регістру на символи нижнього регістру, і навпаки.

string = "THIS SHOULD ALL BE LOWERCASE."
print(string.swapcase())
# this should all be lowercase.

string = "this should all be uppercase."
print(string.swapcase())
# THIS SHOULD ALL BE UPPERCASE.

string = "ThIs ShOuLd Be MiXeD cAsEd."
print(string.swapcase())
# tHiS sHoUlD bE mIxEd CaSeD.

# Щоб перетворити рядок лише на нижній регістр, використовуйте функцію lower(), а якщо навпаки — upper().
