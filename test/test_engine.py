from micrograd.engine import Value


def test_add():
    a, b = Value(2.0), Value(-3.0)
    c = a + b
    assert c.data == -1.0
    assert c._prev == {a, b}


def test_mul():
    a, b = Value(2.0), Value(-3.0)
    c = a * b
    assert c.data == -6.0
    assert c._prev == {a, b}


def test_div():
    a = Value(-4.0)
    b = Value(2.0)
    c = a / b
    assert c.data == -2.0


def test_backward_same_element():
    a = Value(3.0)
    b = a + a
    b.backward()
    assert a.grad == 2.0


def test_backward_multiple_chain():
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
