from chatbot import financial_chatbot, get_available_questions
from data_loader import final_report


def run_cli_chatbot():
    """Run chatbot in CLI mode"""
    print("\n------------------------------------------------")
    while True:
        user_input = input("\nEnter 'Hi' to start the chatbot session; type 'exit' to quit: ").strip().lower()

        if user_input == "exit":
            break
        elif user_input == "hi":
            print("\nWelcome to AI-Driven Financial Chatbot!")
            print("Available companies:", ', '.join(final_report['company'].unique()))

            company = input("Enter company name: ").strip().capitalize()
            try:
                year = int(input("Enter the fiscal year (e.g., 2022, 2023, 2024): ").strip())
            except ValueError:
                print("Invalid input. Please enter a numeric fiscal year.")
                continue

            print("\nIf you need a list of queries, type: 'show queries'")
            query = input("\nEnter your query: ").strip()

            if query.lower() == "show queries":
                print(get_available_questions())
                continue

            response = financial_chatbot(query, company, year)
            print(response)
        else:
            print("Invalid input. Restart and enter 'Hi' to start.")


if __name__ == "__main__":
    run_cli_chatbot()
