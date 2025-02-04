import pandas as pd

data_file = 'melb_data.csv'

#read data in csv
mal_data = pd.read_csv(data_file)

#prints summary of data
print(mal_data.describe())
