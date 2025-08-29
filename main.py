# main.py

import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import argparse
import logging

# Import configuration from our config file
import config

# --- Setup Basic Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """
    Loads a CSV file into a pandas DataFrame with error handling.
    """
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Successfully loaded data from {file_path}")
        return df
    except FileNotFoundError:
        logging.error(f"Error: The file at {file_path} was not found.")
        sys.exit(1) # Exit the script with an error code
    except Exception as e:
        logging.error(f"An unexpected error occurred while loading {file_path}: {e}")
        sys.exit(1)

def perform_data_quality_checks(df, file_name):
    """
    Performs and logs basic data quality checks on a DataFrame.
    """
    logging.info(f"--- Performing Data Quality Checks on {file_name} ---")
    
    # Check for missing values
    missing_values = df.isnull().sum().sum()
    if missing_values > 0:
        logging.warning(f"Found {missing_values} missing values.")
    else:
        logging.info("No missing values found.")

    # Check for duplicate rows
    duplicate_rows = df.duplicated().sum()
    if duplicate_rows > 0:
        logging.warning(f"Found {duplicate_rows} duplicate rows.")
    else:
        logging.info("No duplicate rows found.")
    
    # Log the data types
    logging.info("DataFrame Info:")
    df.info()
    print("\n")

def ensure_images_dir_exists():
    """
    Checks if the images directory from the config exists, and creates it if not.
    """
    if not os.path.exists(config.IMAGES_DIR):
        logging.info(f"Images directory '{config.IMAGES_DIR}' not found. Creating it.")
        os.makedirs(config.IMAGES_DIR)

def analyze_overall_trends():
    """
    Loads and plots the overall 'workout' search trend.
    """
    logging.info("--- 1. Analyzing Overall Workout Trends ---")
    df = load_data(config.PROCESSED_TIMESERIES_FILE)
    perform_data_quality_checks(df, 'processed_timeseries_data.csv')
    df['month'] = pd.to_datetime(df['month'])

    plt.figure(figsize=(config.PLOT_WIDTH, config.PLOT_HEIGHT))
    plt.plot(df['month'], df['workout_worldwide'], color='navy')
    plt.xlabel('Month')
    plt.ylabel('Relative Search Interest')
    plt.title('Global "Workout" Search Interest Trend (2018-2023)')
    plt.grid(True, linestyle='--', alpha=0.6)
    
    output_path = os.path.join(config.IMAGES_DIR, '1_overall_trends.png')
    plt.savefig(output_path, bbox_inches='tight')
    logging.info(f"Plot saved to {output_path}")
    #plt.show()

    peak_idx = df['workout_worldwide'].idxmax()
    year_str = df.loc[peak_idx, 'month'].strftime('%Y')
    logging.info(f"Finding: The peak year for 'workout' searches was {year_str}.\n")

def analyze_keyword_trends():
    """
    Analyzes and plots trends for 'Home Workout' vs. 'Gym Workout'.
    """
    logging.info("--- 2. Analyzing Specific Keyword Trends (Home vs. Gym) ---")
    df = load_data(config.PROCESSED_TIMESERIES_FILE)
    perform_data_quality_checks(df, 'processed_timeseries_data.csv')
    df['month'] = pd.to_datetime(df['month'])

    plt.figure(figsize=(config.PLOT_WIDTH, config.PLOT_HEIGHT))
    plt.plot(df['month'], df['home_workout_worldwide'], label='Home Workout')
    plt.plot(df['month'], df['gym_workout_worldwide'], label='Gym Workout')
    
    covid_start = pd.to_datetime('2020-03-01')
    covid_end = pd.to_datetime('2021-06-01')
    plt.axvspan(covid_start, covid_end, color='red', alpha=0.15, label='COVID-19 Peak Period')

    plt.xlabel('Month')
    plt.ylabel('Relative Search Interest')
    plt.title('Search Interest: Home Workout vs. Gym Workout')
    plt.legend(loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.6)
    
    output_path = os.path.join(config.IMAGES_DIR, '2_keyword_trends.png')
    plt.savefig(output_path, bbox_inches='tight')
    logging.info(f"Plot saved to {output_path}")
    #plt.show()

    covid_data = df[(df['month'] >= covid_start) & (df['month'] <= covid_end)]
    peak_covid = covid_data[['home_workout_worldwide', 'gym_workout_worldwide', 'home_gym_worldwide']].max().idxmax().replace('_worldwide', '')
    most_recent_month = df['month'].max()
    current_data = df[df['month'] == most_recent_month]
    current = current_data[['home_workout_worldwide', 'gym_workout_worldwide', 'home_gym_worldwide']].idxmax(axis=1).values[0].replace('_worldwide', '')
    logging.info(f"Finding: The peak keyword during COVID was '{peak_covid}'.")
    logging.info(f"Finding: The most popular keyword currently is '{current}'.\n")


def analyze_home_vs_gym_dominance():
    """
    Calculates and plots the dominance shift between 'Home' and 'Gym' workouts.
    """
    logging.info("--- 3. Unique Analysis: The Battle of Home vs. Gym ---")
    df = load_data(config.PROCESSED_TIMESERIES_FILE)
    perform_data_quality_checks(df, 'processed_timeseries_data.csv')
    df['month'] = pd.to_datetime(df['month'])
    
    df['home_vs_gym_diff'] = df['home_workout_worldwide'] - df['gym_workout_worldwide']

    plt.figure(figsize=(config.PLOT_WIDTH, config.PLOT_HEIGHT))
    plt.plot(df['month'], df['home_vs_gym_diff'], label='"Home" minus "Gym" Interest')
    plt.axhline(0, color='black', linestyle='--')
    plt.fill_between(df['month'], df['home_vs_gym_diff'], 0, where=df['home_vs_gym_diff'] >= 0, facecolor='green', interpolate=True, alpha=0.2, label='Home More Popular')
    plt.fill_between(df['month'], df['home_vs_gym_diff'], 0, where=df['home_vs_gym_diff'] < 0, facecolor='orange', interpolate=True, alpha=0.2, label='Gym More Popular')
    
    plt.title('Dominance Shift: "Home Workout" vs. "Gym Workout"')
    plt.xlabel('Month')
    plt.ylabel('Search Interest Difference')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    output_path = os.path.join(config.IMAGES_DIR, '3_home_vs_gym_dominance.png')
    plt.savefig(output_path, bbox_inches='tight')
    logging.info(f"Plot saved to {output_path}")
    #plt.show()

    max_diff_date = df.loc[df['home_vs_gym_diff'].idxmax(), 'month'].strftime('%B %Y')
    logging.info(f"Finding: The dominance of 'Home Workout' peaked in {max_diff_date}.\n")

def analyze_geo_trends():
    """
    Analyzes the processed geographical workout data to find top countries for
    general and home-specific workout searches.
    """
    logging.info("--- 4. Analyzing Geographical Trends ---")
    
    # Load the single, clean, pre-merged geographical dataset
    df_geo = load_data(config.PROCESSED_GEO_FILE)
    perform_data_quality_checks(df_geo, 'processed_geo_data.csv')
    
    # Find the top country overall
    top_country = df_geo.loc[df_geo['workout_2018_2023'].idxmax()]['country']
    logging.info(f"Finding: The country with the highest overall workout interest is '{top_country}'.")

    # Compare Philippines vs Malaysia for home workout interest
    filtered_df = df_geo[df_geo['country'].isin(['Philippines', 'Malaysia'])]
    home_workout_geo = filtered_df.loc[filtered_df['home_workout_2018_2023'].idxmax()]['country']
    logging.info(f"Finding: Between the Philippines and Malaysia, '{home_workout_geo}' has the higher interest in home workouts.\n")

    # Create a bar chart for the comparison
    plt.figure(figsize=(8, 5))
    plt.bar(filtered_df['country'], filtered_df['home_workout_2018_2023'], color=['#FFC300', '#C70039'])
    plt.xlabel('Country')
    plt.ylabel('Relative Search Interest (2018-2023)')
    plt.title('Comparative "Home Workout" Interest')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    output_path = os.path.join(config.IMAGES_DIR, '4_geo_comparison.png')
    plt.savefig(output_path, bbox_inches='tight')
    logging.info(f"Plot saved to {output_path}")
    #plt.show()

# --- Main Execution Block ---
if __name__ == '__main__':
    # making the script interactive
    parser = argparse.ArgumentParser(description="Analyze workout search trends.")
    parser.add_argument(
        '--analysis', 
        choices=['all', 'overall', 'keywords', 'dominance', 'geo'], 
        default='all',
        help="Specify which analysis to run: 'overall', 'keywords', 'dominance', 'geo', or 'all'."
    )
    args = parser.parse_args()

    # Ensure the directory for saving images exists before running any analysis
    ensure_images_dir_exists()

    logging.info(f"Starting analysis for: {args.analysis}\n")

    if args.analysis == 'all':
        analyze_overall_trends()
        analyze_keyword_trends()
        analyze_home_vs_gym_dominance()
        analyze_geo_trends()
    elif args.analysis == 'overall':
        analyze_overall_trends()
    elif args.analysis == 'keywords':
        analyze_keyword_trends()
    elif args.analysis == 'dominance':
        analyze_home_vs_gym_dominance()
    elif args.analysis == 'geo':
        analyze_geo_trends()
        
    logging.info("--- Analysis Complete ---")