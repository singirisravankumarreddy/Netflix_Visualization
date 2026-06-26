import numpy as np
import os
import pandas as pd  # <--- ADD THIS LINE

# 1. Load or Generate Mock Dataset
file_path = "netflix_titles.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    print("Real dataset loaded successfully!")
else:
    print(
        f"\n[INFO] '{file_path}' not found. Generating sample data for testing..."
    )
    # Creating simulated Netflix data so the charts run flawlessly
    np.random.seed(42)
    sample_size = 500
    df = pd.DataFrame({
        "type": np.random.choice(["Movie", "TV Show"], size=sample_size, p=[0.7, 0.3]),
        "country": np.random.choice(["United States", "India", "United Kingdom", "Japan", "South Korea"], size=sample_size),
        "rating": np.random.choice(["TV-MA", "TV-14", "TV-PG", "R", "PG-13"], size=sample_size),
        "date_added": pd.date_range(start="2015-01-01", end="2024-12-31", periods=sample_size),
        "cast": "Sample Cast",
        "director": "Sample Director"
    })
    df["year_added"] = df["date_added"].dt.year
    df["date_added"] = df["date_added"].dt.strftime("%B %d, %Y")
    print("Sample data generated successfully!")