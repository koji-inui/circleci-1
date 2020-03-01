#!/usr/bin/python
# -*- coding: utf-8 -*-
from sample import add1

class TestClass(object):
    def test_add1(self):
        ans = add1(1,2)
        expected = 3
        assert ans==expected
