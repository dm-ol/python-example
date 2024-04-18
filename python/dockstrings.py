# Документаційні рядки Python — це рядкові літерали,
# які з’являються відразу після визначення функції, методу, класу або модуля.
# Вказуються у тілі функції та беруться в потрійні (одинарні чи подвійні) лапки.

def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2


def square(n):
    """Takes in a number n, returns the square of n"""
    return n**2


print(square(9))


def add_binary(a, b):
    '''
    Returns the sum of two decimal numbers in binary digits.

            Parameters:
                    a (int): A decimal integer
                    b (int): Another decimal integer

            Returns:
                    binary_sum (str): Binary string of the sum of a and b
    '''
    binary_sum = bin(a+b)[2:]
    return binary_sum


print(add_binary.__doc__)
