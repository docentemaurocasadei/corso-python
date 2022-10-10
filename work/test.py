x = 10
def myf(v, *args, **kwargs):
    y = 5
    x = 9
    print("x è {}".format(x))
    def myf2():
        print("y è {}".format(y))
        print(v, args, kwargs)
    myf2()

myf('aa', 'bb', 'cc', miav=1)
print(x)