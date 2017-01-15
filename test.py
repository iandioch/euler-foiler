import unittest
import parse

class TestParse(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(parse.parse('test.png'), '128')

if __name__ == '__main__':
    unittest.main()
