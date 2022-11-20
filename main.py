def printer(a):
    if a == '2':
        print('This is second version')
    elif a == 'BOB':
        print('CAM TЫ BOB xDD')
    else:
        print("I don't know what is this version")


if __name__ == '__main__':
    a = input('Введите 2 либо BOB: ')
    printer(a)