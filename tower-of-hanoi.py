def toh(n, origin, buffer, destination):
    if n == 1:
        print(origin,'->',destination)
        return
    toh(n-1, origin, destination, buffer)
    print(origin,'->',destination)
    toh(n-1, buffer, origin, destination)
n = int(input())
toh(n, 'A', 'B', 'C')
