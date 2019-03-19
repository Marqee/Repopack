'''Return sum of all items in array'''
def sum_array(array):
    return sum(array)


'''Return nth term in fibonacci sequence'''
def fibonacci(n):

    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


'''Return the factorial of a number'''
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n * factorial(n-1)
    '''Return n!'''


''' Return a string in reverse'''
def reverse(word):

    '''Return word in reverse'''
    return word[::-1]
