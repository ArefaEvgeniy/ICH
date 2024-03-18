def outer_function():
    x = 1

    def inner_function():
        # global x
        nonlocal x
        x = 2
        print('local-local x:', x)

    inner_function()
    print('local x:', x)


x = 0
outer_function()
print('x:', x)
