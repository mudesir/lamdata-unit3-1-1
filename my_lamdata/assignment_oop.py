# my_lamdata/assignment_oop
from pandas import DataFrame

class DataFrameProcessor():
    def __init__(self, df):
        """
        Params (df) a DataFrame with a column called
        "abbrev" that has state abbrevations.

        """
        self.df = df
    

    def add_state_names_column(self):
        
        """
        This add a column of corresponding state names
        to a DataFrame.
        
        Return a copy of the original DataFrame, but with
        an extra column.
        """
        names_map = {"CA": "California", "CO": "Collorado",
                 "CT": "Connecticut", "DC": "District of Columbia",
                 "TX": "Texas"}
        
        # this way will return the exisisting df
        # new_df = self.df.copy()
        # new_df["name"] = new_df["abbrev"].map(names_map)
        # return new_df

        # this way will mutate the exisiting df
        self.df["name"] = self.df["abbrev"].map(names_map)


if __name__ == "__main__":
    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    
    processor = DataFrameProcessor(df=df)
    print(processor.df.head())
    processor.add_state_names_column()
    print(processor.df.head())

    