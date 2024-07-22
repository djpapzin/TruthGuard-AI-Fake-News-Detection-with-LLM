import os
from together import Together

# Retrieve the API key
api_key = os.getenv('TOGETHER_API_KEY')

if not api_key:
  raise ValueError("TOGETHER_API_KEY not found. Please set it in your environment variables.")

# Initialize the Together client
client = Together(api_key=api_key)

# Define a function to classify news
def classify_news(article):
  system_prompt = "You are an AI model fine-tuned to classify news articles as real or fake. Respond with 'Real' or 'Fake' based on the given article."
  prompt = f"{system_prompt}\n\nArticle: {article}\n\nClassification:"
  try:
      output = client.completions.create(
          model="reemamemon/Meta-Llama-3-8B-Instruct-fake-news-detection-2024-07-20-17-48-54-aeb6d725",
          prompt=prompt,
          max_tokens=10,  # Limit the response length to ensure a concise output
          temperature=0.0,  # Set temperature to 0 to make the output deterministic
          top_p=1.0,
          stop=["\n"]
      )
      return output.choices[0].text.strip()
  except Exception as e:
      return f"An error occurred: {str(e)}"

# Test the model with a sample article
if __name__ == "__main__":
    sample_article = "The earth is square"
    result = classify_news(sample_article)
    print(f"Classification result: {result}")

    # You can add more test cases here
