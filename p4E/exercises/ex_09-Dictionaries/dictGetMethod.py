counts = {'chuck':1, 'annie':42, 'jan':100}
#get method takes a default value as parameter, if key appears in dict, it returns the value,
#otherwise, it returns the default value.
print(counts.get('jan',0))
print(counts.get('tim',0))