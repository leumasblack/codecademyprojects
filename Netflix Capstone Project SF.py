from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

netflix_stocks = pd.read_csv("NFLX.csv")
dowjones_stocks = pd.read_csv("DJI.csv")
netflix_stocks_quarterly = pd.read_csv("NFLX_daily_by_quarter.csv")

netflix_stocks.rename(columns={"Adj Close": "Price"}, inplace=True)
dowjones_stocks.rename(columns={"Adj Close": "Price"}, inplace=True)
netflix_stocks_quarterly.rename(columns={"Adj Close": "Price"}, inplace=True)
print(netflix_stocks.head())
print(dowjones_stocks.head())
print(netflix_stocks_quarterly.head())


sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.8, rc={"grid.linewidth": 0.4})
ax = sns.violinplot(data=netflix_stocks_quarterly, x="Quarter", y="Price")
plt.subplots_adjust(hspace=3)
sns.color_palette("Spectral")
sns.despine(left=True, bottom=True)
ax.set_title("Distribution of 2017 Netflix Stock Prices by Quarter")
ax.set_xlabel("Business Quarters in 2017")
ax.set_ylabel("Closing Stock Price")
plt.savefig("Stock Price vs Quarter Violin.png")
plt.show()


x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017", "2Q2017", "3Q2017", "4Q2017"]
earnings_actual = [.4, .15, .29, .41]
earnings_estimate = [.37, .15, .32, .41]

plt.scatter(x_positions, earnings_actual, color="red", alpha=0.5)
plt.scatter(x_positions, earnings_estimate, color="blue", alpha=0.5)
plt.legend(["Actual", "Estimate"])
plt.xticks(x_positions, chart_labels)
plt.title("Earnings Per Share in Cents")
plt.savefig("Stock Actual Vs Estimate Earnings Scatter Plot.png")
plt.show()


# The metrics below are in billions of dollars
revenue_by_quarter = [2.79, 2.98, 3.29, 3.7]
earnings_by_quarter = [.0656, .12959, .18552, .29012]
quarter_labels = ["2Q2017", "3Q2017", "4Q2017", "1Q2018"]

# Revenue
n = 1  # This is our first dataset (out of 2)
t = 2  # Number of dataset
d = 4  # Number of sets of bars
w = 0.8  # Width of each bar
bars1_x = [t * element + w * n for element
           in range(d)]
plt.bar(bars1_x, revenue_by_quarter)

# Earnings
n = 2  # This is our second dataset (out of 2)
t = 2  # Number of dataset
d = 4  # Number of sets of bars
w = 0.8  # Width of each bar
bars2_x = [t * element + w * n for element
           in range(d)]
plt.bar(bars2_x, earnings_by_quarter,)

middle_x = [(a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]
plt.title("Earnings and Revenue reported by Netflix")
plt.xticks(middle_x, quarter_labels)
plt.legend(labels)
plt.savefig("Revenue Vs Earnings by Quarter Bar Plot.png")
plt.show()

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

ax1 = plt.subplot(1, 2, 1)
plt.plot(netflix_stocks['Date'], netflix_stocks['Price'])
ax1.set_xlabel("Date")
ax1.set_ylabel("Stock Price", fontsize=12)
ax1.set_title("Netflix", fontweight='bold')
plt.xticks(fontsize=10, rotation=90, ticks=(netflix_stocks["Date"]), labels=months)
plt.yticks(fontsize=10)

ax2 = plt.subplot(1, 2, 2)
plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'], 'darkblue')
ax2.set_xlabel("Date")
ax2.set_ylabel("Stock Price", fontsize=12)
ax2.set_title("Dow Jones", fontweight='bold')
plt.xticks(fontsize=10, rotation=90, ticks=(dowjones_stocks["Date"]), labels=months)
plt.yticks(fontsize=10)

plt.subplots_adjust(wspace=0.5)
plt.savefig("Netflix Vs DJ comparison.png")
plt.show()
