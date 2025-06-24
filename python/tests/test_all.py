import pytest
import uuid_blake3


def test_sum_as_string():
    assert uuid_blake3.sum_as_string(1, 1) == "2"
    assert uuid_blake3.sum_as_string(1, 2) == "3"
