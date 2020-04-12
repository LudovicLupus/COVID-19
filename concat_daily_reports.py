
from pathlib import Path
import pandas as pd

desired_width = 640
pd.set_option('display.max_columns', 10)

csv_1 = Path.cwd() / "COVID-19/csse_covid_19_data/csse_covid_19_daily_reports" / "02-25-2020.csv"
csv_2 = Path.cwd() / "COVID-19/csse_covid_19_data/csse_covid_19_daily_reports" / "03-01-2020.csv"

df1 = pd.read_csv(csv_1)
df2 = pd.read_csv(csv_2)

df3 = pd.concat([df1, df2], sort=False)

# print(df3.head())
print(df1.count())
print(df2.count())
print(df3.count())
