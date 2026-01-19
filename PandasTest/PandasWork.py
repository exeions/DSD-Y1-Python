import pandas as pd

print(pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]}))

print(pd.Series([1, 2, 3, 4, 5]))

wine_reviews = pd.read_csv("covid_19_data.csv")

print(wine_reviews.head)