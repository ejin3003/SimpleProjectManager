# from ProjectPhoenix.Tools.act_rep_cleaner import *
# from ProjectPhoenix.Tools.graph_config import *
from Tools.act_rep_cleaner import *
from Tools.graph_config import *


path = r"C:\Users\ejin3\OneDrive\Desktop\Apr 2020 Act Rep.xlsx"
df_daily_totals = act_report(path)

graph_daily_trip_totals(df_daily_totals)
