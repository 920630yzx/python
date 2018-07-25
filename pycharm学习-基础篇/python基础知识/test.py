a=[1,2,3]
def run(n):
    for i in n:
        print(i)
        if i<3:
            return 'yes'

r=run(a)
print(r)