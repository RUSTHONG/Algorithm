def rec(n):
    if n == 1:
        return 1
    return n+rec(n-1)  


if __name__ == "__main__":
    n = int(input("Please type in a number: "))
    print(rec(n))