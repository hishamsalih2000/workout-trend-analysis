# data_preparation.py

import pandas as pd
import os
import logging

# --- Setup Basic Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main ETL function to prepare and merge all raw data sources into clean,
    analysis-ready datasets.
    """
    logging.info("--- Starting Data Preparation Pipeline (ETL) ---")

    # Define file paths
    raw_dir = os.path.join('data', 'raw')
    processed_dir = os.path.join('data', 'processed')

    # Ensure processed directory exists
    os.makedirs(processed_dir, exist_ok=True)

    # --- 1. EXTRACT ---
    try:
        df_workout = pd.read_csv(os.path.join(raw_dir, 'workout.csv'))
        df_keywords = pd.read_csv(os.path.join(raw_dir, 'three_keywords.csv'))
        df_geo = pd.read_csv(os.path.join(raw_dir, 'workout_geo.csv'))
        df_keywords_geo = pd.read_csv(os.path.join(raw_dir, 'three_keywords_geo.csv'))
        logging.info("Successfully extracted all raw data files.")
    except FileNotFoundError as e:
        logging.error(f"Error extracting data: {e}. Make sure raw files are in data/raw/")
        return

    # --- 2. TRANSFORM (TIME-SERIES DATA) ---
    df_workout['month'] = pd.to_datetime(df_workout['month'], format='%Y-%m')
    df_keywords['month'] = pd.to_datetime(df_keywords['month'], format='%Y-%m')
    df_merged_ts = pd.merge(df_workout, df_keywords, on='month', how='outer')
    logging.info("Successfully transformed and merged time-series data.")

    # --- 2. TRANSFORM (GEOGRAPHICAL DATA) ---
    # Standardize column names for a clean merge ('country' vs 'Country')
    df_keywords_geo.rename(columns={'Country': 'country'}, inplace=True)
    
    # Merge the two geographical dataframes into a single, comprehensive one
    df_merged_geo = pd.merge(df_geo, df_keywords_geo, on='country', how='outer')
    logging.info("Successfully transformed and merged geographical data.")

    # --- 3. LOAD ---
    # Define output paths for our new, clean datasets
    ts_output_path = os.path.join(processed_dir, 'processed_timeseries_data.csv')
    geo_output_path = os.path.join(processed_dir, 'processed_geo_data.csv')
    
    # Save the processed data to new files in the processed directory
    df_merged_ts.to_csv(ts_output_path, index=False)
    df_merged_geo.to_csv(geo_output_path, index=False)
    
    logging.info(f"Clean time-series data saved to {ts_output_path}")
    logging.info(f"Clean geographical data saved to {geo_output_path}")
    logging.info("--- ETL Complete ---")

if __name__ == '__main__':
    main()