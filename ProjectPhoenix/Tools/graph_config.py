
def graph_daily_trip_totals(df_daily_totals):
    import pandas as pd
    import matplotlib.pyplot as plt

    x = df_daily_totals["Date"].to_list()
    y = df_daily_totals["Daily Total"].to_list()

    plt.figure(figsize=(10, 6), dpi=300)

    plt.style.use("ggplot")
    plt.plot(x, y, label="Total Escorts", linewidth=2, marker=".", markersize=6)

    plt.title("Completed Central Trips for the Month of April", fontdict={"fontsize": 20})
    plt.xlabel("April 2020", fontdict={"fontsize": 14})
    plt.xticks(rotation=45)
    plt.ylabel("Total Trips", fontdict={"fontsize": 14})

    plt.legend()
    plt.show()

