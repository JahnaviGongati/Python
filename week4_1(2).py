import pandas as pd
data = [10,20,30,40,50]
series = pd.Series(data)
list_data = series.tolist()
print(list_data)
print(type(list_data))
