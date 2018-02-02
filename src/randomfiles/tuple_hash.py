if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = ()
    for i in integer_list:
        t = t + (i,)
    x = hash(t)
    print x
