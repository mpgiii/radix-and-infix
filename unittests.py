from infix import *
from radix import *
import unittest


class TestTicTacToe(unittest.TestCase):
    def test_infix_1(self):
        s = '( 9 + 2 + 3 + 4 * 5 + ( 2 / 1 / 34 ) )'
        mine = eval_infix(s)
        pythons = float(eval(s))
        self.assertEqual(mine, pythons)

    def test_infix_2(self):
        s = "1.7 + 2.8 * 3.6 / ( 0 - 9.4 ) + 5 / ( 0.36 - 7.7 ) / 9.12 * 11"
        mine = eval_infix(s)
        pythons = float(eval(s))
        self.assertEqual(mine, pythons)

    def test_radix_1(self):
        unsortedlst = ['b', 'a', 'c', 'e', 'd', 'f']
        sortedlst = radixsort(unsortedlst, len(unsortedlst))
        self.assertListEqual(sortedlst, ['a', 'b', 'c', 'd', 'e', 'f'])

    def test_radix_2(self):
        unsortedlst = ['ppp', 'bac', 'eaf', 'aac', 'aab']
        sortedlst = radixsort(unsortedlst, len(unsortedlst))
        self.assertListEqual(sortedlst, ['aab', 'aac', 'bac', 'eaf', 'ppp'])


if __name__ == '__main__':
    unittest.main()