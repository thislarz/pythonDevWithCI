import unittest


class TestUtil(unittest.TestCase):

    def test_foo(self):
        test_cases = [(
            "foo",
            "bar",
            "foo is unexpectedly equal to bar"
        )]

        for test_value, expected_value, msg in test_cases:
            self.assertNotEqual(test_value, expected_value, msg)


if __name__ == '__main__':
    unittest.main()