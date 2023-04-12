while True:
    try:
        s = str(input())
        print(s)
    except EOFError:
        break