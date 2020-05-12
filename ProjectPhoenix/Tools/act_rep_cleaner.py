import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
df_daily_totals.columns = ["Date", "Daily Total"]

x = df_daily_totals["Date"].to_list()
y = df_daily_totals["Daily Total"].to_list()

# Increases Graph Size
# fig = plt.gcf()
# fig.set_size_inches(16, 10)

plt.figure(figsize=(10, 6), dpi=300)

plt.style.use("ggplot")
plt.plot(x, y, label="Total Escorts", linewidth=2, marker=".", markersize=6)

plt.title("Completed Central Trips for the Month of April", fontdict={"fontsize": 20})
plt.xlabel("April 2020", fontdict={"fontsize": 14})
plt.xticks(rotation=45)
plt.ylabel("Total Trips", fontdict={"fontsize": 14})

plt.legend()
plt.show()


# plt.style.use("ggplot")
# ax = sns.lineplot(x="Date", y="Daily Total", data=df_daily_totals)
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

