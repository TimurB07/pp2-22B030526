def div_gen(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
numb = div_gen(n)
for number in numb:
    print(number)