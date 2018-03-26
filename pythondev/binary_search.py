#非递归实现
def binary_search(List, item):
    first = 0
    last = len(List)-1
    while first <= last:
        midpoint = int((first + last)/2)
        if List[midpoint] == item:
            return True
        elif item < List[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return False


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42] 
print(binary_search(testlist, 3)) 
print(binary_search(testlist,13))