def insertion_sort(List):
    for i in range(1, len(List)):
        for j in range(i, 0, -1):
            if List[j] < List[j-1]:
                List[j], List[j-1] = List[j-1], List[j]
    return List

List = [4,3,5,8,7]
print(insertion_sort(List))
[3,4,2,8,7]