from dsa.arrays import StaticArray, DynamicArray


def test_static_array_size():
    a = StaticArray(5)
    assert a.size() == 5


def test_static_array_clear():
    a = StaticArray(3)
    a.array[0] = 1
    a.array[1] = 2
    a.array[2] = 3
    a.clear()
    assert a.array[0] == None
    assert a.array[1] == None
    assert a.array[2] == None

def test_static_array_get():
    a = StaticArray(5)
    a.array[0] = 1
    a.array[2] = 2
    a.array[4] = 3
    assert a.get(0) == 1
    assert a.get(1) == None
    assert a.get(2) == 2
    assert a.get(4) == 3

def test_static_array_set():
    a = StaticArray(5)
    a.array[0] = 1
    a.array[2] = 2
    a.array[4] = 3
    a.set(0, 4)
    a.set(1, 5)
    a.set(2, 6)
    a.set(4, 7)
    assert a.get(0) == 4
    assert a.get(1) == 5
    assert a.get(2) == 6
    assert a.get(3) == None
    assert a.get(4) == 7


def test_static_array_contains():
    a = StaticArray(5)
    a.array[0] = 1
    a.array[2] = 2
    a.array[4] = 3
    assert a.contains(2) == True
    assert a.contains(4) == False


def test_dynamic_array_size():
    a = DynamicArray(5)
    assert a.size() == 5


def test_dynamic_array_clear():
    a = DynamicArray(3)
    a.set(0, 1)
    a.set(1, 2)
    a.set(2, 3)
    a.clear()
    assert a.get(0) == None
    assert a.get(1) == None
    assert a.get(2) == None


def test_dynamic_array_get():
    a = DynamicArray(3)
    a.set(0, 1)
    a.set(1, 2)
    a.set(2, 3)
    assert a.get(0) == 1
    assert a.get(1) == 2
    assert a.get(2) == 3



def test_dynamic_array_set():
    a = DynamicArray(3)
    a.set(0, 1)
    a.set(2, 3)
    assert a.get(0) == 1
    assert a.get(1) == None
    assert a.get(2) == 3


def test_dynamic_array_contains():
    a = DynamicArray(3)
    a.set(0, 1)
    a.set(1, 2)
    a.set(2, 3)
    assert a.contains(2) == True
    assert a.contains(4) == False


def test_dynamic_array_insert():
    a = DynamicArray(3)
    a.set(0, 1)
    a.set(1, 2)
    a.set(2, 3)
    a.insert(4)
    assert a.get(0) == 4
    assert a.get(3) == 3


def test_dynamic_array_append():
    a = DynamicArray(3)
    a.set(0, 1)
    a.set(1, 2)
    a.set(2, 3)
    a.append(4)
    assert a.get(0) == 1
    assert a.get(3) == 4


def test_dynamic_array_delete():
    a = DynamicArray(3)
    a.set(0, 1)
    a.set(1, 2)
    a.set(2, 3)
    a.delete(1)
    assert a.get(0) == 1
    assert a.get(1) == 3

