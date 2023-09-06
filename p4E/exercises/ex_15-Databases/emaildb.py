import sqlite3

#connection to sqlite
conn = sqlite3.connect('emaildb.sqlite')
#creating a handle for sql
cur = conn.cursor()

#drops the table if it exists, in order to run this code over and over again
cur.execute('DROP TABLE IF EXISTS Counts')

#creating a table Counts, columns email and count
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

#opening a file
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    #picking lines that only starts with From
    if not line.startswith('From: '): continue
    pieces = line.split()
    #picking only email addresses from the lines that start with from
    email = pieces[1]
    #doesnt retrieve email but makes another connection to the db, ensures tables are right
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    #fetches the first email
    row = cur.fetchone()
    if row is None:
        #if the row is empty it inserts the email into the row
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        #otherwise if the row has emails, it updates the rows
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
        (email,))
    #commits connection, I presume its like the git commit
    conn.commit()

#selects emails from the Count Table ordered by count in a descending order
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

#loop through the selection and prints them out.
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

#closes the count
cur.close()
