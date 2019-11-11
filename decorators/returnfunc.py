def welcome():
    print('i am inside the welcome')
    def hello():
        print('I am inside the hello')
    return  hello
result=welcome()
result()