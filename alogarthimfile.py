# from fractions import Fraction
# print(Fraction(35,177)+Fraction(15,155))
# def gcd(a,b):
#     assert a>=0 and b>=0 and a+b>0
#     if a==0 or b==0:
#         return max(a,b)
#     else:
#         for i in range(min(a,b),0,-1):
#             if a%i==0 and b%i==0:
#                 return i
# print(gcd(24,16))
def gcd(a,b):
    # while a>=b:

       if b==0:
          return a
       else:
          return gcd(b,a%b)
       # print('the numbers are {0}and {1}'.format(a,b))
print(gcd(1980,1848))
# print('the numbers are {0}and {1}'.format(a,b))
print('thr product of {} an {} is {}'.format(2,3,6))
a='abcd , '.join('madhan_kumar ')
print(a)
b=' '.join('xvid')
print(b)
print(17//4)
def lcm(a,b):
    assert a>0 and b>0
    for i in range(1,a*b+1):
        if i%a==0 and i%b==0:
            return i
print(lcm(1980,1848))
def gcd(a,b):
    # while a>=b:

    if b==0:
        return a
    else:
        return gcd(b,a%b)
    # print('the numbers are {0}and {1}'.format(a,b))
print(gcd(10,6))
lcm=(10*6/gcd(10,6))
print(lcm)
print('teh nf {0.3d}'.format(float(1/3)))