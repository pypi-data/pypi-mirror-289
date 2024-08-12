import pandas as pd
import pyarrow.parquet as pq
from .config import get_env_variable

def load_data(file_path):
    """
    Load data from a Parquet file into a pandas DataFrame.
    
    Args:
        file_path (str): Path to the Parquet file.
    
    Returns:
        pandas.DataFrame: The data from the Parquet file.
    """
    return pd.read_parquet(file_path)

def save_data(df, file_path):
    """
    Save a pandas DataFrame to a Parquet file.
    
    Args:
        df (pandas.DataFrame): The DataFrame to save.
        file_path (str): Path where the Parquet file will be saved.
    """
    df.to_parquet(file_path, index=False)