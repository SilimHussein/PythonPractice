counts = {'chuck':1, 'annie':42, 'jan':100}
for key in counts:
    #print(key, counts[key])
    #if we want to find all entries with value above 10
    if counts[key] > 10:
        print(key, counts[key])
