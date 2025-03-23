import pandas as pd
import numpy as np

data = {
    'PlayerID': range(1, 15),
    'RunsScored': [450, 320, 670, 560, 300, 490, 720, 610, 580, 520, 600, 540, 690, 620],
    'MatchesPlayed': [15, 12, 20, 18, 10, 16, 22, 19, 17, 14, 21, 18, 20, 19],
    'StrikeRate': [145.5, 150.8, 155.3, 148.4, 142.6, 147.2, 151.5, 149.1, 146.3, 143.6, 152.8, 144.7, 153.5, 148.9],
    'Team': ['CSK', 'MI', 'RCB', 'KKR', 'DC', 'SRH', 'RR', 'PBKS', 'GT', 'LSG', 'MI', 'RCB', 'CSK', 'KKR']
}

df = pd.DataFrame(data)

# Normalization functions
def normalize_minmax(series):
    """Performs Min-Max normalization."""
    return (series - series.min()) / (series.max() - series.min())

def normalize_zscore(series):
    """Performs Z-Score normalization."""
    return (series - series.mean()) / series.std()

def normalize_decimal_scaling(series):
    """Performs Decimal Scaling normalization."""
    max_val = series.abs().max()
    scaling_factor = 10 ** (np.ceil(np.log10(max_val)))
    return series / scaling_factor

# Display the original dataset
print("Original IPL-Themed Dataset:")
print(df)

# Columns to normalize
numeric_cols = ['RunsScored', 'MatchesPlayed', 'StrikeRate']

# Apply Min-Max Normalization
df_minmax = df.copy()
for col in numeric_cols:
    df_minmax[col] = normalize_minmax(df[col])

print("\nDataset after Min-Max Normalization:")
print(df_minmax)

# Apply Z-Score Normalization
df_zscore = df.copy()
for col in numeric_cols:
    df_zscore[col] = normalize_zscore(df[col])

print("\nDataset after Z-Score Normalization:")
print(df_zscore)

# Apply Decimal Scaling Normalization
df_decimal = df.copy()
for col in numeric_cols:
    df_decimal[col] = normalize_decimal_scaling(df[col])

print("\nDataset after Decimal Scaling Normalization:")
print(df_decimal)
