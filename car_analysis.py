import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("cars.csv")

print("First 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

avg_price_by_brand = df.groupby("brand")["price"].mean().sort_values(ascending=False)

print("\nAverage price by brand:")
print(avg_price_by_brand)

print("\nAverage price by fuel type:")
avg_price_by_fuel = df.groupby("fuel")["price"].mean().sort_values(ascending=False)
print(avg_price_by_fuel)

print("\nTransmission counts:")
print(df["transmission"].value_counts())

correlation = df["mileage"].corr(df["price"])
print("\nCorrelation between mileage and price:")
print(correlation)

# Create a bar chart
avg_price_by_brand.plot(kind="bar")
plt.title("Average Price by Brand")
plt.xlabel("Brand")
plt.ylabel("Average Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("avg_price_by_brand.png")
plt.show()