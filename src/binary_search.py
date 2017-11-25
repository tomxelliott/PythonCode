import sys

def binary_search(data, target, low, high):
    if target > high:
        print "too big dude!"
    elif target < low:
        print "too small dude! ;p"
    elif not isinstance(target, int):
        print "the target we are searching for must be a number!"
    else:
        if low > high:
            return False
        else:
            mid = (low+high)//2
            if target == mid:
                return True
            elif target < data[mid]:
                return binary_search(data, target, low, mid-1)
            else:
                return binary_search(data, target, mid+1, high)

def main():
    try:
        x = []
        i = 0
        while i < 20:
            try:
                j = int(input())
                if j < 0 or not isinstance(j, int):
                    raise ValueError
                x.append(j)
                i += 1
            except ValueError:
                print "Please enter a positive number."

        x.sort()
        print x
        print ""
        print "Please enter a number you would like to search..."
        user_input = input()
        print binary_search(x, user_input, x[0], x[-1])
    except KeyboardInterrupt:
        sys.exit()

if __name__=='__main__':
    main()

