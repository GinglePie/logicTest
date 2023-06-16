
def main():
    
    while 1:
        n = int(input("Enter the length of Prime number: "))
        if n < 1:
            print("Please insert number that greater than or equal to 1.")
        else:
            break

    primeList = [2, 3]
    if n == 1:
        print(primeList[0])
    elif n == 2:
        print(*primeList, sep=", ")
    else:
        p = 3
        n -= 2
        while n:
            p += 2
            isPrime = True
            for i in primeList:
                if p%i == 0:
                    isPrime = False
                    break
                if i > p/i:
                    break
   
            if isPrime:
                primeList.append(p)
                n -= 1

        print(*primeList, sep=", ")


if __name__ == "__main__":
    main()