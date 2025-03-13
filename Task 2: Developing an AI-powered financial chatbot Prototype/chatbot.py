import os
from data_loader import final_report, summary_report
from validators import validate_inputs


def get_financial_data(company, year):
    """Fetch financial data for the given company and year"""
    company_data = final_report[(final_report['company'] == company) & (final_report['fiscal_year'] == year)]
    return company_data.iloc[0] if not company_data.empty else None


def get_summary_data(company):
    """Fetch year-over-year average growth rates from summary_report"""
    summary_data = summary_report[summary_report['company'] == company]
    return summary_data.iloc[0] if not summary_data.empty else None


def financial_chatbot(query, company, year):
    """Handle chatbot queries and return appropriate responses"""

    # Validate user input
    validation_error = validate_inputs(company, year)
    if validation_error:
        return validation_error

    # Get financial data for the given fiscal year
    data = get_financial_data(company, year)

    # Get summary data (year-over-year average growth)
    summary_data = get_summary_data(company)

    if data is None:
        return f"No financial data available for {company} in {year}."

    # Predefined responses for single-year data
    responses = {
        "What is the total revenue?": f"The Total Revenue for {company} in {year} is $ {data['total_revenue']:,.2f}",
        "What is the Net Income?": f"The Net Income for {company} in {year} is $ {data['net_income']:,.2f}",
        "What is the sum of total assets?": f"The Total Assets for {company} in {year} is $ {data['total_assets']:,.2f}",
        "What is the sum of total liabilities?": f"The Total Liabilities for {company} in {year} is $ {data['total_liabilities']:,.2f}",
        "What is cash flow from operating activities?": f"The Cash Flow from Operating Activities for {company} in {year} is $ {data['cash_flow_operating_activities']:,.2f}",
        "What is the revenue growth(%) ?": f"The Revenue Growth for {company} in {year} is {data['revenue growth (%)']:.2f}%",
        "What is the net income growth(%) ?": f"The Net Income Growth for {company} in {year} is {data['net income growth (%)']:.2f}%",
        "What is the assets growth(%) ?": f"The Assets Growth for {company} in {year} is {data['total assets growth (%)']:.2f}%",
        "What is the liabilities growth(%) ?": f"The Liabilities Growth for {company} in {year} is {data['total liabilities growth (%)']:.2f}%",
        "What is the cash flow from operations growth(%) ?": f"The Cash Flow from Operations Growth for {company} in {year} is {data['cash flow growth (%)']:.2f}%"
    }

    # Predefined responses for year-over-year average growth
    if summary_data is not None:
        summary_responses = {
            "What is the year by year average revenue growth rate(%)?": f"The Yearly Average Revenue Growth Rate for {company} (2022-2024) is {summary_data['revenue growth (%)']:.2f}%",
            "What is the year by year average net income growth rate(%)?": f"The Yearly Average Net Income Growth Rate for {company} (2022-2024) is {summary_data['net income growth (%)']:.2f}%",
            "What is the year by year average assets growth rate(%)?": f"The Yearly Average Assets Growth Rate for {company} (2022-2024) is {summary_data['total assets growth (%)']:.2f}%",
            "What is the year by year average liabilities growth rate(%)?": f"The Yearly Average Liabilities Growth Rate for {company} (2022-2024) is {summary_data['total liabilities growth (%)']:.2f}%",
            "What is the year by year average cash flow from operations growth rate(%)?": f"The Yearly Average Cash Flow from Operations Growth Rate for {company} (2022-2024) is {summary_data['cash flow growth (%)']:.2f}%"
        }
        responses.update(summary_responses)

    return responses.get(query, "Sorry, I can only provide information on predefined queries.")


def get_available_questions():
    """Read available questions from a file"""
    questions_file = "questions.txt"
    if not os.path.exists(questions_file):
        return "Error: Questions file not found."

    with open(questions_file, "r") as file:
        return file.read()
