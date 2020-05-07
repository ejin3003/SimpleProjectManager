import pandas as pd

df = pd.read_excel(r"C:\Users\ejin3\OneDrive\Desktop\Apr 2020 Act Rep.xlsx", parse_dates=["Transport Date"])
pd.set_option("display.width", 400)
pd.set_option("display.max_columns", None)
df["Transport Date"] = df["Transport Date"].dt.date

mask = df["Status"] != "Canceled"
df = df[mask]

# print(df.info())
print(df["Pick-up Location"].nunique())
