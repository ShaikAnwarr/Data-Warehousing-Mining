import pandas as pd

data = [
    [101, "Virat Kohli", 34, 57.7, 12400, "RCB"],
    [102, "MS Dhoni", 41, None, 10500, "CSK"],
    [103, "Rohit Sharma", 36, 45.4, None, "MI"],
    [104, "Jasprit Bumrah", 29, None, 700, "MI"],
    [105, "David Warner", 37, 42.5, 11400, "DC"],
    [106, "AB de Villiers", None, 51.2, 12000, "RCB"],
    [107, "KL Rahul", 31, 46.7, 8600, "LSG"],
    [108, "Steve Smith", 33, None, 9500, "RR"],
    [109, "Shubman Gill", None, 40.8, None, "GT"],
    [110, "Hardik Pandya", 30, 35.4, 6400, "GT"],
]

# Creating the DataFrame
df = pd.DataFrame(data, columns=["PlayerID", "PlayerName", "Age", "BattingAverage", "TotalRuns", "Team"])
print("Original DataFrame:")
print(df)
print()

# 1. Removing rows with missing values
df_removed = df.dropna()  # Drop rows with missing values
print("After removing rows with missing values:")
print(df_removed)
print()

# 2. Filling missing values with column-wise means
df_filled = df.copy()
df_filled["Age"] = df_filled["Age"].fillna(df["Age"].mean())
df_filled["BattingAverage"] = df_filled["BattingAverage"].fillna(df["BattingAverage"].mean())
df_filled["TotalRuns"] = df_filled["TotalRuns"].fillna(df["TotalRuns"].mean())

print("After filling missing values with column means:")
print(df_filled)
print()

# 3. Filling missing values with team-wise means
df_team_filled = df.copy()
for col in ["Age", "BattingAverage", "TotalRuns"]:
    df_team_filled[col] = df_team_filled.groupby("Team")[col].transform(lambda x: x.fillna(x.mean()))

print("After filling missing values with team-specific means:")
print(df_team_filled)
