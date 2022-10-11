#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ret = 0
    for i in range(x):
        print("{}".format(my_list[i]), end="")
        ret += 1
    except (TypeError,ValueError,IndexError):
        break
    print("")
    return(ret)
