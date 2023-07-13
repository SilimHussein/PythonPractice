s = 'spam'
#using list function to convert a string into individual letters
t = list(s)
print(t)
s1 = 'pinning for the fjords'
#using method split to convert a string into words
t1 = s1.split()
print(t1)
#printing with optional argument delimiter to specify boundaries
s2 = 'monty-python-flying-circus'
delimiter = '-'
t2 = s2.split(delimiter)
print(t2)
#join is the inverse of split, concatenates elements of a list into a string
t3 = ['pining','for','the','fjords']
delimiter = ' '
s3 = delimiter.join(t3)
print(s3)