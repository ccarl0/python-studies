# finding the number the requires the most number of loops
def x3plus1_loops(n):
    i = 0
    while True:
        i += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        if n == 1:
            break
    return i


n = 0
n_loop = 0
number_most_loop = 0
while True:
    n += 1
    new_n_loop = x3plus1_loops(n)
    if new_n_loop > n_loop:
        n_loop = new_n_loop
        number_most_loop = n
        print(f"{n} requires {n_loop} loops;")
