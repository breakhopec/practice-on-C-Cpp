#coding=utf-8
import name_function
import unittest

class NameTest(unittest.TestCase):

    def test_name_function(self):
        formatted = name_function.get_formatted_name('steve', 'jobs')
        self.assertEqual(formatted, 'Steve Jobs')

def main():
    unittest.main()

if __name__ == '__main__':
    main()