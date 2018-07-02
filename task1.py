def parity_function(value):
    if value % 2 == 0:
        print("Even")
    else:
        print("Odd")


for i in range(10):
    parity_function(i)
