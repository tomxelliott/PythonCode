import sys

def binary_search(target, low, high):
    if target > high:
        print "too big dude!"
    elif target < low:
        print "too small dude! ;p"
    else:
        if low > high:
            return False
        else:
            mid = (low+high)//2
            if target == mid:
                return True
            elif target < mid:
                return binary_search(target, low, mid-1)
            else:
                return binary_search(target, mid+1, high)

def main():
    try:
        print "Please enter a low value: "
        lower = int(input())

        print "Please enter a high value: "
        higher = int(input())

        if lower and higher:
            print "Please enter a number you would like to search..."
            user_input = int(input())
            print binary_search(user_input, lower, higher)
        else:
            print "Please try again..."
    except ValueError:
        print "Please enter a positive number."
    except NameError:
        print "Please enter a valid number, not any other type!"
    except SyntaxError:
        print "Please enter a valid number!!!"
    except UnboundLocalError:
        print "Low value and High value not entered correctly!"
    except KeyboardInterrupt:
        sys.exit()

if __name__=='__main__':
    main()
