import datetime

# Formating strings

str_1 = "Very good?"
str_2 = "Yes! Very good!"

str_3 = f"{str_1} {str_2}"

print(str_3)  # Very good? Yes! Very good!

# Prints today's date with help
# of datetime library

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")
