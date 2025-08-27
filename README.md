## Key Questions Explored

1.  How has the general interest in "workout" evolved, and when did it peak?
2.  What was the impact of the COVID-19 pandemic on searches for "Home Workout" vs. "Gym Workout"?
3.  How did the popularity of "Home Workout" directly compete with "Gym Workout" over this period?
4.  Which country has the highest overall interest in workouts?
5.  Between the Philippines and Malaysia, which has a stronger market for "Home Workout" products?

## Key Findings & Visualizations

### 1. Overall Interest Peaked During the Pandemic
The global search interest for the term "workout" saw a dramatic spike in early 2020, which directly correlates with the onset of global lockdowns.

![Overall Trends Plot](images/1_overall_trends.png)

### 2. "Home Workout" Dominated During COVID-19
During the pandemic, "Home Workout" searches massively outpaced "Gym Workout." Post-pandemic, gym-related searches have recovered, but "Home Workout" remains a strong competitor.

![Keyword Trends Plot](images/2_keyword_trends.png)

### 3. The Dominance Shift: Home vs. Gym
This analysis plots the difference in search volume between "Home Workout" and "Gym Workout." It clearly shows that before 2020, gym workouts were consistently more popular (orange area). The pandemic caused a massive and immediate shift in favor of home workouts (green area).

![Home vs Gym Dominance Plot](images/3_home_vs_gym_dominance.png)

### 4. Geographical Interest: Philippines Leads in Home Workouts
The analysis of geographical data shows that while some countries have high overall workout interest, specific markets show unique trends. When comparing potential expansion markets for home workout products, the Philippines shows significantly higher search interest than Malaysia.

![Geo Comparison Plot](images/4_geo_comparison.png)

## How to Run This Project

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/hishamsalih2000/workout-trend-analysis
    cd workout-market-analysis
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

4.  **Run the Analysis**
    The script is an interactive tool. You can run the full analysis or specific parts.

    *   **To run the full analysis (generates all plots):**
        ```bash
        python main.py
        ```
        *(This is the same as running `python main.py --analysis all`)*
    *   **To run only the overall trends analysis:**
        ```bash
        python main.py --analysis overall
        ```
        **To run only the keywords trends analysis:**
        ```bash
        python main.py --analysis keywords
        ```
    *   **To run only the home vs. gym dominance analysis:**
        ```bash
        python main.py --analysis dominance
        ```
    *   **To run only the geographical analysis:**
        ```bash
        python main.py --analysis geo
        ```