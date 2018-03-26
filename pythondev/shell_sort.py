def shell_sort(List):
    n = len(List)
    gap = int(n/2)
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and List[j-gap] > List[j]:
                List[j-gap], List[j] = List[j], List[j-gap]
                j -= gap
        if type(gap/2) == int:
            gap = gap/2
        else: 
            gap = int(gap/2)

List = [54,26,93,17,77,31,44,55,67]
shell_sort(List)
print(List)