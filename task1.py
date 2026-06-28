import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# Load Dataset
# ----------------------------
df = pd.read_csv("data/titanic.csv")

# ----------------------------
# Dataset Summary
# ----------------------------
print("=" * 45)
print("        TITANIC DATASET SUMMARY")
print("=" * 45)

print(f"Total Records : {len(df)}")
print(f"Male          : {(df['Sex'] == 'male').sum()}")
print(f"Female        : {(df['Sex'] == 'female').sum()}")
print(f"Average Age   : {df['Age'].mean():.2f}")
print(f"Minimum Age   : {df['Age'].min()}")
print(f"Maximum Age   : {df['Age'].max()}")

print("=" * 45)

# ----------------------------
# User Menu
# ----------------------------
print("\nChoose the graph you want to display:")
print("1. Gender Distribution (Bar Chart)")
print("2. Age Distribution (Histogram)")
print("3. Display Both Graphs")

choice = input("\nEnter your choice (1/2/3): ")

# ==========================================================
# OPTION 1 - Gender Distribution
# ==========================================================
if choice == "1":

    gender_counts = df["Sex"].value_counts()

    plt.figure(figsize=(7,5))

    bars = plt.bar(
        gender_counts.index,
        gender_counts.values,
        color=["royalblue", "deeppink"],
        edgecolor="black"
    )

    # Display values above bars
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 5,
            str(int(height)),
            ha='center',
            fontsize=11,
            fontweight='bold'
        )

    plt.title("Gender Distribution", fontsize=16, fontweight="bold")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.savefig("gender_distribution.png", dpi=300)
    plt.show()

# ==========================================================
# OPTION 2 - Age Distribution
# ==========================================================
elif choice == "2":

    plt.figure(figsize=(8,5))

    plt.hist(
        df["Age"].dropna(),
        bins=20,
        color="mediumseagreen",
        edgecolor="black"
    )

    plt.title("Age Distribution", fontsize=16, fontweight="bold")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.savefig("age_distribution.png", dpi=300)
    plt.show()

# ==========================================================
# OPTION 3 - Display Both
# ==========================================================
elif choice == "3":

    # Gender Distribution
    gender_counts = df["Sex"].value_counts()

    plt.figure(figsize=(7,5))

    bars = plt.bar(
        gender_counts.index,
        gender_counts.values,
        color=["royalblue", "deeppink"],
        edgecolor="black"
    )

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 5,
            str(int(height)),
            ha='center',
            fontsize=11,
            fontweight='bold'
        )

    plt.title("Gender Distribution", fontsize=16, fontweight="bold")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.savefig("gender_distribution.png", dpi=300)
    plt.show()

    # Age Distribution
    plt.figure(figsize=(8,5))

    plt.hist(
        df["Age"].dropna(),
        bins=20,
        color="mediumseagreen",
        edgecolor="black"
    )

    plt.title("Age Distribution", fontsize=16, fontweight="bold")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.savefig("age_distribution.png", dpi=300)
    plt.show()

# ==========================================================
# Invalid Input
# ==========================================================
else:
    print("\nInvalid Choice! Please run the program again and choose 1, 2, or 3.")