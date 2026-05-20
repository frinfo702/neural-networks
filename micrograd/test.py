from engine import Value


def test():
    a = Value(2.0)
    b = Value(-3.0)
    expected = Value(-1.0)
    assert expected.data == a.data + b.data  # python call internally a.__add__(b)

    print("__add__: computed successfully")

    expected = Value(-6.0)
    assert expected.data == a.data * b.data

    print("__mul__: computed successfully")

    c = a + b
    expected = {
        a,
        b,
    }  # don't use {Value(2.0), Value(-3.0)} otherwise this fails because of allocatin diffrent meomry address
    assert c._prev == expected
    print("__add__: chiledren value computed successfully")

    c = a * b
    expected = {a, b}
    assert c._prev == expected
    print("__mul__: chiledren value computed successfully")

    a = Value(3.0, label="a")
    b = a + a
    b.backward()
    assert a.grad == 2.0
    print("__add__: correctly computed children's grad")

    a = Value(-2.0, label="a")
    b = Value(3.0, label="b")
    d = a * b
    d.label = "d"
    e = a + b
    d.label = "e"
    f = d * e
    f.label = "f"
    f.backward()
    assert a.grad == -3.0
    assert b.grad == -8.0
    print("having multiple prev: correctly computed children's grad")
