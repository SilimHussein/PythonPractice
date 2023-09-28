import json
import sqlite3 

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;
                  
CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE           
);

CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
)
                  
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

str_data = open(fname).read()
json_data = json.loads(str_data)

iteration = 0
for entry in json_data:

    name = entry[0]
    title = entry[1]
    role = entry[2]

    print((name, title, role))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES (?)''', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES (?)''', (title, ))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ?)''', 
        ( user_id, course_id, role))

    # force a write operation to the database file after every 20 entries
    iteration += 1
    if iteration == 20:
        conn.commit()
        iteration = 0

    # display each entry after being inserted
    print(name, title, role)

conn.commit()

# test command #1
method1 = '''
    SELECT User.name, Course.title, Member.role
    FROM User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2'''
testMethod(method1, 1)

# test command #2
method2 = '''
    SELECT 'XYZZY' || HEX( User.name || Course.title || Member.role ) AS X
    FROM User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1'''
testMethod(method2, 2)

# close connection to the database
conn.close()