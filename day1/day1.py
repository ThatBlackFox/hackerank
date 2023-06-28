if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        opt = input().split()
        opt = [int(opt[i]) if i>0 else opt[i] for i in range(len(opt))]
        if "insert" in opt:
            arr.insert(int(opt[1]),opt[2])
        elif "print" in opt:
            print(arr)
        elif "remove" in opt:
            arr.remove(opt[1])
        elif "append" in opt:
            arr.append(opt[1])
        elif "sort" in opt:
            arr.sort()
        elif "pop" in opt:
            arr.pop()
        elif "reverse" in opt:
            arr.reverse()