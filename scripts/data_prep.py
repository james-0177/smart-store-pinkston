"""
Module 2: Initial Script to Verify Project Setup
File: scripts/data_prep.py
"""

import pathlib
import sys
import pandas as pd

# For local imports, temporarily add project root to Python sys.path
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# Now we can import local modules
from utils.logger import logger
from scripts.data_scrubber import DataScrubber

# Constants
DATA_DIR: pathlib.Path = PROJECT_ROOT.joinpath("data")
RAW_DATA_DIR: pathlib.Path = DATA_DIR.joinpath("raw")
PREPARED_DATA_DIR: pathlib.Path = DATA_DIR.joinpath("prepared")

def read_raw_data(file_name: str) -> pd.DataFrame:
    """Read raw data from CSV."""
    file_path: pathlib.Path = RAW_DATA_DIR.joinpath(file_name)
    try:
        logger.info(f"Reading raw data from {file_path}.")
        return pd.read_csv(file_path)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return pd.DataFrame()  # Return an empty DataFrame if the file is not found
    except Exception as e:
        logger.error(f"Error reading {file_path}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame if any other error occurs

def process_data(file_name: str) -> None:
    """Process raw data by reading it into a pandas DataFrame object."""
    df = read_raw_data(file_name)
    if df.empty:
        logger.warning(f"No data to process for {file_name}. Skipping.")
        return
    
    try:
        scrubber = DataScrubber(df)

        #Clean data: remove duplicates and handle missing values (drop rows with missing data)
        scrubber.remove_duplicate_records()
        scrubber.handle_missing_data(drop=True)

        #Save the cleaned data to the prepared directory
        cleaned_file_path = PREPARED_DATA_DIR.joinpath(file_name)
        scrubber.df.to_csv(cleaned_file_path, index=False)
        logger.info(f"Cleaned data saved to {cleaned_file_path}")

    except Exception as e:
        logger.error(f"Error processing {file_name}: {e}")

def main() -> None:
    """Main function for processing customer, product, and sales data."""
    logger.info("Starting data preparation...")

    #Process the raw data files
    process_data("customers_data.csv")
    process_data("products_data.csv")
    process_data("sales_data.csv")

    logger.info("Data preparation complete.")

if __name__ == "__main__":
    main()