import pandas as pd
df = pd.read_excel(r"C:\Users\tyson\OneDrive\Desktop\Apr 2020 Act Rep.xlsx", parse_dates=["Transport Date"])
pd.set_option("display.max_columns", None)
df["Pick-up Location"].fillna("None", inplace=True)
df["Mode"].fillna("None", inplace=True)
mask = df["Status"] != "Canceled"
df = df[mask]

df["Assigned To ID"] = df["Assigned To ID"].astype(int)
df["Ack->Cmp"] = df["Ack->Cmp"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
df["Ack->InP"] = df["Ack->InP"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
df["Asgn->Ack"] = df["Asgn->Ack"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
df["Asgn->Cmp"] = df["Asgn->Cmp"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
df["InP->Cmp"] = df["InP->Cmp"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
df["Pnd->Asgn"] = df["Pnd->Asgn"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
df["Pnd->Cmp"] = df["Pnd->Cmp"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
df["Total Delay Time"] = df["Total Delay Time"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)

raw_report = df[[
    'Assigned To ID',
    'Assigned To',
    'Ack->Cmp',
    'Ack->InP',
    'Asgn->Ack',
    'Asgn->Cmp',
    'InP->Cmp',
    'Pnd->Asgn',
    'Pnd->Cmp',
    'Total Delay Time'
    ]]

raw_report.head(3)
