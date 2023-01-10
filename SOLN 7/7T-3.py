def foo_moo (x):
    if x%2 == 0 and x%3 == 0:
        return "FooMoo"
    elif x%2 == 0:
        return "Foo"
    elif x%3 == 0:
        return "Moo"
    else:
        return "Boo"

#function call
print(foo_moo(5))
print(foo_moo(6))
print(foo_moo(4))