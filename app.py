import os
from flask import Flask, request, jsonify
from together import Together

app = Flask(__name__)

# Initialize the Together client
api_key = os.environ.get('TOGETHER_API_KEY')
client = Together(api_key=api_key)

def classify_news(article):
    system_prompt = "You are an AI model fine-tuned to classify news articles as real or fake. Respond with 'Real' or 'Fake' based on the given article."
    prompt = f"{system_prompt}\n\nArticle: {article}\n\nClassification:"
    try:
        output = client.completions.create(
            model="reemamemon/Meta-Llama-3-8B-Instruct-fake-news-detection-2024-07-20-17-48-54-aeb6d725",
            prompt=prompt,
            max_tokens=10,
            temperature=0.0,
            top_p=1.0,
            stop=["\n"]
        )
        return output.choices[0].text.strip()
    except Exception as e:
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
    app.run()
