# l=[10,15,3,7]
# l.sort()
# print(l)
# a=l[0]
#
# # print(int(mid))
# for i in range(1,4):
#     while a+l[i]==17:
#         print("present")
#     # else:
#     #     print("absent")
def FindPairs(arr, k):
    for i in range(0, len(arr)):
        if k - arr[i] in arr:
            return True
    return False
A = [1, 4, 45, 6, 10, 8]
n = 51
print(FindPairs(A, n))