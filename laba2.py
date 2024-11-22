import math
def killLastDigit(a, n):
    t=len(a)
    c=[0]*(t-n)
    for i in range(t-n):
        c[i]=a[i]
    return c

def barretReduction(x, n, m, w):
    k=len(n)
    q=killLastDigit(x, k-1)
    q=mul(q, m, w)
    q=killLastDigit(q, k+1)
    p=mul(q, n, w)
    r=sub(x, p, w)
    while longCmp(r, n)>=0:
        r=sub(r, n, w)
        print(r)
    return r

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
     
    return c

def longCmp(a, b):
    if len(a) < len(b):
        a = [0] * (len(b) - len(a)) + a
    elif len(b) < len(a):
        b = [0] * (len(a) - len(b)) + b
    n=len(a)
    v=0
    i=0
    for i in range(len(a)):
        if a[i] > b[i]:
            return 1
        elif a[i] < b[i]:
            return -1
    return 0  

def longDivMod(a, b, w):

    k = len(b)
    r = a  
    q = 0  
    
    while longCmp(r, b)==1 or longCmp(r, b)==0:
        t = len(r)
        c = longShiftDigitsToHigh(b, t - k)  

        if longCmp(r, c)==-1:
            t = t - 1
            c = longShiftDigitsToHigh(b, t - k)
           
        r = sub(r, c, w)
        q = q + pow(65536, t-k)  
    q=hex(q)[2:]  
    q = hexTo16bit(q)

    return q, r

'''def gcdlong (a, b, w):
    d=1
    min=1
    print(1)
    while a[-1] % 2 == 0 and b[-1] % 2 == 0:
       a=longDivMod(a, [2], w)
       b=longDivMod(b, [2], w)
       print(2)
       d=d*2
    print(3)
    while a[-1]%2==0:
        a=longDivMod(a, [2], w)
        print(4)
       # print(a, b)
    
    while longCmp(b, [0])==1 and longCmp(a, b)!=0 :
        print(1)
        while b[-1]%2==0:
            b=longDivMod(b, [2], w)
            
        
        if longCmp(a, b)==1:
            min=b
            print(6)
            while longCmp(a, b)==1:
                t=len(a)
                k=len(b)
                c=longShiftDigitsToHigh(b, t-k)
                if longCmp(a, c)==-1:
                    t=t-1
                    c=longShiftDigitsToHigh(b, t-k)
                a=sub(a, c, w)
    
            a, b = b, a
            
        elif longCmp(a, b)==-1:
            print(7)
            min=a
            while longCmp(a, b)==-1:
                t=len(b)
                k=len(a)
                c=longShiftDigitsToHigh(a, t-k)
                if longCmp(b, c)==-1:
                    t=t-1
                    c=longShiftDigitsToHigh(a, t-k)
                b=sub(b, c, w)
            
            
    #print(min)
    d=hex(d)[2:] 
    d = hexTo16bit(d)
    d=mul(d, min, w)
    return d'''


def gcdlong (a, b, w):
    d=1
    min=1
    
    while a[-1] % 2 == 0 and b[-1] % 2 == 0:
       a=longDivMod(a, [2], w)
       b=longDivMod(b, [2], w)
      
       d=d*2
   
    while a[-1]%2==0:
        a=longDivMod(a, [2], w)
        
    
    
    while longCmp(b, [0])==1 and longCmp(a, b)!=0 :
        while b[-1]%2==0:
            b=longDivMod(b, [2], w)
            
        
        if longCmp(a, b)==1:
            min=b
            a=sub(a, b, w)
            a, b = b, a
            
        elif longCmp(a, b)==-1:
            min=a
            b=sub(b, a, w)
            
            
    #print(min)
    d=hex(d)[2:] 
    d = hexTo16bit(d)
    d=mul(d, min, w)
    return d    
def lcmlong(a, b, w):
    c=mul(a, b, w)
    d=gcdlong(a, b, w)
    f=longDivMod(c, d, w)
    return f

def amodn(a, n, w):
   while longCmp(a, n)==1:
       a=sub(a, n,w)
   return a

def addmod(a, b, n, w):
    c=add1(a, b, w)
    k=len(n)*2
    mu=longShiftDigitsToHigh([1], k)
    mu=longDivMod(mu, n, w)
    c=barretReduction(c, n, mu, w)
    return c

def submod(a, b, n, w):
    c=sub(a, b, w)
    k=len(n)*2
    mu=longShiftDigitsToHigh([1], k)
    mu=longDivMod(mu, n, w)
    c=barretReduction(c, n, mu, w)
    return c

def mulmod(a, b, n, w):
    c=mul(a, b, w)
    k=len(n)*2
    mu=longShiftDigitsToHigh([1], k)
    mu=longDivMod(mu, n, w)
    c=barretReduction(c, n, mu, w)
    return c

def sqmod(a, n, w):
    c=mul(a, a, w)
    k=len(n)*2
    mu=longShiftDigitsToHigh([1], k)
    mu=longDivMod(mu, n, w)
    c=barretReduction(c, n, mu, w)
    return c

def sqmodmu(a, n, mu, w):
    c=mul(a, a, w)
    c=barretReduction(c, n, mu, w)
    return c

def longModPowerBarrett(a, b, n, w):
    c=[1]
    k=len(n)*2
    mu=longShiftDigitsToHigh([1], k)
    mu=longDivMod(mu, n, w)
    p=len(b)
    for i in range(p-1, -1, -1):
        if b[i]=='1':
            c=mulmod(c, a, n, w) 
        a=sqmodmu(a, n, mu, w)
    return c


def hexTo16bit(hex_str):
    if len(hex_str) % 4 != 0:
        hex_str = hex_str.zfill(len(hex_str) + (4 - len(hex_str) % 4))
    return [int(hex_str[i:i+4], 16) for i in range(0, len(hex_str), 4)]



hex_num1 = 0xc9c95a1c5b959df0e2283c9a3a06426955a83daf35afc88883ee2665fb28ade1cf927c551db2fd3277a1310c9fdd258a4d7e8c7854b106938b9ab15a3570989e142d66ad0248e393f3aa77e3d7048a4240d6a9a969e1c3386b4f4edeecdf4cf1655960f3c1b7318c68154cda535bce1a9f8f0685ecaaadb42a299dc4da90ebfa
hex_num2 = 0xa40facc13cdf7169ced90eea3d5943bf2077933ba8e4419a36e3481fbd108636908a791f13307f9f4525c3d670e08e9b8265a84561d20c615c70f5a16057b0f5
hex_num3 = 0xefec64f6f415234dacdaeb3bac4d448964527de1cff5414bb79397e3fce5dfe2b8ba751f0a36ff4504c042e61836499a7407862365f8fcc17f71038ffd030b41f3796edd03916614947b9c041f133480b18dd2e3360fb57bf56b91c3fc42a90fe08b5224b6e091405813bf32c9ac4950fb8e203a36fc888f856783370a57b317


'''hex_num1 = 0x3
hex_num2 = 0x15
hex_num3 = 0x5'''
hex_str1 = hex(hex_num1)[2:]  
hex_str2 = hex(hex_num2)[2:]  
hex_str3 = hex(hex_num3)[2:] 

a = hexTo16bit(hex_str1)
b = hexTo16bit(hex_str2)
n = hexTo16bit(hex_str3) 

w = 16

#print(binary_num)

k=len(b)*2
mu=longShiftDigitsToHigh([1], k)
mu=longDivMod(mu, n, w)
print(f"Число 1: {hex(hex_num1)}")
print(f"Число 2: {hex(hex_num2)}")

resultsum = add1(a, b, w)
resultsum= ''.join(format(x, 'x') for x in resultsum) 
print(f"Результат додавання: {resultsum}")
resultsub= sub(a, b, w)
resultsub= ''.join(format(x, 'x') for x in resultsub)
print(f"Результат віднімання: {resultsub}")
resultmult = mul(a, b, w)
resultmult= ''.join(format(x, 'x') for x in resultmult) 
print(f"Результат множення: {resultmult}")

resultdiv, r= longDivMod(a, b, w)
resultdiv= ''.join(format(x, 'x') for x in resultdiv)
r= ''.join(format(x, 'x') for x in r)
print(f"Результат ділення: {resultdiv}")
print(f"Остача: {r}")
 
resulutamodb=amodn(a, b, w)
resulutamodb= ''.join(format(x, 'x') for x in resulutamodb)
print(f"Результат ділення: {resulutamodb}")
resulrgcd=gcdlong(a, b, w)
resulrgcd= ''.join(format(x, 'x') for x in resulrgcd)
print(f"НСД: {resulrgcd}")

resultlcm=lcmlong(a, b, w)
resultlcm= ''.join(format(x, 'x') for x in resultlcm)
print(f"НСК: {resultlcm}")

resultbarret=barretReduction(a, b, mu, w)
resultbarret=''.join(format(x, 'x') for x in resultbarret)
print(f"А за модулем В при використанні редукції:{resultbarret}")

resultaddmod=addmod(a, b, n, w)
resultaddmod= ''.join(format(x, 'x') for x in resultaddmod)
print(f"А + B за модулем :{resultaddmod}")

resultsub=submod(a, b, n, w)
resultsub= ''.join(format(x, 'x') for x in resultsub)
print(f"А - B за модулем :{resultsub}")

resultmulmod=mulmod(a, b, n, w)
resultmulmod= ''.join(format(x, 'x') for x in resultmulmod)
print(f"А * B за модулем :{resultmulmod}")

resultsqmod=sqmod(a, n, w)
resultsqmod= ''.join(format(x, 'x') for x in resultsqmod)
print(f"А^2 за модулем :{resultsqmod}")

resultlongmod=longModPowerBarrett(a, binary_num, n, w)
resultlongmod= ''.join(format(x, 'x') for x in resultlongmod)
print(f"А^B за модулем N:{resultlongmod}")