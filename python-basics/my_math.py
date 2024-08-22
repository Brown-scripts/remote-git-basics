def calculate(a,b,c):
    if a =='add':
        return(b+c)
    elif a== 'subtract':
        return(b-c)
    elif a== 'divide':
        return(b/c)
    elif a== 'multiply':
        return(b*c)
    else:
        print('Operation can not be identified')



answer=calculate('divide', 7, 3)
print(answer)