import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn styling keeping white background
sns.set_theme(style="white")

# Time ranges
years = np.linspace(2000, 2050, 1000)
years_vr = np.linspace(2020, 2050, 1000)

# S-curve function
def s_curve(x, x0, k, y_scale=1.0, y_shift=0.0):
    return y_scale * (1 / (1 + np.exp(-k * (x - x0)))) + y_shift

# General technology growth — ends by 2025
tech_growth_full = s_curve(years, x0=2014, k=0.3, y_scale=1.0, y_shift=0)
mask = years <= 2025
years_cut = years[mask]
tech_growth = tech_growth_full[mask]

# AR growth — starts in 2020, rises from ~0.6, peaks by 2040
vr_growth_full = s_curve(years_vr, x0=2027, k=0.35, y_scale=0.5, y_shift=0.6)
mask_vr = years_vr <= 2040
years_vr_cut = years_vr[mask_vr]
vr_growth = vr_growth_full[mask_vr]

# Plot setup
plt.figure(figsize=(12, 6))

# Plot curves
plt.plot(years_cut, tech_growth, label="AR Technology Growth", linewidth=2)
plt.plot(years_vr_cut, vr_growth, label="AR App-Based Software Growth", linestyle="--", linewidth=2)

# Annotations
annotations = {
    2003: "First AR Game",
    2008: "AR Travel Guide",
    2015: "Mobile AR Emerges",
    2018: "AR In Social Media",
    2022: "AR Shopping",
    2026: "AR App Ecosystem Booms",
    2040: "AR Maturity"
}

# Annotate points
for year, label in annotations.items():
    if year <= 2025:
        y = s_curve(year, x0=2014, k=0.3)
        y_offset = 0.0  # keep it at 0.00
    else:
        y = s_curve(year, x0=2027, k=0.35, y_scale=0.5, y_shift=0.6)
        y_offset = -0.05  # Shift label slightly below the AR app curve
    plt.scatter(year, y, color='black', zorder=5)
    plt.text(year + 0.5, y + y_offset, label, fontsize=9, ha='left', va='center')

# Axes limits and labels
plt.xticks([2000, 2010, 2020, 2030, 2040, 2050])
plt.xlabel("Year")
plt.ylabel("Growth Level")
plt.title("S-Curves: AR Technology Growth vs AR App-Building (2000–2040)")
plt.legend()
plt.tight_layout()
plt.show()
