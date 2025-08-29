# Analysis of Global Workout Search Trends (2018-2023)

## My Motivation: From Internship Experience to Deeper Skills

Having gained practical experience in data analysis during my internship, I understand that the foundation of any valuable insight is clean, well-structured data. This project began as an opportunity to revisit fundamental data processing concepts, inspired by a DataCamp course, and to build upon them with a professional software engineering mindset.

My goal was to construct a complete, professional, and end-to-end data analysis pipeline—from raw data to actionable insights—that showcases best practices I've learned both in theory and in practice.

## The Story: From Tutorial to Professional Tool

The foundational concept for this project came from DataCamp, providing a great starting point for the analysis. I saw an opportunity to significantly expand upon it by engineering a more robust and professional solution.

My objective was to take a simple analysis and transform it into a resilient, automated, and well-documented software tool that reflects real-world data workflows. This `README.md` documents both the findings of the analysis and the engineering decisions I made to elevate the project.

### Data Source
The datasets used in this analysis were provided by DataCamp and represent anonymized and aggregated Google Trends data for various workout-related keywords from 2018 to 2023, stored in the `data/raw` directory.

---

## Project Architecture & Key Features

This project is structured as a two-stage data pipeline, separating data preparation from analysis. This is a best practice that ensures a clean, maintainable, and robust workflow.

### 1. Data Preparation Pipeline (`data_preparation.py`)
A dedicated ETL (Extract, Transform, Load) script that serves as the foundation for all analysis.
*   **Extract:** Connects to multiple raw CSV files located in the `data/raw` directory.
*   **Transform:** Performs data cleaning, merges the different datasets, standardizes column names, and models the data into clean, analysis-ready tables.
*   **Load:** Saves two new, clean datasets (`processed_timeseries_data.csv` and `processed_geo_data.csv`) into the `data/processed` directory, completely decoupling the analysis from the raw source files.

### 2. Analysis & Visualization (`main.py`)
A modular application that consumes only the clean, prepared data to generate insights.
*   **Data Quality Assurance:** Integrates a dedicated data quality check as the first step, verifying the integrity of the processed data before any analysis begins.
*   **Interactive Command-Line Interface (CLI):** Built with `argparse`, allowing a user to run specific parts of the analysis on demand for targeted reporting.
*   **Automated Report Generation:** Automatically saves all generated plots to the `images/` directory for use in reports and this documentation.

---

## Key Questions Explored

1.  How has the general interest in "workout" evolved, and when did it peak?
2.  What was the impact of the COVID-19 pandemic on searches for "Home Workout" vs. "Gym Workout"?
3.  How did the popularity of "Home Workout" directly compete with "Gym Workout" over this period?
4.  Which country has the highest overall interest in workouts?
5.  Between the Philippines and Malaysia, which has a stronger market for "Home Workout" products?

---

## Key Findings & Visualizations

### 1. Overall Interest Peaked During the Pandemic
The global search interest for the term "workout" saw a dramatic spike in early 2020, which directly correlates with the onset of global lockdowns.

![Overall Trends Plot](images/1_overall_trends.png)

### 2. "Home Workout" Dominated During COVID-19
During the pandemic, "Home Workout" searches massively outpaced "Gym Workout." Post-pandemic, gym-related searches have recovered, but "Home Workout" remains a strong competitor.

![Keyword Trends Plot](images/2_keyword_trends.png)

### 3. The Dominance Shift: Home vs. Gym
This unique analysis plots the difference in search volume between "Home Workout" and "Gym Workout." It clearly shows that before 2020, gym workouts were consistently more popular (orange area). The pandemic caused a massive and immediate shift in favor of home workouts (green area).

![Home vs Gym Dominance Plot](images/3_home_vs_gym_dominance.png)

### 4. Geographical Interest: Philippines Leads in Home Workouts
The analysis of geographical data shows that while some countries have high overall workout interest, specific markets show unique trends. When comparing potential expansion markets for home workout products, the Philippines shows significantly higher search interest than Malaysia.

![Geo Comparison Plot](images/4_geo_comparison.png)

---

## Technologies Used
- Python (Pandas, Matplotlib)
- Git & GitHub
- Anaconda

---

## How to Run This Project

This project requires a two-step process: first, run the data preparation pipeline to create the clean datasets, then run the main analysis script to generate insights and visualizations.

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/hishamsalih2000/workout-trend-analysis.git
    cd workout-trend-analysis
    ```

2.  **Set Up the Environment**
    ```bash
    conda create --name workout-market-analysis python=3.9
    conda activate workout-market-analysis
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Data Preparation Pipeline (Crucial First Step)**
    This script takes the raw data from `data/raw`, performs cleaning and merging, and saves the final, analysis-ready datasets into `data/processed`.
    ```bash
    python data_preparation.py
    ```

5.  **Run the Analysis**
    After the preparation script has run successfully, you can now run the main analysis script on the clean data. The interactive command-line interface allows you to run the full analysis or specific parts.

    *   **To run the full analysis (generates all plots):**
        ```bash
        python main.py --analysis all
        ```

    *   **To run only the geographical analysis:**
        ```bash
        python main.py --analysis geo
        ```

    *   **(Other analysis options)**
        ```bash
        python main.py --analysis overall
        python main.py --analysis keywords
        python main.py --analysis dominance
        ```