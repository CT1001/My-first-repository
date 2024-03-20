
# def show():
#     i=10
#     while i>=2:
#         yield i
#         i-=1
# for i in show():
#     print(i)        
def p(num):
    while num>=2:
        if num%2==0:
            yield num**2
        elif num%3==0:
            yield num**3
        elif num%5==0:
            yield num**5
        else:
            yield num        
        num=num-1
for num in p(40):
    print(num)
l=list(p(40))
print(l)                