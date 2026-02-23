import pandas as pd
import matplotlib.pyplot as plt

# Read expense data from CSV
df = pd.read_csv("expenses.csv")

# Clean data
df["date"] = pd.to_datetime(df["date"])
df["amount"] = df["amount"].astype(float)

# Total spent
total_spent = df["amount"].sum()

# Spending by category
by_category = df.groupby("category")["amount"].sum().sort_values(ascending=False)

# Daily spending trend
daily_spend = df.groupby(df["date"].dt.date)["amount"].sum()
avg_daily = daily_spend.mean()

print("===== Budget Analyzer Summary =====")
print(f"Total spent: ${total_spent:.2f}\n")

print("Spending by category:")
print(by_category)

print(f"\nAverage daily spend: ${avg_daily:.2f}")

# Create a simple bar chart
plt.figure()
by_category.plot(kind="bar")
plt.title("Spending by Category")
plt.ylabel("Amount ($)")
plt.xlabel("Category")
plt.tight_layout()

# Save chart image
plt.savefig("spending_by_category.png")
print("\nChart saved as spending_by_category.png")
