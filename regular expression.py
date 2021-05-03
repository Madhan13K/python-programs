# import re
# name = input("Enter file:")
# if len(name) < 1 : name = "test.txt"
# fh = open(name)
# newlist = list()
# for line in fh :
#     line = re.findall('[0-9]+', line)  #finds all numbers '.[0-9]*[0-9]' was before and it missed py4e.com and etx
#     for number in line :
#         newlist.append(int(number)) # creates newlist with int line values
# print(sum(newlist))
# import re
# lis=list()
# f=open('give.txt')
# for lines in f:
#     line=re.findall('[0-9]+',lines)
#     for num in line:
#         lis.append(int(num))
#
# print(sum(lis))
# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
#
# mysock.close()
# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
#
# lit = list()
# while True:
#     data = mysock.recv(512)
#     lit.append(data)
#     if (len(data) < 1):
#         break
#     print(data.decode())
# mysock.close()
# print(ord('e'))

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))
#
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl
#
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# html = urlopen('', context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")
# tags = soup('span')
# sum = 0
# coun = 0
# print('Enter - ')
# for tag in tags:
#     coun += 1
#     sum += int(tag.contents[0])
# print('Count', coun, '\nSum', sum)


# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter URL: ')
# num = input('Enter count: ')
# pos = input('Enter position: ')
# print('Retrieving: ', url)
# for times in range(int(num)):
#     html = urllib.request.urlopen(url, context=ctx).read()
#     soup = BeautifulSoup(html, 'html.parser')
#     tags = soup('a')
#     print('Retrieving: ', tags[int(pos)-1].get('href', None))
#     url = tags[int(pos)-1].get('href', None) http://py4e-data.dr-chuck.net/known_by_Nyomi.html


# import xml.etree.ElementTree as ET
#
# input = '''
# <stuff>
#   <users>
#     <user x="2">
#       <id>001</id>
#       <name>Chuck</name>
#     </user>
#     <user x="7">
#       <id>009</id>
#       <name>Brent</name>
#     </user>
#   </users>
# </stuff>'''
#
# stuff = ET.fromstring(input)
# lst = stuff.findall('users/user')
# print('User count:', len(lst))
#
# for item in lst:
#     print('Name', item.find('name').text)
#     print('Id', item.find('id').text)
#     print('Attribute', item.get('x'))


# import urllib.request, urllib.parse, urllib.error
# import xml.etree.ElementTree as ET
# import ssl
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter location: ')
# print ('Retrieving ', url)
# html = urllib.request.urlopen(url, context=ctx).read()
# print ('Retrieved', len(html), 'characters')
# tree = ET.fromstring(html)
# print ('Count: ',len(tree.findall('.//count')))
# total = 0
# for r in tree.findall("./comments/comment"):
#     total += int(r.find('count').text)
# print ('Sum: ', total)

# import urllib.request, urllib.parse, urllib.error
# import json
#
# url = input('Enter location: ')
# data = urllib.request.urlopen(url).read()
# info = json.loads(data)
# info = info['comments']
# print ('Retrieving', url, '\nRetrieved', len(data), 'caracters', '\nCount:', len(info))
# num = 0
# for item in info:
#     num += int(item['count'])
# print ('Sum:', num)



import urllib.request, urllib.parse, urllib.error
# import json
#
# serviceurl = 'http://python-data.dr-chuck.net/geojson'
# address = input('Enter location: ')
# url = serviceurl + '?' + urllib.parse.urlencode({'sensor':'false', 'address':  address})
# data = urllib.request.urlopen(url).read().decode()
# info = json.loads(data)
# info = info['results']
# print ('Retrieving', url, '\nRetrieved', len(data), 'caracters')
# for item in info:
#     key = item['place_id']
# print ('Place id:', key)


# import json
#
# data = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Chuck"
#   }
# ]'''
#
# info = json.loads(data)
# print('User count:', len(info))
#
# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])


#
# import urllib.request, urllib.parse, urllib.error
# import json
#
# # Note that Google is increasingly requiring keys
# # for this API
# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
#
# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break
#
#     url = serviceurl + urllib.parse.urlencode(
#         {'address': address})
#
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url)
#     data = uh.read().decode()
#     print('Retrieved', len(data), 'characters')
#
#     try:
#         js = json.loads(data)
#     except:
#         js = None
#
#     if not js or 'status' not in js or js['status'] != 'OK':
#         print('==== Failure To Retrieve ====')
#         print(data)
#         continue
#
#     print(json.dumps(js, indent=4))
#
#     lat = js["results"][0]["geometry"]["location"]["lat"]
#     lng = js["results"][0]["geometry"]["location"]["lng"]
#     print('lat', lat, 'lng', lng)
#     location = js['results'][0]['formatted_address']
#     print(location)


import json
# import urllib.request, urllib.parse, urllib.error
# import xml.etree.ElementTree as ET
#
# place_name = input("Enter a place name: ")
# base_url = "http://python-data.dr-chuck.net/geojson?sensor=false&"
# address_param = urllib.parse.urlencode({'address': place_name})
# target = base_url + address_param
#
# print ("Retrieving {0}".format(target))
# connection = urllib.request.urlopen(target)
# raw_data = connection.read()
# print ("Retrieved {0} characters".format(len(raw_data)))
# parsed_data = json.loads(raw_data)
#
# #print(parsed_data)
# print ("Place id", parsed_data["results"][0]["place_id"])

# import urllib.request, urllib.parse, urllib.error
# import json
#
# # Initialising
# service_url = 'http://py4e-data.dr-chuck.net/geojson?'
#
# # Asking user to input the source URL of the JSON data file
# loc = input('Enter location: ')
#
# # Concatinating the URL for the request
# url = service_url + urllib.parse.urlencode({'address' : loc})
# print('Retrieving', loc, 'here:', url)
#
# # Opening connection to the JSON data file
# uhandle = urllib.request.urlopen(url)
# data = uhandle.read().decode()
# print('Retrieved', len(data), 'characters')
#
# # Transforming the text of the JSON file into a tree
# try:
#     tree = json.loads(data)
# except:
#     tree = None
#
# # Finding the first "place_id" in the JSON data file
# place_id = tree["results"][0]["place_id"]
#
# # Printing the result
# print('Place ID:', place_id)


# import urllib
# import json
#
# serviceurl = 'http://python-data.dr-chuck.net/geojson?'
#
# address = input('Enter location: ')
# url = serviceurl + urllib.urlopen({'sensor':'false', 'address': address})
# print('Retrieving', url)
# uh = urllib.urlopen(url)
# data = uh.read()
# print('Retrieved',len(data),'characters')
# try: js = json.loads(str(data))
# except: js = None
# if 'status' not in js or js['status'] != 'OK':
#     print('==== Failure To Retrieve ====')
#     print(data)
#
# placeid = js["results"][0]["place_id"]
# print('Place ID ', placeid )


import urllib.request, urllib.parse, urllib.error
# import json
#
# serviceurl = 'http://python-data.dr-chuck.net/geojson'
# address = input('Enter location: ')
# url = serviceurl + '?' + urllib.parse.urlencode({'sensor':'false', 'address':  address})
# data = urllib.request.urlopen(url).read().decode()
# info = json.loads(data)
# info = info['results']
# print ('Retrieving', url, '\nRetrieved', len(data), 'caracters')
# for item in info:
#     key = item['place_id']
# print ('Place id:', key)


# import urllib.request, urllib.parse, urllib.error
# import json
#
# # Note that Google is increasingly requiring keys
# # for this API
# serviceurl =  'http://py4e-data.dr-chuck.net/json?'
#
# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break
#
#     url = serviceurl + urllib.parse.urlencode(
#         {'address': address})
#
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url)
#     data = uh.read().decode()
#     print('Retrieved', len(data), 'characters')
#
#     try:
#         js = json.loads(data)
#     except:
#         js = None
#
#     if not js or 'status' not in js or js['status'] != 'OK':
#         print('==== Failure To Retrieve ====')
#         print(data)
#         continue
#
#     #print(json.dumps(js, indent=4))
#
#     #lat = js["results"][0]["geometry"]["location"]["lat"]
#     #lng = js["results"][0]["geometry"]["location"]["lng"]
#     #print('lat', lat, 'lng', lng)
#     #location = js['results'][0]['formatted_address']
#     placeID=js['results'][0]['place_id']
#     print('The place Id of the place',address,'you entered is',placeID)


# import urllib.request as ur
# import urllib.parse as up
# import json
#
# serviceurl = "http://python-data.dr-chuck.net/geojson?"
#
# address_input = input("Enter location: ")
# params = {"sensor": "false", "address": address_input}
# url = serviceurl + up.urlencode(params)
# print("Retrieving ", url)
# data = ur.urlopen(url).read().decode('utf-8')
# print('Retrieved', len(data), 'characters')
# json_obj = json.loads(data)
#
# place_id = json_obj["results"][0]["place_id"]
# print("Place id", place_id)



import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
