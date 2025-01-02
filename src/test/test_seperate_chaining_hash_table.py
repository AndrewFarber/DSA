from unittest.mock import patch
from dsa.hash_tables.separate_chaining import HashTable


def test_insert_and_get():
    ht = HashTable()
    ht.set("key1", "value1")
    ht.set("key2", "value2")
    ht.set("key3", "value3")

    assert ht.get("key1") == "value1"
    assert ht.get("key2") == "value2"
    assert ht.get("key3") == "value3"
    assert ht.get("nonexistent") is None


def test_update_value():
    ht = HashTable()
    ht.set("key1", "value1")
    ht.set("key1", "new_value1")

    assert ht.get("key1") == "new_value1"


def test_remove_key():
    ht = HashTable()
    ht.set("key1", "value1")
    ht.set("key2", "value2")
    ht.set("key3", "value3")

    assert ht.get("key2") == "value2"
    ht.remove("key2")
    assert ht.get("key2") is None
    assert ht.get("key1") == "value1"
    assert ht.get("key3") == "value3"


def test_resize():
    ht = HashTable()
    initial_capacity = len(ht.lst)
    for i in range(200):
        ht.set(f"key{i}", f"value{i}")

    resized_capacity = len(ht.lst)
    print("Size", ht.length)
    assert resized_capacity > initial_capacity
    for i in range(200):
        assert ht.get(f"key{i}") == f"value{i}"


@patch("dsa.hash_tables.separate_chaining.hash")
def test_collision_handling(mock_hash):
    mock_hash.return_value = 1

    ht = HashTable()
    ht.set(1, "value1")
    ht.set(101, "value101")
    ht.set(201, "value201")

    assert ht.get(1) == "value1"
    assert ht.get(101) == "value101"
    assert ht.get(201) == "value201"
    assert ht.lst[1] is not None
    assert ht.lst[1].hash == 1


def test_empty_table():
    ht = HashTable()
    assert ht.get("nonexistent") is None
    ht.set("key1", "value1")
    assert ht.get("key1") == "value1"


def test_multiple_removals():
    ht = HashTable()
    ht.set("key1", "value1")
    ht.set("key2", "value2")
    ht.set("key3", "value3")

    ht.remove("key1")
    assert ht.get("key1") is None
    ht.remove("key2")
    assert ht.get("key2") is None
    assert ht.get("key3") == "value3"


def test_default_value():
    ht = HashTable()
    assert ht.get("nonexistent", default="default_value") == "default_value"
