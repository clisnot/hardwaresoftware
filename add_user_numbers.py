Var = 42

def ask_me():
     num = int(input ("Enter number:"))
     return(num)

def add_global(num)

    Var = Var + num
    return(Var)

def main():
    global Var
    number1 = ask_me()
    number2 = ask_me()
    sum +- add_global(number1)
    sum =- add_global(number2)
    sum += add_global(Var)
    print("Sum:" sum)
    print("Global:", Var)


if __name__ == '__main__':
    main()
