import os
from flask import Flask, request, jsonify
from together import Together

app = Flask(__name__)

# Initialize the Together client
api_key = os.environ.get('TOGETHER_API_KEY')
client = Together(api_key=api_key)

def classify_news(article):
    system_message = {
        "role": "system",
        "content": (
            "You are a fake news detection AI. Your task is to determine whether the following news article is Real or Fake. "
            "Respond strictly with 'Real' or 'Fake'. Do not provide any other text.\n"
        )
    }
    user_message = {
        "role": "user",
        "content": article
    }
    
    try:
        response = client.chat.completions.create(
            model="reemamemon/Meta-Llama-3-8B-Instruct-fake-news-detection-2024-07-20-17-48-54-aeb6d725",
            messages=[system_message, user_message],
            max_tokens=10,
            temperature=0.0,  # Making the model more deterministic
            top_p=1.0,
            top_k=50,
            repetition_penalty=1.0,
            stop=["\n"]
        )
        response_text = response.choices[0].message.content.strip().lower()
        print(f"DEBUG: System message - {system_message}")  # Debug logging for system message
        print(f"DEBUG: User message - {user_message}")  # Debug logging for user message
        print(f"DEBUG: Model response - {response_text}")  # Debug logging for model response

        if response_text not in ["real", "fake"]:
            print(f"ERROR: Invalid response - {response_text}")  # Error logging for invalid response
            return "Article could not be analyzed, please try again with a different article"

        return response_text
    except Exception as e:
        print(f"ERROR: {str(e)}")  # Error logging
        return f"An error occurred: {str(e)}"

@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()
    article = data.get('article', '')
    result = classify_news(article)
    return jsonify({"classification": result})

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Please use POST method to classify news"})

if __name__ == '__main__':
    app.run(debug=True)
