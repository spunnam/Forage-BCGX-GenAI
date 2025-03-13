# Forage-BCGX-GenAI
# AI-Powered Financial Chatbot

## Project Overview

This project focuses on developing an AI-powered chatbot designed to transform complex financial data into actionable insights. The chatbot aims to assist GFC in making informed financial decisions by making intricate data more accessible and understandable.

## Objectives

- Extract and analyze financial data from SEC 10-K filings.
- Develop a rule-based chatbot to provide predefined financial insights.
- Enhance chatbot capabilities using natural language processing (NLP) and machine learning (ML).
- Seamlessly integrate real-time financial data for accurate decision-making.
- Provide an intuitive and user-friendly interface for financial analysis.

## Project Phases

### **Phase 1: Data Extraction & Initial Analysis**

- Manually extract financial data (Total Revenue, Net Income, Total Assets, Total Liabilities, Cash Flow from Operating Activities) for Microsoft, Tesla, and Apple.
- Compile extracted data into an Excel spreadsheet for structured analysis.
- Use Python (pandas) to analyze trends and calculate year-over-year changes.
- Document findings and prepare for chatbot integration.

### **Phase 2: Chatbot Development**

- Design a rule-based chatbot to answer predefined financial queries.
- Implement chatbot logic using Python (if-else statements or Flask for a web-based interface).
- Map analyzed financial data to structured chatbot responses.
- Test and document chatbot functionality.

### **Phase 3: Advanced Enhancements (Future Scope)**

- Integrate NLP capabilities to allow more dynamic user interactions.
- Implement ML algorithms to improve chatbot accuracy over time.
- Enable real-time data integration for up-to-date financial insights.
- Enhance UX design for improved accessibility and usability.

## Tech Stack

- **Programming Language:** Python
- **Data Analysis:** pandas, Jupyter Notebook
- **Web Framework (Optional):** Flask
- **Data Sources:** SEC EDGAR Database (10-K Filings)
- **Version Control:** GitHub

## Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run Jupyter Notebook for Data Analysis:**
   ```bash
   jupyter notebook
   ```
4. **Run the Chatbot (CLI version):**
   ```bash
   python chatbot.py
   ```
5. **(Optional) Run Flask Web App:**
   ```bash
   python app.py
   ```

## Usage

- **Data Analysis:** Open `Task_1_Data_Analysis.ipynb` to review financial trends.
- **Chatbot Interaction:** Run `chatbot.py` to interact with the rule-based chatbot.
- **Future Enhancements:** Contributions for NLP and ML-based improvements are welcome.

## Contribution Guidelines

- Fork the repository and create a new branch for your changes.
- Submit a pull request with a clear description of your modifications.
- Ensure your code is well-documented and follows PEP8 guidelines.

## License

This project is licensed under the MIT License.

## Contact

For any queries or collaboration opportunities, reach out to the me.


