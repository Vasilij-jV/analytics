import unittest
import pandas as pd
from data_plotting import export_data_to_csv
import os


class Exporting(unittest.TestCase):

    def test_create_new_file(self):
        data = {'A': [1, 2, 3], 'B': ['x', 'y', 'z']}
        df = pd.DataFrame(data)
        file_name = 'save_dataframe.csv'
        export_data_to_csv(df, file_name)

        # Проверяем, что файл был успешно создан
        self.assertTrue(os.path.exists(file_name))


if __name__ == '__main__':
    unittest.main()
