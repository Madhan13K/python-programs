# # # list=['a','b','c','d']
# # # new_string=''
# # # #
# # # # new_string=','.join(list)
# # # # print(new_string)
# # # for i in list:
# # #     numbers='1234567890'
# # #     new_string='god\n'.join(numbers)+int(list[i])
# # #     print(new_string)
# # # a=(',').join('xvid')
# # # print(a)
# # #print(n)
# # # Python3 program to largest and smallest digit of a number
# #
# # # Function to the largest and smallest digit of a number
# # def Digits(n):
# #     largest = 0
# #     smallest = 9
# #
# #     while (n):
# #         r = n % 10
# #
# #         # Find the largest digit
# #         largest = max(r, largest)
# #
# #         # Find the smallest digit
# #         smallest = min(r, smallest)
# #
# #         n = n // 10
# #
# #     print(largest,smallest)
# #
# #
# # # Driver code
# #
# # n = 2346
# #
# # # Function call
# # Digits(n)
# #
# # # This code is contributed by mohit kumar 29
# print(ord("A"))
# x=input("enter the fisrt no")
# y=input("enter the sceond no")
# z=input("enter the third no")
# a=str(x)
# b=str(y)
# c=str(z)
# m=int(max(a))+int(max(b))+int(max(c))
# n=int(min(a))+int(min(b))+int(min(c))
# key= m-n
# print(key)
from  scipy.io.wavfile import read
(fs,x)=read("music.wav")
print(fs, x)
import matplotlib.pyplot as plt
plt.plot(x)
plt.show()
import numpy as np
t=np.arrange(x.sixe/float(fs))
plt.plot(t,x)
plt.show()