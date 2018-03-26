def bubble_sort(List):
    for t in range(len(List)-1, 0, -1):
        for i in range(t):
            if List[i] > List[i+1]:
                List[i], List[i+1] = List[i+1], List[i]
    print(List)

if __name__ == "__main__":
    List = input("Please type in your list: ").split(",")
    List = [int(a) for a in List]
    print(List)
    bubble_sort(List)            

   