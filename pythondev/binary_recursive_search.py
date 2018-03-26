def binary_recursive_search(List, item):
    if len(List) == 0:
        return False
    else:
        midpoint = int(len(List)/2)
        if List[midpoint]==item:
            return True
        else:
            if item < List[midpoint]:
                return binary_recursive_search(List[:midpoint], item)
            else:
                return binary_recursive_search(List[midpoint+1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_recursive_search(testlist, 3))
print(binary_recursive_search(testlist, 13))