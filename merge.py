t = int(input())

for i in range(t):
    N = list(map(int, input().split()))
    M = list(map(int, input().split()))

    temp = []
    N.reverse()
    M.reverse()

    #print(*N)
    #print(*M)
    while not(len(N)== 0 or len(M) == 0):
        if N[-1] > M[-1]:
            M.pop()
            temp.append(2)
        elif N[-1] < M[-1]:
            N.pop()
            temp.append(1)
    if len(N) != 0 :
        for i in range(len(N)):
            N.pop()
            temp.append(1)
    elif len(M) != 0 :
        for k in range(len(M)):
            M.pop()
            temp.append(2)

    print(*temp)



