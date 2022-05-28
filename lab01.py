def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    depth = n - k
    result = 1
    while n != depth:
        result = result * n
        n = n - 1
    return result

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    n = 0
    result = 0
    while y >= pow(10, n):
        check = pow(10, n)
        n = n + 1
    while y >= 10:
        digit = y // check
        result = result + digit
        y = y % check
        check = check // 10
    result = result + y
    return result # 第一个一次过，嘿嘿
   
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    k = 0
    while n >= pow(10, k):
        check = pow(10, k)
        k = k + 1
    while n >= 10:
        x = n // check
        if x != 8:
            n = n % check
            check = check // 10
        else:
            n = n % check
            check = check // 10
            x = n // check
            if x == 8:
                return True
    return False

# Second week. I spent a lot of time for my internship this week, for which little time was left for the course. Balancing matters!
