import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv(r"/Users/onyinyechiaghaizu/Downloads/archive-2/covid19_italy_region.csv")
#print(data.isnull().sum)
#relating the variables with scatterplots
data.head()
sns.relplot(x="TotalPositiveCases", y="Recovered", data=data)
