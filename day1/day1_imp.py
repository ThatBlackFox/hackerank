if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        opt = input().split()
        n = len(opt)
        eval(f"""{f"arr.{opt[0]}({f'{opt[1]},{opt[2]}' if n==3 else opt[1]})" if n>1 else "print(arr)" if 'print' in opt else f"arr.{opt[0]}()"}""")
        
