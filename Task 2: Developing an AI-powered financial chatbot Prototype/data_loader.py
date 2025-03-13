import os
import pandas as pd

# Define file paths
DATA_DIR = os.path.dirname(os.path.abspath(__file__))  # Get script directory
FINAL_REPORT_FILE = os.path.join(DATA_DIR, "final-data-report-task1.csv")
SUMMARY_REPORT_FILE = os.path.join(DATA_DIR, "growth_report.csv")


def load_data():
    """Load financial datasets and clean column names"""
    try:
        final_report = pd.read_csv(FINAL_REPORT_FILE)
        summary_report = pd.read_csv(SUMMARY_REPORT_FILE)
    except FileNotFoundError as e:
        print(f"Error: {e}. Please check file paths.")
        exit(1)

    # Normalize column names
    final_report.columns = final_report.columns.str.strip().str.lower()
    summary_report.columns = summary_report.columns.str.strip().str.lower()

    return final_report, summary_report


# Load data globally
final_report, summary_report = load_data()
