import pandas as pd

# Sample expense data (you can replace this with your real data later)
data = {
    "date": ["2026-02-01", "2026-02-02", "2026-02-03", "2026-02-04", "2026-02-05"],
    "category": ["Food", "Gas", "Food", "Shopping", "Gas"],
    "amount": [18.75, 42.10, 12.50, 65.00, 38.40]
}

df = pd.DataFrame(data)

# Clean data
df["date"] = pd.to_datetime(df["date"])
df["amount"] = df["amount"].astype(float)

# Total spent
total_spent = df["amount"].sum()

# Spending by category
by_category = df.groupby("category")["amount"].sum().sort_values(ascending=False)

# Average daily spend
daily_spend = df.groupby(df["date"].dt.date)["amount"].sum()
avg_daily = daily_spend.mean()

print("===== Budget Analyzer Summary =====")
print(f"Total spent: ${total_spent:.2f}\n")

print("Spending by category:")
print(by_category)

print(f"\nAverage daily spend: ${avg_daily:.2f}")
