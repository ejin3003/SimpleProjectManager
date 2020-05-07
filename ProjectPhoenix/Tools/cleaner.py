import pandas as pd

df = pd.read_excel(r"C:\Users\ejin3\OneDrive\Desktop\Apr 2020 Act Rep.xlsx", parse_dates=["Transport Date"])
pd.set_option("display.width", 400)
pd.set_option("display.max_columns", None)
df["Assigned To"] = df["Assigned To"].astype("category")
df["Status"] = df["Status"].astype("category")
df["Mode"] = df["Mode"].astype("category")
df["Region"] = df["Region"].astype("category")
df["Transport Type"] = df["Transport Type"].astype("category")
df["Transport Date"] = df["Transport Date"].dt.date

mask = df["Status"] != "Canceled"
df = df[mask]

new_mask = pd.isnull(df).any(axis=1)
print(df[new_mask])
# print(df.info())
# print(df["Pick-up Location"].nunique())
