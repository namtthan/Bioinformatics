# Learning PANDAS

# Data as tables
import pandas
# It is a CSV file, but the separator is “;”
data = pandas.read_csv('examples/brain_size.csv', sep=';', na_values="NaN")
# A pandas.DataFrame can also be seen as a dictionary of 1D ‘series’,
# eg arrays or lists. If we have 3 numpy arrays
import numpy as np
t = np.linspace(-6,6,20)
sin_t = np.sin(t)
cos_t = np.cos(t)
data_frame = pandas.DataFrame({'t': t, 'sin': sin_t, 'cos': cos_t})

# manipulating data
print(data.shape)
print(data.columns)
print(data['Gender'])
print(data[data['Gender'] == 'Female']['VIQ'].mean())
# For a quick view on a large dataframe, use its describe method:
print(data.describe())
print(data_frame.describe())
