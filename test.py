a = 1

def move():
    global a
    a += 1


if __name__ == '__main__':
    print(a)
    a += 1
    print(a)
    move()
    print(a)
