def computepay(h, r):
    if h<=40:
        pay=h*r
    elif h>40:
        pay= r*40 + ((h-40)*r*1.5)
        return pay
       

   
hrs = float(input("Enter Hours:"))
rate= float(input("enter rate:"))
p = computepay(hrs,rate)
print("Pay", p)
