

def greeting():
    name = input("Input your name")
    print("You are the best", name)


def count_in_list(ls, to_count):
    counter = 0
    for e in ls:
        if e == to_count:
            counter += 1
    return counter