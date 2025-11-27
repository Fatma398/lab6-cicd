import unittest
import pandas as pd
from filter_columns import filter_columns   # adjust if your file name is different

class TestFilterColumns(unittest.TestCase):
    def test_two_columns(self):
        df = pd.DataFrame({
            "a": [1,2],
            "b": [3,4],
            "c": [5,6]
        })
        result = filter_columns(df)
        self.assertEqual(result.shape[1], 2)

if __name__ == "__main__":
    unittest.main()
