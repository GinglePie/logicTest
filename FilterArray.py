
def main():
    listA = [-9, 0, 7, 1, 5]
    listB = [-1, 0, 1]
    # n = -1
    # while 1:
    #     n = int(input("Enter the length of Fibonacci: "))
    #     if n < 1:
    #         print("Please insert number that greater than or equal to 1.")
    #     else:
    #         break
        
    listC = []
    for i in listA:
        for j in listB:
            if i == j:
                listC.append(i)
    print(*listC, sep=", ")


if __name__ == "__main__":
    main()