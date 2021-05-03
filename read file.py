# # host=([1,'gold'],[3,'platinum'],[2,'silver'])
# # ra=[4,'mam',5,'god']
# #
# # with open('file.txt','a') as host_file:
# #   for lines in host_file:
# #      ra.append(lines)
# #
# # print(ra)
# # host_file.close()
# for i in range(100000,100999):
#     if i%9127==0:
#         print(i)
import itertools as it

def is_solution(perm):
    for (i1, i2) in it.combinations(range(len(perm)), 2):
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False

    return True

for perm in it.permutations(range(10)):
    if is_solution(perm):
        print(perm)
        exit()
