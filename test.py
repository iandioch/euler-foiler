import unittest
import parse

class TestParse(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(parse.parse('tests/iandioch.png'), '128')
        self.assertEqual(parse.parse('tests/michcioperz.png'), '25')

if __name__ == '__main__':
    unittest.main()
