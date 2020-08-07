from pandas import DataFrame

class CustomFrame(DataFrame):
    pass
# helper from assignment
# State abbreviation -> Full Name and visa versa. FL -> Florida, etc.
# (Handle Washington DC and territories like Puerto Rico etc.)


    def add_state_names_column(self):
        """
        
        A DataFrame with a column called
        "abbrev" that has state abbrevations.
        """
        names_map = {"CA": "California", "CO": "Collorado",
            "CT": "Connecticut", "DC": "District of Columbia",
            "TX": "Texas"}
        self["name"] = self["abbrev"].map(names_map)

        

if __name__ == "__main__":
    # df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    
    custom_frame = CustomFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(custom_frame.head())

    custom_frame.add_state_names_column()
    print(custom_frame.head())