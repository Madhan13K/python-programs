# # def python_food():
# #     width=80
# #     text='SPAM AND EGGS'
# #     left_margin=(width-len(text))//2
# #     print(' '*left_margin,text)
# # def centre_text(*args):
# #     text=' '
# #     for arg in args:
# #         text+=str(arg)+' '
# #     left_margin=(80-len(text))//2
# #     print(' '*left_margin,text, end=end ,flush=flush,file=file)
# #
# # centre_text('spam and eggs')
# # centre_text('spam,spam,and eggs')
# # centre_text(str(12))
# # centre_text('spam,spam,spam,and spam')
# # print('first','second',3,4,'spam')
# import sqlite3
#
# conn = sqlite3.connect('emaildb.sqlite')
# cur = conn.cursor()
#
# cur.execute('DROP TABLE IF EXISTS Counts')
#
# cur.execute('''
# CREATE TABLE Counts (org TEXT, count INTEGER)''')
#
# fname = input('Enter file name: ')
# if (len(fname) < 1): fname = 'mbox-short.txt'
# fh = open(fname)
# for line in fh:
#     if not line.startswith('From: '): continue
#     pieces = line.split()
#     org = pieces[1]
#     cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('''INSERT INTO Counts (org, count)
#                 VALUES (?, 1)''', (org,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
#                     (org,))
#     conn.commit()
#
# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
#
# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])
#
# cur.close()



# import sqlite3
#
# conn = sqlite3.connect('Counts.sqlite')
# cur = conn.cursor()
#
# cur.execute('DROP TABLE IF EXISTS Counts')
#
# cur.execute('''
# CREATE TABLE Counts (org TEXT, count INTEGER)''')
#
# fname = input('Enter file name: ')
# if (len(fname) < 1): fname = 'mbox.txt'
# fh = open(fname)
# for line in fh:
#     if not line.startswith('From: '): continue
#     pieces = line.split()
#     email = pieces[1]
#     email = line.split("@")
#     email = email[1]
#     email = email.split("\n")
#     email = email[0]
#     cur.execute('SELECT count FROM Counts WHERE org = ? ', (email,))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('''INSERT INTO Counts (org, count)
#                 VALUES (?, 1)''', (email,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
#                     (email,))
#     conn.commit()
#
# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
#
# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])
#
# cur.close()


import json
import sqlite3

conn = sqlite3.connect('assignment_15_3.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;
CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);
CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);
CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0];
    title = entry[1];
    role = entry[2];

    print((name, title, role))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
                ( user_id, course_id, role ) )

    conn.commit()