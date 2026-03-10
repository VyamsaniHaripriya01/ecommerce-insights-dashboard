import pandas as pd
import streamlit as st

@st.cache_data
def load_data(filepath):
    """
    Load the cleaned Flipkart dataset from CSV.
    """
    try:
        df = pd.read_csv(filepath)

        # Optional: convert rating to numeric if needed
        if 'rating' in df.columns:
            df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

        return df
    except Exception as e:
        raise RuntimeError(f"Failed to load data from {filepath}: {e}")
