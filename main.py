'''

'''

m = 0
n = 0
a = int(input())
for i in range(a):
    
    b = int(input())
    if b > m:
        
        m = b
        
    if b == 0:
        
        n = 1
        
print(m)
    
if n > 0:
    print('YES')
else:
    print('NO')