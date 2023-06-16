
def main():
    fiboList = [0, 1]

    while 1:
        n = int(input("Enter the length of Fibonacci: "))
        if n < 1:
            print("Please insert number that greater than or equal to 1.")
        else:
            break

    if n == 1:
        print(fiboList[0])
    elif n == 2:
        print(*fiboList, sep=", ")
    else:
        for i in range(1, n-1):
            fiboList.append(fiboList[i-1]+fiboList[i])
        print(*fiboList, sep=", ")


if __name__ == "__main__":
    main()