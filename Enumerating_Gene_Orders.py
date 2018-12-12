n = 7


def factorial(n):
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1


def print_list(arglist):
    text = ""
    for i in range(len(arglist)):
        text = text + str(arglist[i]) + " "
    text = text.rstrip()
    print(text)


def sub_fun(index, oldlist, newlist):
    if not oldlist:
        print_list(newlist)
        return
    else:
        for i in range(len(oldlist)):
            passed_newlist = newlist + [oldlist[i]]
            passed_oldlist = oldlist[0:i] + oldlist[i + 1:len(oldlist)]
            sub_fun(i, passed_oldlist, passed_newlist)


original_list = []
new_list = []

for i in range(n):
    original_list.append(i + 1)

print(factorial(n))

sub_fun(n, original_list, new_list)
