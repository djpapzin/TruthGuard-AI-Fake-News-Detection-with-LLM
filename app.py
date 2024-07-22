# api/classify.py

import os
from http.server import BaseHTTPRequestHandler
from together import Together
import json

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

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        
        article = data.get('article', '')
        result = classify_news(article)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = json.dumps({"classification": result})
        self.wfile.write(response.encode())

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = json.dumps({"message": "Please use POST method to classify news"})
        self.wfile.write(response.encode())