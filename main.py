'''

'''

def U(a, base):
    
    alf = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if a == 0:
        
        return alf[0]

    n = []
    while a > 0:
        
        e = a % base
        a = a // base 
        n.append(alf[e])

    return ''.join(reversed(n))
    
a = int('105', 8) + (5 * 37 + 15) * int('1011', 3) ** int('BA', 15)
m = U(a, 24)
n = 0
for i in m:
    
    if i == 'H':
        
        n += 1

print(n)
