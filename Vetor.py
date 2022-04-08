x = int(input())
n= list()


for i in range (10):
    n.append(x)
    x = x * 2
    print(f'N[{i}] ='.format(i), n[i])