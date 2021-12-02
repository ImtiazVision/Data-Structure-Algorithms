def fib(n):
    # The first and second values will always be fixed
    first = 0
    second = 1

    if n < 1:
        return -1

    if n == 1:
        return first

    if n == 2:
        return second

    count = 3  # Starting from 3 because we already know the first two values
    while count <= n:
        fib_n = first + second # we are adding first and 2nd 
        first = second # here we are setting 2nd to first
        second = fib_n # here we are appointing addition of 1st and 2nd into 2nd
        count += 1  # Increment count in each iteration
    return fib_n


n = 7
print(fib(n))
