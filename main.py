# Generator expressions must be parenthesized if not sole argument

def example(gen, num):
    print(gen)
    print(num)


example((num for num in range(3)), 10)