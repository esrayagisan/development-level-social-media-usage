import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr

# Load data
monthly = pd.read_csv("monthly_time_spend_by_country.csv")
android = pd.read_csv("android_phone_use_by_country.csv")
dev = pd.read_csv("development_country.csv")

# Clean Country_Code
for df_ in [monthly, android, dev]:
    df_["Country_Code"] = df_["Country_Code"].astype(str).str.strip()

# Merge datasets
df = monthly.merge(android, on="Country_Code", how="left")
df = df.merge(dev, on="Country_Code", how="left")
df.replace("-", np.nan, inplace=True)


# Chech if worldwide got lost during merge
monthly_worldwide = monthly[monthly["Country"].str.lower() == "worldwide"]
merged_worldwide = df[df["Country"].str.lower() == "worldwide"]

if merged_worldwide.empty and not monthly_worldwide.empty:
    print("⚠ Worldwide disappeared during merge — restoring it.")
    
    # Row of Worldwide
    w_row = monthly_worldwide.copy()

    # Set android and development scores as None
    for col in df.columns:
        if col not in w_row.columns:
            w_row[col] = np.nan

    # Add column to the data frame
    w_row = w_row[df.columns]
    df = pd.concat([df, w_row], ignore_index=True)

else:
    print("✔ Worldwide found in merged dataframe.")



social_cols = [c for c in monthly.columns if c not in ["Country", "Country_Code"]]
development_cols = dev.columns.drop(["Country", "Country_Code"], errors="ignore")

print("Social media platforms: ", social_cols)
print("Development indicators:", list(development_cols))

# Z score normalization
# The datasets have data for the top 50 most used countries
# It can create a bias
# That's why a comparison with worldwide data is made

df_z = df.copy()

for col in social_cols:

    worldwide_value = df.loc[df["Country"] == "Worldwide", col]

    world_mean = float(worldwide_value.values[0])

    country_values = df.loc[df["Country"] != "Worldwide", col].astype(float)
    std_val = np.nanstd(country_values)

    if std_val == 0:
        print(f"⚠ Standard deviation = 0 for {col}, cannot compute z-score.")
        continue

    df_z[col + "_zscore"] = (df[col].astype(float) - world_mean) / std_val

print("\nZ-score normalizasyonu tamamlandı.")
print(df_z[[c for c in df_z.columns if c.endswith("_zscore")]].head())

zscore_cols = [c for c in df_z.columns if c.endswith("_zscore")]


# Correalation Heatmap (z-score)


plt.figure(figsize=(12, 8))
sns.heatmap(df_z[zscore_cols + list(development_cols)].corr(), annot=True, fmt=".2f")
plt.title("Z-Score Normalized Social Media vs Development Indicators Correlation")
plt.show()


# Hypothesis Testing (z-score)


results = []

for soc in zscore_cols:
    for devcol in development_cols:

        clean = df_z[[soc, devcol]].dropna()

        if len(clean) > 5:
            pear_corr, pear_p = pearsonr(clean[soc], clean[devcol])
            spear_corr, spear_p = spearmanr(clean[soc], clean[devcol])

            results.append({
                "SocialMedia_Z": soc,
                "Development": devcol,
                "Pearson_Corr": pear_corr,
                "Pearson_p": pear_p,
                "Spearman_Corr": spear_corr,
                "Spearman_p": spear_p
            })

results_df = pd.DataFrame(results)

print("\n--- Hypothesis Test Results (Z-score Normalized) ---")
print(results_df.sort_values("Pearson_p"))

significant = results_df[
    (results_df["Pearson_p"] < 0.05) | (results_df["Spearman_p"] < 0.05)
]

print("\n--- SIGNIFICANT RELATIONSHIPS (p < 0.05) ---")
print(significant)
