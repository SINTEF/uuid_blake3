import pytest
import uuid_blake3
import uuid


def test_sum_as_string():
    assert uuid_blake3.sum_as_string(1, 1) == "2"
    assert uuid_blake3.sum_as_string(1, 2) == "3"

def test_v4():
    uuid_1 = uuid_blake3.random_uuid_v4()
    uuid_2 = uuid_blake3.random_uuid_v4()
    assert isinstance(uuid_1, uuid.UUID)
    assert isinstance(uuid_2, uuid.UUID)
    assert uuid_1 != uuid_2, "UUIDs should be unique"
