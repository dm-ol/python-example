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


# Example

english = 78
maths = 56
biology = 85

print(f"Ram got total marks {english + maths + biology} out of 300")
