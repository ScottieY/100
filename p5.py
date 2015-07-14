ls = [2,3,4,5,6,7,8,9]
def foo(stack,list):
    equation = ''.join(str(x) for x in stack) 
    if len(list) == 0:
        if eval(equation) == 100:
            print equation
    else:
        foo(stack + ['+'] + list[0:1],list[1:])
        foo(stack + ['-'] + list[0:1],list[1:])
        foo(stack + list[0:1],list[1:])

foo([1],ls)
