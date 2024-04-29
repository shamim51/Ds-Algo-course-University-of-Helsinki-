def count(a, b, c):

    if a>b:
        min = b
    else:
        min = a

    result = int(c / min)
    return result

if __name__ == "__main__":
    print(count(3, 4, 11)) # 3
    print(count(5, 1, 100)) # 100
    print(count(2, 3, 1)) # 0
    print(count(2, 3, 9)) # 4