def primo(x):
    d = x-1
    while (x%d !=0):
        d = d-1

    #return d==1

    if (d==1):
        return True
    else:
        return False


x = int(input())
if(primo(x)):
    print("{:d} é primo".format(x))
else:
    print("{:d} não é primo".format(x))

