import unittest


class TestUM(unittest.TestCase):

    def test_leap(self):
        res = totest.is_leap(2016)
        self.assertTrue(res, True)


if __name__ == '__main__':
    import totest
    unittest.main()
