# Chef went to a shop and buys a pens and b pencils. Each pen costs x units and each pencil costs y units. Now find what is the total amount Chef will spend to buy a pens and b pencils.

a = int(input("pens: "))

b = int(input("pencils: "))

x = int(input("cost of pens: "))

y = int(input("cost of pencils: "))

def buy(a,b,x,y):
    ans = a*x + b*y
    return ans
     
print(buy(a,b,x,y))