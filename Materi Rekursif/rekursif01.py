def hello_world(n):
    if n == 0:
        return
    else:
        print("Hello world!")
        hello_world(n - 1)


hello_world(5)