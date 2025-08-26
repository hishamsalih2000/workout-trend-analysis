## How to Run This Project

1.  **Clone the Repository**
    ```bash
    git clone <your-github-repo-url>
    cd workout-market-analysis
    ```

2.  **Set Up the Environment**
    It is recommended to use a virtual environment.
    ```bash
    # Create and activate the environment (e.g., using conda)
    conda create --name workout-market-analysis python=3.9
    conda activate workout-market-analysis
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Analysis**
    The script is now an interactive tool. You can run the full analysis or specific parts of it. The script will log its progress and save plots to the `images/` directory.

    *   **To run the full analysis:**
        ```bash
        python main.py
        ```
        *(This is the same as running `python main.py --analysis all`)*

    *   **To run only the overall trends analysis:**
        ```bash
        python main.py --analysis overall
        ```

    *   **To run only the home vs. gym dominance analysis:**
        ```bash
        python main.py --analysis dominance
        ```