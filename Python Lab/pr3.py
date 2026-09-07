a = 10
b = 3

print("Arithmetic Operators")
print(a + b) 
print(a - b)  
print(a * b)  
print(a / b)   
print(a // b)  
print(a % b)   
print(a ** b) 

print("\nComparison Operators")
print(a == b)  
print(a != b)  
print(a > b)  
print(a < b)  
print(a >= b)
print(a <= b) 

print("\nLogical Operators")
print(a > 5 and b > 5) 
print(a > 5 or b > 5)  
print(not(a > 5))       

print("\nAssignment Operators")
c = 5
c += 2 
print(c)
c -= 2   
print(c)
c *= 2   
print(c)
c /= 2  
print(c)
c //= 2 
print(c)
c **= 2
print(c)
c %= 3   
print(c)

print("\nBitwise Operators")
x = 5  
y = 3  
print(x & y)  
print(x | y)  
print(x ^ y)  
print(~x)     
print(x << 1) 
print(x >> 1)  

print("\nIdentity Operators")
p = [1, 2, 3]
q = [1, 2, 3]
r = p
print(p is r)      
print(p is q)     
print(p is not q) 

print("\nMembership Operators")
lst = [1, 2, 3, 4]
print(2 in lst)      
print(5 not in lst) 