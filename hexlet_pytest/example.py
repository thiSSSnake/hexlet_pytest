def reverse(string):
    """Reverse string


    >>> reverse('')
    ''
    >>> reverse('Hello')
    'olleH'
    """


    return string[::-1]

# Нужно для запуска тестов из документации
if __name__ == "__main__":
    import doctest
    doctest.testmod()
