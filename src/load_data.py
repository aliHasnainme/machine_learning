import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk

def load_data(csv_file_path):
    data = pd.read_csv(csv_file_path)
    return data