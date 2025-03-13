from data_loader import final_report


def validate_inputs(company, year):
    """Validate company name and fiscal year"""
    valid_companies = final_report['company'].unique().tolist()
    valid_years = final_report['fiscal_year'].unique().tolist()

    if company not in valid_companies:
        return f"Invalid company. Available options: {', '.join(valid_companies)}."

    if year not in valid_years:
        return f"Invalid fiscal year. Available years: {', '.join(map(str, valid_years))}."

    return None  # No validation errors
