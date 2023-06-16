
def main():

    while 1:
        pin = input("Enter pincode: ")
        error = ""
        for i in pin:
            if i < '0' or i > '9':
                error = "Please enter only 0-9 number"
                break
        if len(error) > 0:
            print(error)
            continue
        
        if len(pin) < 6:
            print("Don't use pincode fewer than 6 numbers")
            continue

        temp = pin
        pin = []
        for i in temp:
            pin.append(int(i))

        countSame = 0
        for i in range(len(pin)-1):
            if pin[i] == pin[i+1]:
                countSame += 1
                if countSame > 1:
                    error = "Don't use triple number."
                    break
            else:
                countSame = 0

        if len(error) > 0:
            print(error)
            continue

        countGroup = 0
        for i in range(len(pin)-1):
            if pin[i] == pin[i+1]:
                countGroup += 1
                if countGroup > 2:
                    error = "Don't use double number more than 2 groups."
                    break
                
        if len(error) > 0:
            print(error)
            continue
        
        for i in range(len(pin)-2):
            if abs(pin[i] - pin[i+2]) == pin[i+1] and abs(pin[i] - pin[i+1]) == 1:
                error = "Don't use number in ascending or decending order more than 2 numbers."
                break
        
        if len(error) > 0:
            print(error)
            continue
        else:
            print("Success.")
            break


if __name__ == "__main__":
    main()