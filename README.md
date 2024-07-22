# TruthGuard-AI Backend

## Overview

TruthGuard-AI is an AI-driven fake news detection system that uses a fine-tuned Llama 3 model to classify news articles as real or fake in real-time. This backend service provides an API endpoint for news article classification.

## Features

- Real-time classification of news articles
- Uses Together AI's fine-tuned Llama 3 model
- Flask-based API for easy integration
- Supports both system and user messages for context
- Basic error handling and logging

## Prerequisites

- Python 3.7 or later
- Flask
- Together AI account and API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/djpapzin/TruthGuard-AI.git
   cd TruthGuard-AI
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Together AI API key in:
   ```
   export TOGETHER_API_KEY='your_api_key_here'
   ```

## Usage

1. Start the Flask server:
   ```
   python app.py
   ```

2. The API will be available at `http://localhost:5000`

3. To classify a news article, send a POST request to `/classify` with the following JSON payload:
   ```json
   {
     "article": "Your news article text here"
   }
   ```

4. The API will respond with a classification result:
   ```json
   {
     "classification": "real" or "fake"
   }
   ```

## API Endpoints

- `POST /classify`: Classifies a news article as real or fake
- `GET /`: Returns a simple message (can be used as a health check)

## Model Information

The backend uses a fine-tuned Llama 3 model hosted on Together AI. The model was trained on the WELFake Dataset, which contains a collection of real and fake news articles.

## Future Improvements

- Implement user authentication and rate limiting
- Add support for batch classification
- Integrate with a frontend application for a complete user interface
- Implement caching to improve performance
- Add more comprehensive error handling and input validation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.