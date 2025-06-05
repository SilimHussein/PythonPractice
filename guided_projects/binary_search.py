# Proving that binary search is faster than naive search
# Naive search : scan the entire list and ask if its equal ot the target.
# if yes, return the index, if no, return -1
import random
import time

def naive_search(l, target):
    # Example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i 
    return -1

# Binary search uses divide and conquer
# We leverage the fact that our list is SORTED 
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1 

    # Example l = [1, 3, 5, 10, 12] 
    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)

if __name__=='__main__':
 '''l =[1, 2, 5, 10, 12]
    target = 10
    print(naive_search(l, target))
    print(binary_search(l, target))
'''
    length = 10000
    my_binary_list = set()
    while len(my_binary_list) < length:
        my_binary_list.add(random.randint(-3*length, 3*length))
    my_binary_list= sorted(list(my_binary_list))

    start = time.time()
    for target in my_binary_list:
        naive_search(my_binary_list, target)
    end = time.time()
    print("Naive search time: ", (end - start)/length, "seconds")

    start = time.time()
    for target in my_binary_list:
        binary_search(my_binary_list, target)
    end = time.time()
    print("Binary search time: ", (end - start)/length, "seconds")