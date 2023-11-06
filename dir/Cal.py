"""def fact(k):
    if k==0:
        return 1
    else:
        return k * fact(k+1)

    print(fact(7))"""


"""area =lambda x: x*x
print(area(10))


area1 = lambda x,y :x*y
print(area1(19,9))"""

"""def paka (price_of_apple):
    retrun=(lambda apple_of_shop:paka * price_of_apple)

    x=paka(99)
    print(x(999))"""





"""y= list(filter(lambda x:x%2==0 ,number))
print(y)


number = [1,2,3,4,5,6,7,8,9,10]

m=list(map(lambda x:x*2,number))
print(m)

from functools import reduce

number = [1,2,3,4,5,6,7,8,9,10]

sum=reduce(lambda x,y:x+y,number)
print(sum)"""


"""def new(func):
    def inside(a,b):
        if b==0:
            a,b=b,a
            return func(a,b)
        return inside
def divide(a,b):

    return a/b

divide=new(divide)

print=(divide(20,20))"""

"""def add(a,b):
    return a+b

if__name__=="__main__":
print(add(19,45))
"""
"""print(__name__)"""
