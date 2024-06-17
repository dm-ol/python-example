# Функція compile() обчислює код Python з вихідного об’єкта та повертає його.

codeInString = 'a = 5\nb=6\nmul=a*b\nprint("mul =",mul)'
codeObject = compile(codeInString, 'multiplyNumbers', 'exec')

exec(codeObject)

# Функція compile() приймає наступні параметри:
#   source — звичайний рядок, байтовий рядок або об’єкт абстрактного синтаксичного дерева (скор. “AST” від англ. “Abstract Syntax Tree”);
#   filename — файл, з якого потрібно прочитати код;
#   mode — варіантами значень є exec (може приймати блок коду зі стейтментами, класом та функціями), eval (приймає один вираз) або single (приймає один стейтмент).
