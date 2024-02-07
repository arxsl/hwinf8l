'''

'''

def calculate(n):
    d = 0
    while n > 0:
        d += n % 10
        n //= 10
    return d

def find_numbers(seq):
    m = 0
    nu = []
    for num in seq:
        d = calculate(num)
        if d > m:
            m = d
            nu = [num]
        elif d == m:
            nu.append(num)
    return nu

seq = [123, 456, 789, 321, 654, 987]
nu = find_numbers(seq)

print("Числа с максимальной суммой цифр:", nu)

