import pandas as pd
import matplotlib.pyplot as plt

# Dataset load
df = pd.read_csv("gender_population.csv", skiprows=4)

# 2025 data
year = "2025"

# Top 15 countries
top15 = df[["Country Name", year]].dropna().sort_values(by=year, ascending=False).head(15)

countries = top15["Country Name"]
population = top15[year]

# Male and Female (approximation)
male = population * 0.515
female = population * 0.485

# -------- Graph 1 --------
plt.figure(figsize=(14,6))
x = range(len(countries))
width = 0.35

plt.bar([i-width/2 for i in x], male, width=width, label="Male")
plt.bar([i+width/2 for i in x], female, width=width, label="Female")

plt.xticks(x, countries, rotation=45, ha="right")
plt.title("Male vs Female Population - Top 15 Countries (2025)")
plt.xlabel("Countries")
plt.ylabel("Population")
plt.legend()
plt.tight_layout()
plt.savefig("gender_population.png", dpi=300)
plt.show()

# Age groups (approximation)
age_0_14 = population * 0.24
age_15_64 = population * 0.68
age_65 = population * 0.08

# -------- Graph 2 --------
plt.figure(figsize=(14,6))

plt.bar(countries, age_0_14, label="0-14 years")
plt.bar(countries, age_15_64, bottom=age_0_14, label="15-64 years")
plt.bar(countries, age_65, bottom=age_0_14+age_15_64, label="65+ years")

plt.xticks(rotation=45, ha="right")
plt.title("Age Distribution (0-14 / 15-64 / 65+) - Top 15 Countries (2025)")
plt.xlabel("Countries")
plt.ylabel("Population")
plt.legend()
plt.tight_layout()
plt.savefig("age_distribution.png", dpi=300)
plt.show()

print("Task completed successfully!")