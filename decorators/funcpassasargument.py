def func(f):
    print(f())

def myfunc():
    return 'I am inside myfunc'
func(myfunc)