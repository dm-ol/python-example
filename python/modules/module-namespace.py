# Namespace — це простір (розуміється в нефізичному контексті), у якому існують деякі імена,
# які не конфліктують між собою (тобто немає двох різних об’єктів з однаковою назвою).

import math  # import module
print(math.sin(math.pi/2))  # Namespace "math", func "sin"


# Співіснувати двох Namespace (ваш і модульного).

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14

print(sin(pi/2))  # user "pi"
print(math.sin(math.pi/2))  # math "pi"
