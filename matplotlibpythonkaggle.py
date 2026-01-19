import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Download latest version
path = "covid_19_data.csv"


data = pd.read_csv(path)

sns.heatmap(data.isnull())
plt.show()


print(data.count())