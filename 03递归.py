def countdown(i):
    print(str(i)+"...")
    if i <= 0:
        return
    else:
        countdown(i-1)

countdown(5)