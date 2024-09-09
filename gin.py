def f():
    a = 1
    def g(): # g is a variable on f's stack frame
        # by defining g in f,
        # g needs to capture f's current stack frame, but the stack frame is mutable, so if a changes later, 
        # a in g will also change
        # nonlocal a states that the a used in g is not the a in g
        # stack frame is an object (meaning that something else may hold the address of this stack frame)
        return a
    a = 2
    return g # when returning f,
            # the ref cnt of f's stack frame -= 1,
            # but g is not called so not returned, so g is holding f's stack frame
            # so a is not eliminated
            # what returned will hold g,
            

print(f) # what returned is not kept, cuz it hasn't been assigned
print(f())
print(f()())


def _():
    def even(n):
        return n == 0 or odd(n - 1)
    def odd(n):
        return not n == 0 and even(n - 1)
    return even, odd

for i in range(10):
    print(_()[0](i))

# under mutual recursion, f and g just capture the stack frame, they do not capture the variables in the stack frame
# thus, they can refer to the same variables, and triumph the mutual recursion
# python vm just parse the function body upon definition, without knowing what the variables inside the function
# python only knows what's inside the function when called.
