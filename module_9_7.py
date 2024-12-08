
def is_prime(func):
    def do_func(*args, **kwargs):
        k = 0
        n = func(*args, **kwargs)
        for j in range(2, n):
           if n % j == 0:
                k = k + 1
        if k == 0:
            print('Простое')
        else:
            print('Составное')
        return n
    return do_func


@ is_prime
def sum_three(*agrs):
    return sum(agrs)


result = sum_three(2, 3, 6)
print(result)