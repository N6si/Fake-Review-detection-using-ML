import pandas as pd

df = pd.read_csv("fake_reviews_dataset.csv")
print(df['label'].unique())
