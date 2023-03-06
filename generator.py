def even_gen(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input(" "))
even = even_gen(n)
result = ", ".join(str(number) for number in even)
print("{}:{}".format(n, result))