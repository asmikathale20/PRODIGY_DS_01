import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/titanic.csv")
print("=" * 40)
print("      TITANIC DATASET SUMMARY")
print("=" * 40)

print(f"Total Records : {len(df)}")
print(f"Male          : {(df['Sex'] == 'male').sum()}")
print(f"Female        : {(df['Sex'] == 'female').sum()}")

print(f"Average Age   : {df['Age'].mean():.2f}")
print(f"Minimum Age   : {df['Age'].min()}")
print(f"Maximum Age   : {df['Age'].max()}")

print("=" * 40)

# ----------------------------
# Gender Distribution
# ----------------------------

# ----------------------------
# Gender Distribution
# ----------------------------

gender_counts = df["Sex"].value_counts()

plt.figure(figsize=(7,5))

bars = plt.bar(
    gender_counts.index,
    gender_counts.values,
    color=["royalblue", "deeppink"],
    edgecolor="black"
)

# Display count above each bar
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 5,
        f"{int(height)}",
        ha="center",
        fontsize=11,
        fontweight="bold"
    )

plt.title("Gender Distribution", fontsize=16, fontweight="bold")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("gender_distribution.png", dpi=300)
plt.show()

# ----------------------------
# Age Distribution
# ----------------------------

plt.figure(figsize=(8,5))

plt.hist(
    df["Age"].dropna(),
    bins=20,
    color="mediumseagreen",
    edgecolor="black"
)

plt.title("Age Distribution", fontsize=16, fontweight="bold")
plt.xlabel("Age", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("age_distribution.png", dpi=300)
plt.show()