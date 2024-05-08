'''

'''

def count_zeros(n):
    n_base_three = ''
    while n > 0:
        n_base_three = str(n % 3) + n_base_three
        n //= 3
    return n_base_three.count('0')

r = 4**3 * 3**19
zeros = count_zeros(r)

print(zeros)
