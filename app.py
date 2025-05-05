from flask import Flask, render_template, request, jsonify
import random
import re

app = Flask(__name__)

# Define the regular expressions for various queries
patterns = [
    # Greeting
    (re.compile(r'(hi|hello|hey|good morning|good afternoon|good evening)', re.I), [
        "Hello! How can I assist you with admissions today?Hi there! Feel free to ask me anything about admission."
    ]),
    
    # Application Deadline / Last Date to Apply
    (re.compile(r'(What is the application deadline?|last date|due date|closing date)', re.I), [
        "The application deadline is August 31, 2024. Please submit your application before August 31, 2024."
    ]),
    
    # Course and Program Queries
    (re.compile(r'(courses|programs|degrees|majors)', re.I), [
        "We offer courses in Computer Science, Business, Psychology, Engineering, and more.Our programs include B.Tech, MBA, BBA, and MSc."
    ]),
    
    # Fee / Tuition / Cost Queries
   (re.compile(r'(fee|tuition|cost|price)', re.I), [
        "B.Tech: $10,000/year, MBA: $15,000/year. Fees vary by course.Visit our website for a detailed fee structure."
    ]),
    
    # How to Apply Queries
     (re.compile(r'(apply|admission|application|process|steps|how)', re.I), [
        "1. Fill out the online form\n2. Upload documents\n3. Pay application fee\n4. Fill out the form\n5. upload documents and wait for confirmation."
    ]),
    
    # Scholarship / Financial Aid Queries
    (re.compile(r'(scholarship|financial aid|grant)', re.I), [
        "We offer merit-based and need-based scholarships.Scholarships are available — apply during the admission process."
    ]),
    
    # Contact Info Queries
    (re.compile(r'(contact|email|phone|address)', re.I), [
        "Email: admission@university.edu | Phone: +1-234-567-890. Our office is open Mon–Fri, 9 AM to 5 PM."
    ]),
    
    # Campus Location Queries
    (re.compile(r'(campus|location|where)', re.I), [
        "The main campus is located at 123 University Avenue, Cityville. We have campuses in multiple cities. Main campus: Cityville."
    ]),
    
    # Catch-all / Unrecognized Query
    (re.compile(r'.*', re.I), [
        "Sorry, I didn't quite understand that. Could you ask a specific question? Can you please clarify your question about admissions?"
    ])
]

def get_bot_response(message):
    print(f"User message: {message}")  # Debugging log
    for pattern, responses in patterns:
        if pattern.search(message):
            print(f"Pattern matched: {pattern}")  # Debugging log
            return random.choice(responses)
    return "Sorry, something went wrong."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['message']
    print(f"Received message: {user_message}")  # Debugging log
    bot_response = get_bot_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)