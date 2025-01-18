import pytest

from dsa.hash_tables.open_addressing import HashTable


@pytest.fixture
def hash_table():
    return HashTable()


def test_set_and_get_single_item(hash_table):
    hash_table.set("key1", "value1")
    assert hash_table.get("key1") == "value1"


def test_get_nonexistent_key(hash_table):
    assert hash_table.get("nonexistent") is None
    assert hash_table.get("nonexistent", "default") == "default"


def test_update_existing_key(hash_table):
    hash_table.set("key1", "value1")
    hash_table.set("key1", "updated_value")
    assert hash_table.get("key1") == "updated_value"


def test_remove_existing_key(hash_table):
    hash_table.set("key1", "value1")
    hash_table.remove("key1")
    assert hash_table.get("key1") is None


def test_remove_nonexistent_key(hash_table):
    try:
        hash_table.remove("nonexistent")
    except Exception as e:
        pytest.fail(f"Unexpected error occurred: {e}")


def test_collision_handling(hash_table):
    # Force collision by using two keys with same hash (mock if needed)
    key1, key2 = "key1", "key2"
    hash_table.set(key1, "value1")
    hash_table.set(key2, "value2")
    assert hash_table.get(key1) == "value1"
    assert hash_table.get(key2) == "value2"


def test_resize_operation(hash_table):
    # Insert enough items to trigger resize
    for i in range(70):  # Above the load threshold
        hash_table.set(f"key{i}", f"value{i}")

    for i in range(70):
        assert hash_table.get(f"key{i}") == f"value{i}"

    assert hash_table.length > 100  # Confirm resize occurred


def test_tombstone_reuse(hash_table):
    hash_table.set("key1", "value1")
    hash_table.remove("key1")
    hash_table.set("key2", "value2")  # Should reuse tombstone spot
    assert hash_table.get("key1") is None
    assert hash_table.get("key2") == "value2"


def test_multiple_data_types(hash_table):
    hash_table.set(42, "integer key")
    hash_table.set((1, 2), "tuple key")
    hash_table.set(3.14, "float key")

    assert hash_table.get(42) == "integer key"
    assert hash_table.get((1, 2)) == "tuple key"
    assert hash_table.get(3.14) == "float key"


def test_overwrite_after_resize(hash_table):
    for i in range(70):
        hash_table.set(f"key{i}", f"value{i}")
    hash_table.set("key1", "new_value1")
    assert hash_table.get("key1") == "new_value1"
