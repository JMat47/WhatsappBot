from numpy.core.arrayprint import printoptions
import pandas as pd
from time import sleep
from csv import writer

donorData = pd.read_csv(r"C:\Users\jerry\OneDrive\Documents\Sender\Final_Data.csv")
list_of_rows = [list(row) for row in donorData.values]

for x in list_of_rows:
    x.append("Yes")
    print(x)
    data = [x]
    column_names = ["Name", "BloodGroup", "PhoneNo","District","City","Donor?"]
    df = pd.DataFrame(data, columns=column_names)
    df.to_csv('SavedData2.csv',mode='a', index=False, header=False)

