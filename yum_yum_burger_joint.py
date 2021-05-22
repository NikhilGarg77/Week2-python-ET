def menu():
    print("1.yum yum burger")
    print("2.grease yum fries")
    print("3.soda yum")
    print("4.close")
    i = True
    j = 0
    k = 0
    l = 0
    total = 0
    while i:
        item = int(input("enter no. of items you want"))
        if item == 1:
            nob = int(input("how many burgers?"))
            j = j + nob
            total = total + (nob * 0.99)
            i = True
        elif item == 2:
            nof = int(input('how many fries?'))
            k = k + nof
            total = total + (nof * 0.79)
            i = True
        elif item == 3:
            nos = int(input('how many sodas?'))
            l = l + nos
            total = total = (nos * 1.09)
            i = True

        else:
            i = False
    total = total + (0.06 * total)
    print('\n Your Receipt:')
    print('yum yum burger are ' + str(j) + 'which cost' + str(j * 0.99))
    print('grease yum fries are ' + str(k) + 'which cost' + str(k * 0.79))
    print('soda yum are ' + str(l) + 'which cost' + str(l * 1.09))
    print('total payable amount after 6% tax is ' + str(total))


menu()
