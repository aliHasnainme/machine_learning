from src.load_data import load_data
from src.cleaning import data_cleaning

data = load_data(r"C:\Users\PMLS\Desktop\New folder\artifacts\raw.csv")
data = data_cleaning(data)
print(data)