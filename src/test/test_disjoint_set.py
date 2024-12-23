from dsa.disjoint_set import DisjointSet


def test_ds_union_find():
    elements = set(["A", "B", "C", "D"])
    ds = DisjointSet(elements)
    ds.union("A", "B")
    ds.union("B", "C")
    assert ds.find("A") == ds.find("B")
    assert ds.find("B") == ds.find("C")
    assert ds.find("A") == ds.find("C")
    assert ds.find("A") == ds.find("A")
    assert ds.find("B") == ds.find("B")
    assert ds.find("C") == ds.find("C")
    assert ds.find("A") != ds.find("D")
