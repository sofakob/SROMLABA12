import math
def add1(a, b, w):
    n = max(len(a), len(b))
    c = [0] * (n + 1)  
    carry = 0
    max_value = (1 << w) - 1  

   
    if len(a) < len(b):
        a = [0] * (len(b) - len(a)) + a
    elif len(b) < len(a):
        b = [0] * (len(a) - len(b)) + b

   
    for i in range(n-1, -1, -1):  
        temp_sum = a[i] + b[i] + carry
        c[i + 1] = temp_sum & max_value   
        carry = temp_sum >> w 
         
    
    c[0] = carry  

    
    while len(c) > 1 and c[0] == 0:
        c.pop(0)  
    return c 

def longShiftDigitsToHigh(temp, i):
    new_temp = temp + [0] * i
    return new_temp


def sub(a, b, w):
    n= len(a)
    c=[0]*n
    borrow=0
    max_value =  (1 << w) 
    if len(a) < len(b):
        a = [0] * (len(b) - len(a)) + a
    elif len(b) < len(a):
        b = [0] * (len(a) - len(b)) + b

    for i in range(n-1, -1, -1):
        temp=a[i]-b[i]-borrow
        
        if temp>=0:
            c[i]=temp
            borrow=0
        else:
            c[i]=max_value+temp

            borrow=1
    while len(c) > 1 and c[0] == 0:
        c.pop(0)  
    return  c



def mulOneDigit(a, b1, w):
    carry=0
    n=len(a)
    c=[0]*(n+1)
    max_value = (1 <<w) - 1 
    for i in range(n-1,-1, -1 ):
        temp2=a[i]*b1+carry
        c[i+1]=temp2 & max_value
        carry=temp2>>w
    c[0]=carry
    
    while len(c) > 1 and c[0] == 0:
        c.pop(0)
    return c

def mul(a, b, w):
    
    if len(a) < len(b):
        a = [0] * (len(b) - len(a)) + a
    elif len(b) < len(a):
        b = [0] * (len(a) - len(b)) + b
    n1=len(a)
    n2=len(b)
    c=[0]*(n1*n2+1)
    for i in range(n2-1, -1, -1):
        temp3=mulOneDigit(a, b[i], w)  
        temp3=longShiftDigitsToHigh(temp3, n2-i-1)
        c=add1(c, temp3, w)
    while len(c) > 1 and c[0] == 0:
        c.pop(0)
    c= ''.join(format(x, 'x') for x in c) 
    return c

def longDivMod(a, b, w):
    
    if len(a) > len(b):
        b1 = [0] * (len(a) - len(b)) + b
    else:
        b1 = b  

    k = len(b)
    r = a  
    q = 0  
    
    while r >= b1:
        t = len(r)
        c = longShiftDigitsToHigh(b, t - k)  

        if r < c:
            t = t - 1
            c = longShiftDigitsToHigh(b, t - k)
           
        r = sub(r, c, w)
        if len(r)!=len(b1):
            b1=[0]*(len(r)-len(b))+b
        q = q + pow(16, t-k)  
    q=hex(q)
    return q 


     
    

hex_num1 = 0xc9c95a1c5b959df0e2283c9a3a06426955a83daf35afc88883ee2665fb28ade1cf927c551db2fd3277a1310c9fdd258a4d7e8c7854b106938b9ab15a3570989e142d66ad0248e393f3aa77e3d7048a4240d6a9a969e1c3386b4f4edeecdf4cf1655960f3c1b7318c68154cda535bce1a9f8f0685ecaaadb42a299dc4da90ebfa
hex_num2 = 0xa40facc13cdf7169ced90eea3d5943bf2077933ba8e4419a36e3481fbd108636908a791f13307f9f4525c3d670e08e9b8265a84561d20c615c70f5a16057b0f5









hex_str1 = hex(hex_num1)[2:]  
hex_str2 = hex(hex_num2)[2:]  


a = [int(hex_str1[i], 16) for i in range(len(hex_str1))]  
b = [int(hex_str2[i], 16) for i in range(len(hex_str2))] 
w = 4
print(f"Число 1: {hex(hex_num1)}")
print(f"Число 2: {hex(hex_num2)}")
resultsum = add1(a, b, w)
resultsum= ''.join(format(x, 'x') for x in resultsum) 
print(f"Результат додавання: {resultsum}")
resultsub= sub(a, b, w)
resultsub= ''.join(format(x, 'x') for x in resultsub)
print(f"Результат віднімання: {resultsub}")
resultmult = mul(a, b, w)
print(f"Результат множення: {resultmult}")
resultdiv = longDivMod(a, b, w)
print(f"Результат ділення: {resultdiv}")