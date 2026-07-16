# Dante le Roux 45911398
import pandas as pd
df = pd.read_csv("grades.csv")

grouped_df = df.groupby("Course")["Grade"].mean()
print(grouped_df)
