#!/usr/bin/env python3

# lib/ipdb_debugging.py
import ipdb

def plus_two(num):
    num = num + 2
    return num

# lib/testing/ipdb_debugging_test.py
import pytest
from ipdb_debugging import plus_two

class TestIpdbDebugging:
    def test_adds_two(self):
        assert(plus_two(3) == 5)
