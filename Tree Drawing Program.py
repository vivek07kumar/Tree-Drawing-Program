done = True
print()
print('               >>>>>>>>>>>>>>> Tree Drawing Program <<<<<<<<<<<<<<<')
print()
print()
while done :
    done2 = True
    done3 = True
    while done2 :
        hight = int(input('>> Please enter a number to draw Tree of that hight : '))
        if hight <= 1 :
            print()
            print('                              >>>> WRONG INPUT ! <<<<')
            print('                       Please enter a number greater than 1.')
            print()
        else :
            done2 = False
    print()
    print('* ANSWER --> Below is the tree of',hight,'lines of hight :')
    print()
    number = 1
    repeat = 1
    space = hight - 1
    while repeat <= hight :
        print(' ' * space,end='')
        print('*' * number)
        number = number + 2
        repeat = repeat + 1
        space = space - 1
    space = hight - 1
    print(' ' * space,'|',sep='')
    print(' ' * space,'|',sep='')
    print('-----------------------------------------------------------------------')
    while done3 :
        print()
        userinput = input('>> Press C to Continue or Press E to Exit : ')
        if userinput == 'c' or userinput == 'C' :
            done3 = False
            print()
        elif userinput == 'e' or userinput == 'E' :
            done3 = False
            done = False
        else :
            print()
            print('                              >>>> WRONG INPUT ! <<<<')
