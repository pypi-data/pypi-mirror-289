import unittest
from datetime import datetime, timedelta
from kmon.utility import find_latest_file

class TestUtilityService(unittest.TestCase):
    def test_latest_file_fetch(self):
        file_name = find_latest_file("kmon-datalake-prod", 'compress/kmon_v1_raw_specif')
        print("file_name: ", file_name)
        yesterday = (datetime.today()-timedelta(days=1)).strftime('%Y-%m-%d')
        self.assertIn(yesterday, file_name)

if __name__ == '__main__':
    unittest.main()