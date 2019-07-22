
def isPrime(num):
    ''' If given number is prime it returns true otherwise false'''
    if num < 2:
        return False
    else:
        for i in range(2, num// 2 + 1):
            if num % i == 0:
                return False
    return True
