from pandas import DataFrame
from my_lamdata.mymod import enlarge

print("Hello")

print(enlarge(8))


df = DataFrame({"state":["CT", "CO", "CA", "TX"]})
print(df.head())