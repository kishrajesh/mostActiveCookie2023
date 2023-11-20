from most_active_cookie import Cookie
import unittest
from unittest.mock import patch, mock_open
class TestCookieClass(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='cookie,timestamp\ncookie1,2023-01-01T10:00:00\ncookie2,2023-01-01T12:00:00\ncookie1,2023-01-01T13:00:00\n')
    def test_specific_date(self, mock_file):
        expected_result = ['cookie1']
        result = Cookie.most_cookie('mocked_file.csv', '2023-01-01')
        self.assertEqual(result, expected_result)

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_missing_file(self, mock_file):
        with self.assertRaises(FileNotFoundError):
            Cookie.most_cookie('nonexistent_file.csv', '2023-01-01')

    @patch('builtins.open', new_callable=mock_open, read_data='')
    def test_empty_file(self, mock_file):
        result = Cookie.most_cookie('empty_cookie_log.csv', '2023-01-01')
        self.assertEqual(result, [])

    @patch('builtins.open', new_callable=mock_open, read_data='cookie,timestamp\ncookie1,2023-01-01T10:00:00\ncookie2,2023-01-01T12:00:00\ncookie1,2023-01-01T13:00:00\ncookie2,2023-01-01T15:00:00\n')
    def test_multiple_max_occurrences(self, mock_file):
        expected_result = ['cookie1', 'cookie2']  # Replace this with the expected output for multiple max occurrences
        result = Cookie.most_cookie('mocked_file.csv', '2023-01-01')
        self.assertCountEqual(result, expected_result)
        
    def test_invalid_date_format(self):
        # Test for invalid date format
        with self.assertRaises(Exception):
            Cookie.most_cookie('cookie_log.csv', 'invalid_date_format')

if __name__ == '__main__':
    unittest.main()