"""CSV cleaning and splitting helpers reconstructed from report section 5.3."""

import pandas as pd
from sklearn.model_selection import train_test_split


def load_and_clean_data(file_path):
    """Load a CSV and apply the cleaning steps shown in section 5.3."""
    df = pd.read_csv(file_path)
    df["url"] = df["url"].str.replace(r"https?://(www\.)?", "", regex=True)
    df = df.drop_duplicates()
    df = df.dropna()
    return df


def split_data(df):
    """Return URL and label train/test splits using the report's settings."""
    X_train, X_test, y_train, y_test = train_test_split(
        df["url"], df["label"], test_size=0.2, random_state=42
    )
    return X_train, X_test, y_train, y_test
