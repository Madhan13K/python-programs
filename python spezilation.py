# import re
# hand=open('sample (2).txt')
# for line in hand:
#     line=line.strip()
#     if re.search('From:',line):
#         print(line)
# print('hello world')
# file=open('give.txt')
# print(file.readline())
# print(file.read())
# file.close()
# with open('give1.txt','w') as file:
    # # print(file.readline(34))
    # for line in file:
    #     print(line.upper().strip())
    # file.write('\nthe namme is madhamm kumar')
import os
# os.rename('give.txt','my_name.txt')
# os.path.exists('give.txt')
# os.path.getsize('my_name.txt')
# os.abspath('my_name.txt')
# # os.read()
# print(os.getcwd())
# print(os.listdir('.idea'))
import csv
# f=open('my_name.txt')
# csv_f=csv.reader(f)
# for row in csv_f:
#     name,phone,role=row
#     print(name  +  phone  + role )
# with open('1000 Records.csv') as reader:
#     area=csv.DictReader(reader)
#     for row in area:
#         print('{} has {}'.format(row['Gender'],row['Name Prefix']))
import re
# file=re.search(r'aza','plaza')
# print(file)
# print(re.search(r'^x','xenon'))
# print(re.search(r'p.ng','penguin'))
# print(re.search(r'p.ng','PENGUIN',re.IGNORECASE))
# print(re.search(r'[a-z]way','The end of the highway'))
# print(re.search(r'[a-z]way','The end of the high way'))
# print(re.search(r'[^a-zA-Z ]','this is a sentence with soaces.'))
# print(re.search(r'[^a-zA-Z]','this is a sentence with soaces.'))
# print(re.search(r'cat|dog','i like cats'))
# print(re.search(r'cat|dog','i like dogs'))
# print(re.search(r'cat|dog','i like cats and dogs'))
# print(re.findall(r'cat|dog','i like cats and dogs'))
# print(re.search(r'Py.*n','Python Programming'))
# print(re.search(r'Py[a-z].*n','Python Programming'))
#
# print(re.search(r'o+l+','goldfish'))
# print(re.search(r'p?each','to each their own'))
# print(re.search(r'p?each','to peaches like this'))
# print(re.search(r'.com','welcome'))
# print(re.search(r'\.com','welcome'))
# print(re.search(r'\.com','welcome to my domain.com'))
# print(re.search(r'\w*','and_this_si_another'))
# print(re.search(r'\w*','and this si another'))
# //www.regex.101.com// -reference
# print(re.search(r'A.*a','Argentina'))
# print(re.search(r'A.*a','Azerbaijan'))
# print(re.search(r'A.*a$','Azerbaijan'))
# print(re.search(r'A.*a$','Australia'))
# pattern=r'^'
import random
# rng=RandomNumberGenerator()
# rng.seed(seed)
# from cryptography.fernet import Fernet
# # Put this somewhere safe!
# key = Fernet.generate_key()
# f = Fernet(key)
# token = f.encrypt(b"A really secret message. Not for prying eyes.")
# token
# '...'
# f.decrypt(token)
# 'A really secret message. Not for prying eyes.'
x='my 2 favuroite number are 19 and 42'
y=re.findall('[0-9]+',x)
print(y)
print(re.findall('[AEIOU]+',x))
r='From stephan.marquard@uct.ac.za using the: character'
print(re.findall('^F.+:',r))
print(re.findall('^F.+?:',r))
print(re.findall('\S+@\S+',r))
print(re.findall('^From (\S+@\S+)',r))
print(re.findall('@([^ ]*)',r))