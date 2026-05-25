import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load NASA Exoplanet Archive dataset
df = pd.read_csv(
    r"D:\Documents\PS_2026.05.14_07.48.34.csv",
    comment="#"
)

# Display first rows of dataset
print(df.head())

# Select relevant columns
df = df[[
    "pl_name",
    "pl_rade",
    "pl_bmasse",
    "pl_orbper",
    "discoverymethod",
    "disc_year"
]]

# Remove missing values
df = df.dropna(subset=["pl_rade", "pl_orbper"])

# Remove extreme orbital period outliers for readability
df = df[df["pl_orbper"] < 5000]

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

print("""
Summary Insight:
The dataset contains a wide range of planetary properties, with particularly
large variation in orbital period and planetary mass measurements.
""")

# -----------------------------
# Planet Radius Distribution
# -----------------------------

plt.figure()
plt.hist(df["pl_rade"], bins=30)
plt.title("Distribution of Exoplanet Radii (Earth radii)")
plt.xlabel("Radius")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("planet_radius_hist.png")
plt.show()

print("""
Insight:
The distribution of exoplanet radii shows substantial variation in planetary size.
Smaller planets appear more frequently within the dataset, although this may partly
reflect observational bias, as certain detection methods are more sensitive to
larger planets orbiting close to their host stars.
""")

# -----------------------------
# Orbital Period Distribution
# -----------------------------

plt.figure()
logbins = np.logspace(
    np.log10(df["pl_orbper"].min()),
    np.log10(df["pl_orbper"].max()),
    30
)

plt.hist(df["pl_orbper"], bins=logbins)
plt.xscale("log")
plt.title("Orbital Period Distribution (log scale)")
plt.xlabel("Orbital period (days)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("orbital_period_hist.png")
plt.show()

print("""
Insight:
The orbital period distribution is strongly skewed towards short-period planets.
This is likely influenced by selection effects in transit surveys, where planets
with shorter orbital periods produce more frequent and detectable signals.
A logarithmic scale was used to better visualise the spread of values.
""")

# -----------------------------
# Discovery Methods
# -----------------------------

method_counts = df["discoverymethod"].value_counts()

plt.figure()
method_counts = df["discoverymethod"].value_counts()

# Keep only methods with more than 5 detections
method_counts = method_counts[method_counts > 5]

method_counts.plot(kind="bar")
plt.title("Exoplanet Discovery Methods")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("method_counts.png")
plt.show()

print("""
Insight:
Transit photometry is the dominant exoplanet detection method within the dataset.
This reflects the success of large-scale missions such as NASA's TESS and Kepler
space telescopes, which continuously monitor stellar brightness for periodic dips
caused by planetary transits.
""")

# -----------------------------
# Overall Interpretation
# -----------------------------

print("""
Overall Interpretation:
The dataset demonstrates clear observational biases within exoplanet detection.
Current discovery methods preferentially identify planets that are large, close to
their host stars, and produce strong observational signals. As a result, the known
exoplanet population may not fully represent the true diversity of planetary systems.
""")