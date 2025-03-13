# Task 1 - Data Extraction & Initial Analysis

## Task Instructions
Your task is to manually extract key financial data for the last three fiscal years from the 10-K filings of Microsoft, Tesla, and Apple. Following the data collection, you will use Python to analyze this data, focusing on trends and insights that could inform the development of an AI-powered financial chatbot.

## Step 1: Data Extraction
### Navigate to the SEC's EDGAR database:
- [Microsoft](https://www.sec.gov/edgar/searchedgar/companysearch.html)
- [Tesla](https://www.sec.gov/edgar/searchedgar/companysearch.html)
- [Apple](https://www.sec.gov/edgar/searchedgar/companysearch.html)

### Manual Extraction:
For each company, find the 10-K filings for the last three fiscal years and extract the following financial figures:
- Total Revenue
- Net Income
- Total Assets
- Total Liabilities
- Cash Flow from Operating Activities

### Organize Your Data:
Compile the extracted data into an Excel spreadsheet for easy reference during your Python analysis.

## Step 2: Preparing Your Jupyter Notebook Environment
### Install Jupyter (if not already installed):
Install Jupyter using pip:
```bash
pip install notebook
```

### Launch Jupyter Notebook:
```bash
jupyter notebook
```
This command should open Jupyter in your web browser.

### Create a New Notebook:
In the Jupyter interface, create a new notebook for your analysis.

## Step 3: Python Analysis in Jupyter
### Import Pandas:
At the beginning of your notebook, import the pandas library to work with your data.
```python
import pandas as pd
```

### Load Your Data:
Convert your Excel file to a CSV file for easier handling, then load it into a DataFrame.
```python
df = pd.read_csv('path_to_your_csv_file.csv')
```

### Analyzing Trends with Pandas:
Use pandas to calculate year-over-year changes for each financial metric. You can do this by creating new columns in your DataFrame that represent the percentage change from one year to the next.
```python
df['Revenue Growth (%)'] = df.groupby(['Company'])['Total Revenue'].pct_change() * 100
df['Net Income Growth (%)'] = df.groupby(['Company'])['Net Income'].pct_change() * 100
```
Explore other aggregate functions or groupings to analyze the data across different dimensions (by company, over years, etc.).

### Summarizing Findings:
Conclude your analysis by summarizing your findings directly in the notebook. Use markdown cells to add narrative explanations of your analysis, discussing the trends and changes in financial metrics you've identified.

## Step 4: Documentation and Submission
### Document Your Analysis:
Use the markdown feature in Jupyter Notebook to document your methodology, observations, and conclusions throughout the notebook.

### Export Your Notebook:
Once your analysis is complete, export your Jupyter Notebook as a PDF or HTML file for submission. You can do this from the "File" menu in Jupyter, selecting "Download as" and then choosing your preferred format.

By following this approach, you will focus on the core analytical aspects using pandas within a Jupyter Notebook, providing a clear, documented narrative of your financial analysis process. By the end of this task, you'll have a comprehensive understanding of how to analyze financial data programmatically, a valuable skill set for data-driven decision-making.

