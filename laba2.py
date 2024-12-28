import math
import timeit
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
        
        
    return r


def barretReductionmu(x, n, w):
    k=len(b)*2
    m=longShiftDigitsToHigh([1], k)
    m=longDivMod(mu, b, w)
    k=len(n)
    q=killLastDigit(x, k-1)
    q=mul(q, m, w)
    q=killLastDigit(q, k+1)
    p=mul(q, n, w)
    r=sub(x, p, w)
    while longCmp(r, n)>=0:
        r=sub(r, n, w)
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

def longDivModost(a, b, w):

    k = len(b)
    r = a  
    q = [0]*(len(a)-len(b)+2)  
    
    while longCmp(r, b)==1 or longCmp(r, b)==0:
        t = len(r)
        c = longShiftDigitsToHigh(b, t - k)  

        if longCmp(r, c)==-1:
            t = t - 1
            c = longShiftDigitsToHigh(b, t - k)
           
        r = sub(r, c, w)
        
        q[-(t-k+1)] = q[-(t-k+1)] + 1
    while len(q) > 1 and q[0] == 0:
        q.pop(0)   
  


    return q, r


def longDivMod(a, b, w):

    k = len(b)
    r = a  
    q = [0]*(len(a)-len(b)+2)  
    
    while longCmp(r, b)==1 or longCmp(r, b)==0:
        t = len(r)
        c = longShiftDigitsToHigh(b, t - k)  

        if longCmp(r, c)==-1:
            t = t - 1
            c = longShiftDigitsToHigh(b, t - k)
           
        r = sub(r, c, w)
        while longCmp(r, c)==1:
            r = sub(r, c, w)
        q[-(t-k+1)] = q[-(t-k+1)] + 1
    while len(q) > 1 and q[0] == 0:
        q.pop(0)   
  


    return q




def gcdlong (a, b, w):
    d=1
    min=1
    
    while a[-1] % 2 == 0 and b[-1] % 2 == 0:
       
       a=shift_right_1_bit(a)
       b=shift_right_1_bit(b)
       
    
       d=d*2
    
    while a[-1]%2==0:
        a=shift_right_1_bit(a)
        
    min= b
    while longCmp(b, [0])==1 and longCmp(a, b)!=0 and longCmp(a, [0])==1:
        '''while b[-1]%2==0:
            b=shift_right_1_bit(b)'''
            
        if longCmp(a, b)==1:
            min=b
            a=sub(a, b, w)
            while longCmp(a, b)==1 and longCmp(a, [0])==1 and longCmp(a, b)!=0 :
                a=sub(a, b, w)
                
                
    
            
        elif longCmp(a, b)==-1:
            min=a
            b=sub(b, a, w)
            
            while longCmp(a, b)==-1 and longCmp(b, [0])==1 and longCmp(a, b)!=0 :
                b=sub(b, a, w)
                #
                
                
        
    
            
    #print(min)
    d=hex(d)[2:] 
    d = hexTo16bit(d)
    d=mul(d, min, w)
    return d

    
def lcmlong(a, b, k, f, w):
    if longCmp(a, b)==0:
        return k

    elif longCmp(k, [1])!=0:
        while f[-1]%2==0 and k[-1]%2==0:
            f=shift_right_1_bit(f)
            k=shift_right_1_bit(k)
        if longCmp(k, [1])!=0:
            f=longDivMod(f, k, w)
        return f
    else:
        return f
    

def addmod(a, b, n, mu, w):
    c=add1(a, b, w)
    c=barretReduction(c, n, mu, w)
    return c

def submod(a, b, n, mu, w):
    c=sub(a, b, w)
    c=barretReduction(c, n, mu, w)
    return c

def mulmod(a, b, n, mu,  w):
    c=mul(a, b, w)
    c=barretReduction(c, n, mu, w)
    return c

def sqmod(a, n, mu, w):
    c=mul(a, a, w)
    c=barretReduction(c, n, mu, w)
    return c

def sqmodmu(a, n, mu, w):
    c=mul(a, a, w)
    c=barretReduction(c, n, mu, w)
    return c

def longModPowerBarrett(a, b, n, mu, w):
    c=[1]
    p=len(b)
    for i in range(p-1, -1, -1):
        if b[i]=='1':
            c=mulmod(c, a, n, mu,  w) 
        a=sqmod(a, n, mu, w)
    return c

def shift_right_1_bit(a):
    carry = 0 
    for i in range(len(a)):
        new_carry = a[i] & 1
        a[i] = (a[i] >> 1) | (carry << 15)
        carry = new_carry
    return a

def hexTo16bit(hex_str):
    if len(hex_str) % 4 != 0:
        hex_str = hex_str.zfill(len(hex_str) + (4 - len(hex_str) % 4))
    return [int(hex_str[i:i+4], 16) for i in range(0, len(hex_str), 4)]

hex_num1 = 0xa8bc4cf832d3b64f83ccb7ae4261a58b090d3a78c2dc2f458d266b8863fb33bf3d39a6206eed2ac69035d1e6455f041c7a31da82d7badfd0cbf84578ade0b86ceffda62e89930a4ab0807da3205f12cb237240c33cba9ff51520fb0a5dc05c6ed096ef25f5b97ab947a608b77179976d7ec36a6b0468a4ef72a3fab1ae9874748613406c3935f444ff54dc0c0b7fa04e5ec39a2522bf418520d6a478ac7fce3f86741f8485da4d5ab8dba5ed68bb2de2f726acc6a0a64908f0fad2688d27aff1d119cb0637b2379e176504136adb19158a0d5f4aab38974517b093f9f80729968d11312fe334f4934a6eeafd74eb9091b3bc1f1c37949ba25a1afbdc3f25003b
#hex_num2 = a8bc4cf832d3b64f83ccb7ae4261a58b090d3a78c2dc2f458d266b8863fb33bf3d39a6206eed2ac69035d1e6455f041c7a31da82d7badfd0cbf84578ade0b86ceffda62e89930a4ab0807da3205f12cb237240c33cba9ff51520fb0a5dc05c6ed096ef25f5b97ab947a608b77179976d7ec36a6b0468a4ef72a3fab1ae9874748613406c3935f444ff54dc0c0b7fa04e5ec39a2522bf418520d6a478ac7fce3f86741f8485da4d5ab8dba5ed68bb2de2f726acc6a0a64908f0fad2688d27aff1d119cb0637b2379e176504136adb19158a0d5f4aab38974517b093f9f80729968d11312fe334f4934a6eeafd74eb9091b3bc1f1c37949ba25a1afbdc3f25003b
hex_num2 = 0x12e58a84c786ed718db8f8326b46747cf2d50c6f172ea07711d232fcaafabce1ecb0588657d66eedee12455307287887e1805e0c1e66fc17a0f0702ab58e222991f8b2c1df308817dbcf286c71b4a224f627c70cd3e23b2dba1fc71fe7ed65f1a44d8088eaa8a71623f4e587ae0164d514a09e4e353aff2a5158f2e1b48ea5977f6461efa616a76f686ac59f46b8855f300cbf14e8af25d202bfc4715c772978bcfb78a8f9d3046da979e571fddc2df062fe12614308e83e842b70460ae33c976420892133021c7743869a6a7f6732bff1b745fedf7643496d991135aff48ec3959eae292290f0408ebbcb4af879abd54efad415438ec0288f7ce78e7e33fe28
hex_num3 = 0xd407ff5ba543ea6760415247b80a0bc04e8ef8c6952636175d4a937f158c91f6b799fd4e46da3283e2e1b27ba86c12c7d0415948da2dfc589c516e793398df0b26bb6ee0ea4aad0d89834752764906b47c595ff3db20095bdce3466d5d521795d63bf833a1c665eab6b20d0fcc711184a479fb0907099758de7cad5514a28c964e28cad898aad7666b085b4cced91462016cfeea010858cb8f180e0806a3fc9ece9c07fb64fcebd5982139e7175b3dd7af7dba204a71634b38bdb09fb654e8e7a693bc8d1cad22483fdb5c6fdcd70f005ee41ae688d37ff9591bd14c21e951b8af702e88f9fb15a2b406d35701e80f9b1456cf7993123c9b1d92d7199b87ca8c



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

binary_num = bin(int(hex_str2, 16))[2:]  
#print(binary_num)



print(f"Число 1: {hex(hex_num1)}")
print(f"Число 2: {hex(hex_num2)}")
'''execution_time = timeit.timeit(lambda: gcdlong(a, b, w), number=1)
print(f"Час виконання: {execution_time}")'''
resultsum = add1(a, b, w)
resultsum1= ''.join(format(x, '04x') for x in resultsum) 
resultsum1 = resultsum1.lstrip('0')
print(f"Результат додавання: {resultsum1}")
resultsub= sub(a, b, w)
resultsub1= ''.join(format(x, '04x') for x in resultsub)
resultsub1 = resultsub1.lstrip('0')
print(f"Результат віднімання: {resultsub1}")
resultmult = mul(a, b, w)
resultmult1= ''.join(format(x, '04x') for x in resultmult) 
resultmult1 = resultmult1.lstrip('0')
print(f"Результат множення: {resultmult1}")

resultdiv, r= longDivModost(a, b, w)
resultdiv1= ''.join(format(x, '04x') for x in resultdiv)
resultdiv1 = resultdiv1.lstrip('0')
r= ''.join(format(x, '04x') for x in r)
r = resultsum1.lstrip('0')
print(f"Результат ділення: {r}")
print(f"Остача: {r}")
 


resulrgcd=gcdlong(a, b,  w)
resulrgcd1= ''.join(format(x, '04x') for x in resulrgcd)
resulrgcd1 = resulrgcd1.lstrip('0')
print(f"НСД: {resulrgcd1}")
print(resulrgcd)

resultlcm=lcmlong(a, b, resulrgcd, resultmult, w)
resultlcm= ''.join(format(x, '04x') for x in resultlcm)
resultlcm = resultlcm.strip('0')
print(f"НСК: {resultlcm}")


k= hex_num3.bit_length()
k=1<<(2*k)
mu= k//hex_num3
mu = hex(mu)[2:]
mu= hexTo16bit(mu)

resultaddmod=addmod(a, b, n, mu, w)
resultaddmod= ''.join(format(x, '04x') for x in resultaddmod)
resultaddmod = resultaddmod.lstrip('0')
print(f"А + B за модулем :{resultaddmod}")

resultsub=submod(a, b, n, mu, w)
resultsub= ''.join(format(x, '04x') for x in resultsub)
resultsub = resultsub.lstrip('0')
print(f"А - B за модулем :{resultsub}")


resultmulmod=mulmod(a, b, n, mu, w)

resultmulmod1= ''.join(format(x, '04x') for x in resultmulmod)
print(f"А * B за модулем :{resultmulmod1}")

resultsqmod=sqmod(a, n, mu, w)
resultsqmod= ''.join(format(x, '04x') for x in resultsqmod)
print(f"А^2 за модулем :{resultsqmod}")

resultlongmod=longModPowerBarrett(a, binary_num, n, mu, w)
resultlongmod= ''.join(format(x, '04x') for x in resultlongmod)
print(f"А^B за модулем N:{resultlongmod}")