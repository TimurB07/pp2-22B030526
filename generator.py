def count_gen(n):
    for i in range(n, -1, -1):
        yield i
n = int(input())
cnt = count_gen(n)
for i in cnt:
    print(i)