
def add1(a, b, w):
    n = len(a)
    c = [0] * n  
    carry = 0
    max_value = (1 << w) - 1  

    for i in range(n):
        temp1 = a[i] + b[i] + carry  
        c[i] = temp1 & max_value  
        carry = temp1 >> w  
        
    return c  

def longShiftDigitsToHigh(temp, i):
    n = len(temp)
    
   
    new_temp = [0] * n
    
   
    for j in range(n - i):
        new_temp[j] = temp[j + i]
    
    return new_temp

def sub(a, b, w):
    n= len(a)
    c=[0]*n
    borrow=0
    max_value = (1 << w)

    for i in range(n):
        temp=a[i]-b[i]-borrow
        if temp>=0:
            c[i]=temp
            borrow=0
        else:
            c[i]=max_value+temp
            borrow=1
    return c


def mulOneDigit(a, b1, w):
    carry=0
    n=len(a)+1
    c=[0]*n
    n=n-1
    max_value = (1 << w) - 1 
    for i in range(n):
        temp2=a[i]*b1+carry
        c[i]=temp2 & max_value
        carry=temp2>>w
        c[n]=carry
    return c

def mul(a, b, w):
    n1=len(a)
    n2=len(b)
    c=[0]*(n1*n2)
    for i in range(n2):
        temp3=mulOneDigit(a, b[i], w)
        temp3=longShiftDigitsToHigh(temp3, i)
        c=add1(c, temp3, w)
       
      
    return c

def longDivMod(a, b, w):
     k=len(b)
     r=a
     q=0
     while r>=b:
         t=len(r)
         c=longShiftDigitsToHigh(b, t-k) 
         if r<c:
             t=t-1
             c=longShiftDigitsToHigh(b, t-k)
         r=sub(r, c, w)
         q=q+(1<<(t-k))
     return [q]

     
    

hex_num1 = 0xc74247932cbe58d3e8d3499c2635b6da
hex_num2 = 0xf63659ccf23cb1fc77f5bc4c7c1e4


a = [hex_num1]
b = [hex_num2]
w = 2048



resultsum = add1(a, b, w)
resultsub= sub(a, b, w)
resultmult = mul(a, b, w)
resultdiv = longDivMod(a, b, w)

print(f"Число 1: {hex(hex_num1)}")
print(f"Число 2: {hex(hex_num2)}")
#print(f"Для мене:{hex(d)}")
print(f"Результат додавання: {[hex(x) for x in resultsum]}")
#print(f"Перенос: {hex(carry)}")
print(f"Результат віднімання: {[hex(x) for x in resultsub]}")
#print(f"Перенос: {hex(borrow)}")
print(f"Результат множення: {[hex(x) for x in resultmult]}")
print(f"Результат ділення: {[hex(x) for x in resultdiv]}")

