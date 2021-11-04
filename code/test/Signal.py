import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data2.txt" ,header = None ,delimiter =" ")
data = pd.DataFrame(data1)

x = data[0]
y = data[1]

plt.plot(x,y)
plt.show()