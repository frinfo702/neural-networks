from engine import Value


def test():
    a = Value(2.0)
    b = Value(-3.0)
    expected = Value(-1.0)
    assert expected.data == a.data + b.data  # python call internally a.__add__(b)

    print("__add__: passed")

    expected = Value(-6.0)
    assert expected.data == a.data * b.data

    print("__mul__: passed")
