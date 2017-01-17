import unittest
import parse
from PIL import Image

class TestParse(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(parse.parse(parse.open_image('tests/iandioch.png')), '128')
        self.assertEqual(parse.parse(parse.open_image('tests/michcioperz.png')), '25')

if __name__ == '__main__':
    unittest.main()
