#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# --------------------------------------
# projects/python/collatz/TestCollatz.py
# Copyright (C) 2017
# Glenn P. Downing
# --------------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, get_cycle_length, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5 (self) :
        v = collatz_eval(500, 1500)
        self.assertEqual(v, 182)

    def test_eval_long_range (self) :
        v = collatz_eval(1, 1000000)
        self.assertEqual(v, 525)

    def test_eval_invalid_params_1 (self) :
        self.assertRaises(ValueError, lambda: collatz_eval(-1, 5))

    # -----
    # get_cycle_length
    # -----
    def test_get_cycle_length_1(self):
        v = get_cycle_length(1)
        self.assertEqual(v, 1)

    def test_get_cycle_length_2(self):
        v = get_cycle_length(10)
        self.assertEqual(v, 7)

    def test_get_cycle_length_3(self):
        v = get_cycle_length(100)
        self.assertEqual(v, 26)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

if __name__ == "__main__" : #pragma: no cover
    main()
