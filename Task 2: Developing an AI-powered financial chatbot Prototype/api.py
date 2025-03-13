from flask import Flask, request, jsonify
from chatbot import financial_chatbot, get_available_questions

app = Flask(__name__)


@app.route('/chat', methods=['GET'])
def chat():
    """Web-based API endpoint for chatbot"""
    query = request.args.get('query')
    company = request.args.get('company')
    year = request.args.get('year')

    if not query or not company or not year:
        return jsonify({"response": "Error: Please provide query, company, and year."})

    try:
        year = int(year)
    except ValueError:
        return jsonify({"response": "Error: Year must be a number."})

    response = financial_chatbot(query, company, year)
    return jsonify({"response": response})


@app.route('/queries', methods=['GET'])
def queries():
    """API endpoint to get available questions"""
    return jsonify({"queries": get_available_questions()})


if __name__ == '__main__':
    app.run(debug=True)
