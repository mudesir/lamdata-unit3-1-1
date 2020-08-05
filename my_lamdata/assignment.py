# my_lamdata/assignment.py
from pandas import DataFrame

# helper function from assignment
# State abbreviation -> Full Name and visa versa. FL -> Florida, etc.
# (Handle Washington DC and territories like Puerto Rico etc.)


def add_state_names_column(my_df):
    """
    This add a column of corresponding state names
    to a DataFrame.

    Params (my_df) a DataFrame with a column called
    "abbrev" that has state abbrevations.

    Return a copy of the original DataFrame, but with
    an extra column.
    """
    new_df = my_df.copy()
    names_map = {"CA": "California", "CO": "Collorado",
                 "CT": "Connecticut", "DC": "District of Columbia",
                 "TX": "Texas"}
    new_df["name"] = new_df["abbrev"].map(names_map)
    return new_df


if __name__ == "__main__":
    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(df.head())
    mapped_df = add_state_names_column(df)
    print(mapped_df.head())
