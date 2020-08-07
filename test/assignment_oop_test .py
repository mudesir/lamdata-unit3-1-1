

import unittest
from pandas import DataFrame
from my_lamdata.assignment_oop import add_state_names_column


class TestAssignment@(unittest.TestCase):

    def test_add_state_names(self):

        
        
        df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
        processor = DataFrameProcessor(df=df)
        self.assertEqual(list(processor.df.columns), ['abbrev'])
        self.assertEqual(len(processor.df.columns), 1)
        self.assertEqual(processor.df.iloc[0]['abbrev'], 'CA')

        processor = add_state_names_column()

        self.assertEqual(list(processor.df.columns), ['abbrev'])
        self.assertEqual(len(processor.df.columns), 1)
        self.assertEqual(processor.df.iloc[0]['abbrev'], 'CA')
        self.assertEqual(processor.df.iloc[0]['name'], 'California')

if __name__ == '__main__':
    unittest.main()