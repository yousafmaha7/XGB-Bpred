import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load the data
df = pd.read_csv('merged_4lac_data.csv')

# Separate the first two columns
epitope_label = df.iloc[:, :2]
features = df.iloc[:, 2:]

# Initialize scalers
minmax_scaler = MinMaxScaler()

# Apply MinMaxScaler
minmax_scaled = minmax_scaler.fit_transform(features)
minmax_scaled_df = pd.DataFrame(minmax_scaled, columns=features.columns)

# Combine with epitope and label columns
minmax_scaled_final = pd.concat([epitope_label, minmax_scaled_df], axis=1)

# Save the normalized datasets
minmax_scaled_final.to_csv('minmax_scaled_4lac_data.csv', index=False)

print("Normalized datasets have been saved as 'standard_scaled_4lac_data.csv' and 'minmax_scaled_4lac_data.csv'")

# Display the first few rows of both normalized datasets
print("\
First few rows of MinMaxScaler normalized data:")
print(minmax_scaled_final.head())
