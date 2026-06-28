import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/titanic.csv")

# ----------------------------
# Gender Distribution
# ----------------------------

gender_counts = df["Sex"].value_counts()

plt.figure(figsize=(7,5))

plt.bar(
    gender_counts.index,
    gender_counts.values,
    color=["royalblue", "deeppink"],
    edgecolor="black"
)

plt.title("Gender Distribution", fontsize=16, fontweight="bold")
plt.xlabel("Gender", fontsize=12)
plt.ylabel("Count", fontsize=12)
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