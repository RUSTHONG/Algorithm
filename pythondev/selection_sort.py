def selection_sort(List):
    for i in range(len(List)-1):
        min_pos = i
        for j in range(i+1, len(List)):
            if List[min_pos] > List[j]:
                min_pos = j
        if min_pos != i:
            List[i], List[min_pos] = List[min_pos], List[i]
    print(List)

        
List = [2, 5, 56, 12, 1, 24]
selection_sort(List)