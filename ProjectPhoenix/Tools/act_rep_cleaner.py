import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"C:\Users\ejin3\OneDrive\Desktop\Apr 2020 Act Rep.xlsx", parse_dates=["Transport Date"])
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
    'Transport Date',
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
raw_report["Transport Date"] = raw_report["Transport Date"].dt.date

# Creates a DataFrame of total trips per escort
# escorts = raw_report.groupby("Assigned To")
# escort_totals = escorts.size().sort_values(ascending=False)
# df_escort_totals = pd.DataFrame(escort_totals)
# print(df_escort_totals)

dates = raw_report.groupby('Transport Date')
daily_totals = dates.size()
df_daily_totals = pd.DataFrame(data=daily_totals)
df_daily_totals.reset_index(inplace=True)

# ax = sns.lineplot(x=df_daily_totals.index, y=0, data=df_daily_totals, markers=True)
#
# # Increases Graph Size
# fig = plt.gcf()
# fig.set_size_inches(16, 10)
#
# # Rotates x-ticks by 45 degrees
# for item in ax.get_xticklabels():
#     item.set_rotation(45)
#
# plt.show()

