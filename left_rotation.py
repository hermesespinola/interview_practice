def array_left_rotation(a, n, k):
    return[a[i % n] for i in range(k, n + k)]

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
